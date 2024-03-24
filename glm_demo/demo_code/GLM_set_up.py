from transformers import AutoTokenizer,AutoModel,AutoConfig
import torch
from config import CLASSIFY_PTUNING_PRE_SEQ_LEN,KEYWORDS_PTUNING_PRE_SEQ_LEN,NL2SQL_PTUNING_PRE_SEQ_LEN
from config import CLASSIFY_PATH,KEYWORDS_PATH,NL2SQL_PATH
from transformers.generation.utils import LogitsProcessorList
import gc

import pdb

class GLMforWhale:
    def __init__(self,model_name='GLMforWhale',config_path = r'/root/autodl-tmp/chatglm-6b',user_id=1,dialog_id = 1) -> None:
        self.cls_path = CLASSIFY_PATH
        self.key_path = KEYWORDS_PATH
        self.sql_path = NL2SQL_PATH
        
        self.model_name = model_name
        self.config_path = config_path
        self.model = None
        self.length = None
        self.user_id = user_id
        self.dialog_id = dialog_id
        self.tokenizer = AutoTokenizer.from_pretrained(self.config_path, trust_remote_code=True)
        # self.model = AutoModel.from_pretrained(self.model_name,trust_remote_code=True).quantize(4).cuda()
        # self.model = self.model.eval()
        self.last_query = None

    def unload_model(self):
        # if self.tokenizer is not None:
        #     del self.tokenizer
        if self.model is not None:
            del self.model
        torch.cuda.empty_cache()
        # self.tokenizer = None
        self.model = None
        gc.collect()

    def keyword_retrieval(self,path=None): #Load Keyword retrieval
        self.unload_model()
        self.tokenizer = AutoTokenizer.from_pretrained(self.config_path, trust_remote_code=True)
        self.config = AutoConfig.from_pretrained(self.config_path, trust_remote_code=True,pre_seq_len=KEYWORDS_PTUNING_PRE_SEQ_LEN)
        self.model = AutoModel.from_pretrained(self.key_path, config=self.config, trust_remote_code=True).cuda()
        self.model.eval()
        self.length = KEYWORDS_PTUNING_PRE_SEQ_LEN

    def classification_retrieval(self,path = None):
        self.unload_model()
        self.tokenizer = AutoTokenizer.from_pretrained(self.config_path, trust_remote_code=True)
        self.config = AutoConfig.from_pretrained(self.config_path, trust_remote_code=True,pre_seq_len=CLASSIFY_PTUNING_PRE_SEQ_LEN)
        
        # pdb.set_trace()
        self.model = AutoModel.from_pretrained(self.cls_path, config=self.config, trust_remote_code=True).cuda()
        self.model.eval()
        self.length = CLASSIFY_PTUNING_PRE_SEQ_LEN

    def nl2sql_retrieval(self,path=None):
        # pdb.set_trace()

        self.unload_model()
        self.tokenizer = AutoTokenizer.from_pretrained(self.config_path, trust_remote_code=True)
        self.config = AutoConfig.from_pretrained(self.config_path, trust_remote_code=True, pre_seq_len=NL2SQL_PTUNING_PRE_SEQ_LEN)
        self.model = AutoModel.from_pretrained(self.sql_path, config=self.config, trust_remote_code=True, device_map="auto").cuda()
        self.model.eval()
        self.length = NL2SQL_PTUNING_PRE_SEQ_LEN

    def __get_keyword_prompt(self,query):
        question_prompt = '''
                请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词，你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.
                用户输入：
                '''
        keywords_prompt = f"{question_prompt} {query}"
        return keywords_prompt
    
    def __get_classification_prompt(self,query):
        question_prompt = '''
                请问“{query}”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容.
                用户输入：
                '''
        return question_prompt
    
    def __get_nl2sql_prompt(self,query):
        question_prompt = '''
                你是一名Mysql数据库开发人员，精通Mysql数据库sql代码编写，你需要根据已知表名、字段名和用户输入的问题编写sql代码\n表名：偿债能力\n字段名：[股票代码,股票简称,统计截止日期,报表类型编码,流动比率,速动比率,营运资金,利息保障倍数A,资产负债率,权益乘数]\n表名：盈利能力\n字段名：[股票代码,股票简称,统计截止日期,报表类型编码,净资产收益率（ROE）A]\n表名：经营能力\n字段名：[股票代码,股票简称,统计截止日期,报表类型编码,应收账款周转率A,存货周转率A,应付账款周转率A]\n表名：十大股东\n字段名：[证券代码,统计截止日期,股东名称,持股排名,持股数量,持股比例(百分比),股东类型]\n表名：实际控制人\n字段名：[证券代码,统计截止日期,判断标准,实际控制人名称,实际控制人拥有上市公司所有权比例,实际控制人拥有上市公司控制权比例]\n表名：股权变更\n字段名：[证券代码,股份增持方,股份减持方,第一次公告日期,本次变动数量,本次变动数量占总股本的比例(百分比)]\n表名：基本信息\n字段名：[股票代码,股票简称,统计截止日期,行业名称,注册具体地址,公司办公地址,中文全称,公司成立日期,首次上市日期,所属省份,所属城市,主营业务]\n表名：关联交易\n字段名：[证券代码,统计截止日期,公告日期,关联交易事项,交易日期,交易期限,交易内容]\n表名：诉讼仲裁\n字段名：[证券代码,证券简称,公告日期,事件内容] \n注意对问题中的中文数字（xx亿、xx千万、xx万）进行阿拉伯数字转换，如：一个亿、一亿转换为100000000，一千万转换为10000000，两千万转换为20000000，一百万转换为1000000，五千万转换为50000000\n要求sql代码中的字段名必须是已知字段名，不得新增字段名\n\n示例模板：\n\"\"\"\n用户输入：在北京注册的上市公司中，2020年净资产收益率最高的十家公司有哪些，分别多少？\n\nsql如下：\n```sql\n SELECT a.股票代码, a.股票简称, a.净资产收益率（ROE）A FROM 盈利能力 AS a JOIN 基本信息 AS b ON (b.统计截止日期>='2020-01-01' AND b.统计截止日期<='2020-12-31' AND b.注册具体地址 LIKE '%北京%' AND a.股票代码=b.股票代码 AND a.股票简称=b.股票简称 AND a.统计截止日期=b.统计截止日期) ORDER BY 净资产收益率（ROE）A DESC LIMIT 10; \n```\n\n用户输入：注册地在上海或广州的公司中，2020年营运资金超过五千万的公司有几家？\n\nsql如下：\n```sql\n SELECT COUNT(1) FROM 偿债能力 AS a JOIN 基本信息 AS b ON (b.统计截止日期>='2020-01-01' AND b.统计截止日期<='2020-12-31' AND (b.注册具体地址 LIKE '%上海%' OR b.注册具体地址 LIKE '%广州%') AND a.营运资金>'50000000' AND a.股票代码=b.股票代码 AND a.股票简称=b.股票简称 AND a.统计截止日期=b.统计截止日期); \n``` \"\"\"\n请根据以下用户输入，输出sql代码。\n用户输入：公司裕同科技近期是否有重要股东的增减？"}, {"role": "assistant", "content": "根据用户输入问题，编写sql代码如下：
                用户输入:
                '''
        nl2sql_prompt = f"{question_prompt} {query}"
        return nl2sql_prompt
    
    # def load_model(self):
    #     prefix_state_dict = torch.load(self.checkpoint_path)
    #     new_prefix_state_dict = {}
    #     for k, v in prefix_state_dict.items():
    #         if k.startswith("transformer.prefix_encoder."):
    #             new_prefix_state_dict[k[len("transformer.prefix_encoder."):]] = v
    #     self.model.transformer.prefix_encoder.load_state_dict(new_prefix_state_dict)

    def get_response(self,question,query_type=0):

        if query_type == 0:
            if self.last_query!=query_type:
                self.last_query = query_type
                self.classification_retrieval()
            prompt = self.__get_classification_prompt(question)
            # self.load_model()
        elif query_type == 1:
            if self.last_query!=query_type:
                self.last_query = query_type
                self.keyword_retrieval()
            prompt = self.__get_keyword_prompt(question)
            # self.load_model()
        elif query_type == 2:
            if self.last_query!=query_type:
                self.last_query = query_type
                self.nl2sql_retrieval()
            prompt = self.__get_nl2sql_prompt(question)
        else:
            self.unload_model()
            self.model =  AutoModel.from_pretrained(self.config_path,trust_remote_code=True).cuda()
            self.model.eval()
            self.length = 512
            prompt = question
        # pdb.set_trace()
        response, history = self.model.chat(self.tokenizer, prompt, history=[])
        # pdb.set_trace()
        
        '''
        # Back-up Method
        input = tokenizer.build_chat_input(prompt, role='user').to(torch.device("cuda"))
        eos_token_id = [tokenizer.eos_token_id, tokenizer.get_command("<|user|>"),
                    tokenizer.get_command("<|observation|>")]
        gen_kwargs = {"max_new_tokens": 2048,
                  "do_sample": True,
                  "top_p": 0.8,
                  "temperature": 0.95,
                  "logits_processor": LogitsProcessorList(),
                  "repetition_penalty": 1.1,
                  "length_penalty": 1,
                  "num_beams": 1,
                  'stop_sequences': ['<|user|>']
                  }

        output_text=""
        for output in self.model.stream_generate(**input, past_key_values=None,
                                        eos_token_id=eos_token_id, return_past_key_values=False,
                                        **gen_kwargs):
            output = output.tolist()[0][len(input["input_ids"][0]):]
            response = tokenizer.decode(output)
            output_text = response
        '''

        
        return response, history
        
# tokenizer = AutoTokenizer.from_pretrained(r'/root/autodl-tmp/chatglm-6b', trust_remote_code=True)

# model = AutoModel.from_pretrained('/root/autodl-tmp/chatglm-6b',trust_remote_code=True).cuda()
# model = model.eval()
# response, history = model.chat(tokenizer, "你好", history=[])
# print(response)

# # pdb.set_trace()
# print(history)
# response, history = model.chat(tokenizer, "我不好", history=[])
# print(response)
# print(history)

# GLM=GLMforWhale('model',r'/root/autodl-tmp/chatglm-6b',1)
# response, history=GLM.get_response('注册地在上海或广州的公司中，2020年营运资金超过五千万的公司有几家？',2)
# print(response)

# response2, history=GLM.get_response('你好？',0)
# print(response2)
# # print(history)
# GLM.unload_model()
# response2, history=GLM.get_response('南京药丸公司股东的主营业务和公司业务领域有何关联？',2)
# print(response2)
# pdb.set_trace()