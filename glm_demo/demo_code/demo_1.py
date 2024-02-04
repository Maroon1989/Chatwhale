from transformers import AutoTokenizer,AutoModel
tokenizer = AutoTokenizer.from_pretrained(r'D:\sth_funny\citi2024\chatglm3-6b', trust_remote_code=True)
model = AutoModel.from_pretrained(r'D:\sth_funny\citi2024\chatglm3-6b',trust_remote_code=True).quantize(4).cuda()
model = model.eval()
response, history = model.chat(tokenizer, "你好", history=[])
print(response)