from transformers import AutoTokenizer,AutoModel,AutoConfig
import torch
from config import CLASSIFY_PTUNING_PRE_SEQ_LEN,KEYWORDS_PTUNING_PRE_SEQ_LEN,NL2SQL_PTUNING_PRE_SEQ_LEN,CLASSIFY_CHECKPOINT_PATH,KEYWORDS_CHECKPOINT_PATH,NL2SQL_CHECKPOINT_PATH
class GLM:
    def __init__(self,user_id) -> None:
        self.model_name = r'D:\sth_funny\citi2024\chatglm3-6b'
        # self.tokenizer = None
        self.checkpoint_path = None
        self.config = None
        self.model = None
        self.length = None
        # self.user_id = user_id
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, trust_remote_code=True)
        # self.model = AutoModel.from_pretrained(self.model_name,trust_remote_code=True).quantize(4).cuda()
        # self.model = self.model.eval()
    def unload_model(self):
        del self.tokenizer
        del self.model
        del self.checkpoint_path
        torch.cuda.empty_cache()

    def keyword_retrieval(self,path=None):
        self.config = AutoConfig.from_pretrained(self.model_name, trust_remote_code=True,pre_seq_len=KEYWORDS_PTUNING_PRE_SEQ_LEN)
        self.model = AutoModel.from_pretrained(self.model_name, config=self.config, trust_remote_code=True)
        self.length = KEYWORDS_PTUNING_PRE_SEQ_LEN
        self.checkpoint_path = KEYWORDS_CHECKPOINT_PATH

    def classification_retrieval(self,path = None):
        self.config = AutoConfig.from_pretrained(self.model_name, trust_remote_code=True,pre_seq_len=CLASSIFY_PTUNING_PRE_SEQ_LEN)
        self.model = AutoModel.from_pretrained(self.model_name, config=self.config, trust_remote_code=True)
        self.length = CLASSIFY_PTUNING_PRE_SEQ_LEN
        self.checkpoint_path = CLASSIFY_CHECKPOINT_PATH

    def nl2sql_retrieval(self,path=None):
        self.config = AutoConfig.from_pretrained(self.model_name, trust_remote_code=True,pre_seq_len=NL2SQL_PTUNING_PRE_SEQ_LEN)
        self.model = AutoModel.from_pretrained(self.model_name, config=self.config, trust_remote_code=True)
        self.length = NL2SQL_PTUNING_PRE_SEQ_LEN
        self.checkpoint_path = NL2SQL_CHECKPOINT_PATH

    def __get_keyword_prompt(self,query):
        question_prompt = '''
                请帮我从以下句子中提取关键词。这些关键词是句子中最重要、最能概括句子主题的词汇。通过这些关键词，你可以更好地理解句子的内容。你只需要回答文本中的关键词,不要回答其他内容.
                用户输入：
                '''
        keywords_prompt = f"{question_prompt} {query}"
        return keywords_prompt
    
    def __get_classification_prompt(self,query):
        question_prompt = f"\n        请问“{query}”是属于下面哪个类别的问题?\n        A: 公司基本信息,包含股票简称, 公司名称, 外文名称, 法定代表人, 注册地址, 办公地址, 公司网址网站, 电子信箱等.\n        B: 财务报表相关内容, 包含资产负债表, 现金流量表, 利润表 中存在的字段, 包括费用, 资产，金额，收入等.\n        C: 股东股本相关问题, 包含十大股东、股权投资、股本结构等.\n        D: 分析类问题，包括评估股东风险、公司控股风险等开放性问题.\n        E: 评价类问题，包括基于现有文本进行情况的总结、评价公司的股权结构合理情况、集中度情况等.\n        你只需要回答字母编号, 不要回答字母编号及选项文本外的其他内容."
        return question_prompt
    
    def __get_nl2sql_prompt(self,query):
        question_prompt = ''''''
        nl2sql_prompt = f"{question_prompt} {query}"
        return nl2sql_prompt
    
    def load_model(self):
        prefix_state_dict = torch.load(self.checkpoint_path)
        new_prefix_state_dict = {}
        for k, v in prefix_state_dict.items():
            if k.startswith("transformer.prefix_encoder."):
                new_prefix_state_dict[k[len("transformer.prefix_encoder."):]] = v
        self.model.transformer.prefix_encoder.load_state_dict(new_prefix_state_dict)

    def get_response(self,question,query_type=0):
        if query_type == 0:
            self.classification_retrieval()
            prompt = self.__get_classification_prompt(question)
            self.load_model()
        elif query_type == 1:
            self.keyword_retrieval()
            prompt = self.__get_keyword_prompt(question)
            self.load_model()
        elif query_type == 2:
            self.nl2sql_retrieval()
            prompt = self.__get_nl2sql_prompt(question)
            self.load_model()
        else:
            self.model =  AutoModel.from_pretrained(self.model_name,trust_remote_code=True).quantize(4).cuda()
            self.length = 512
        response, history = self.model.chat(self.tokenizer, prompt, history=[],max_length=self.length,top_p=1, do_sample=False,temperature=0.001)
        return response
        
# tokenizer = AutoTokenizer.from_pretrained(r'D:\sth_funny\citi2024\chatglm3-6b', trust_remote_code=True)
# model = AutoModel.from_pretrained(r'D:\sth_funny\citi2024\chatglm3-6b',trust_remote_code=True).quantize(4).cuda()
# model = model.eval()
# response, history = model.chat(tokenizer, "你好", history=[])
# print(response)
# print(history)
# response, history = model.chat(tokenizer, "我不好", history=[])
# print(response)
# print(history)