import chromadb
from embeddings import MyEmbeddingFunction
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from reranker import rerank
tokenizer = AutoTokenizer.from_pretrained(r'D:\sth_funny\citi2024\RAG_glm\hugging-face-model\bge-reranker-base')
rerank_model = AutoModelForSequenceClassification.from_pretrained(r'D:\sth_funny\citi2024\RAG_glm\hugging-face-model\bge-reranker-base')
client  = chromadb.PersistentClient(path=r"D:\sth_funny\citi2024\chroma_data")
def get_query(query):
    collection1 = client.get_or_create_collection("first_documents",embedding_function=MyEmbeddingFunction(model_path=r'D:\sth_funny\citi2024\RAG_glm\hugging-face-model\gte-small-zh'))
    collection2 = client.get_or_create_collection("first_documents",embedding_function=MyEmbeddingFunction(model_path=r'D:\sth_funny\citi2024\RAG_glm\hugging-face-model\bge-small-zh-v1.5'))
    result1 = collection1.query(
        query_texts=[query],
        n_results=10
    )
    result2 = collection2.query(
        query_texts=[query],
        n_results=10
    )
    rerank_model.cuda()
    rerank_model.eval()
    result = rerank(result1['documents'][0]+result2['documents'][0],query=query,rerank_tokenizer=tokenizer,rerank_model=rerank_model,k=10)
    return result

# # client  = chromadb.Client()
# # collection = client.create_collection("first_document")
# collection = client.get_or_create_collection("first_documents",embedding_function=MyEmbeddingFunction(model_path=r'D:\sth_funny\citi2024\RAG_glm\hugging-face-model\gte-small-zh'))
# collection.add(
#     documents=["今天天气真好！","今天是晴天","明天是阴天","后天是节假日","今天去吃饭","明天去游泳","后天去健身"],
#     ids = ["1","2","3","4","5","6","7"]
# )
# result1 = collection.query(
#     query_texts=["明天天气如何？"],
#     n_results=3
#     # where={"metadata_field": "is_equal_to_this"},
#     # where_document={"$contains":"search_string"}
# )
# collection2 = client.get_or_create_collection("first_documents",embedding_function=MyEmbeddingFunction(model_path=r'D:\sth_funny\citi2024\RAG_glm\hugging-face-model\bge-small-zh-v1.5'))
# collection2.add(
#     documents=["今天天气真好！","今天是晴天","明天是阴天","后天是节假日","今天去吃饭","明天去游泳","后天去健身"],
#     ids = ["1","2","3","4","5","6","7"]
# )
# result2 = collection2.query(
#     query_texts=["明天天气如何？"],
#     n_results=3,
#     # where={"metadata_field": "is_equal_to_this"},
#     # where_document={"$contains":"search_string"}
# )
# # print(result1)
# tokenizer = AutoTokenizer.from_pretrained(r'D:\sth_funny\citi2024\RAG_glm\hugging-face-model\bge-reranker-base')
# rerank_model = AutoModelForSequenceClassification.from_pretrained(r'D:\sth_funny\citi2024\RAG_glm\hugging-face-model\bge-reranker-base')
# rerank_model.cuda()
# rerank_model.eval()
# result = rerank(result1['documents'][0]+result2['documents'][0],query="明天天气如何？",rerank_tokenizer=tokenizer,rerank_model=rerank_model,k=3)
# print(result)
# collection.add(
#     documents=["This is "]
# )