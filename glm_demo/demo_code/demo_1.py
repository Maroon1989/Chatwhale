from transformers import AutoTokenizer,AutoModel
class GLM:
    def __init__(self) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained(r'D:\sth_funny\citi2024\chatglm3-6b', trust_remote_code=True)
        self.model = AutoModel.from_pretrained(r'D:\sth_funny\citi2024\chatglm3-6b',trust_remote_code=True).quantize(4).cuda()
        self.model = self.model.eval()
    def get_response(self,question):
        response, history = self.model.chat(self.tokenizer, question, history=[])
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