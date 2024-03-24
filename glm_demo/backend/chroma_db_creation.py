import chromadb
from embeddings import MyEmbeddingFunction
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from reranker import rerank
import glob
import sys
sys.path.append(r"D:\sth_funny\citi2024\Chatwhale")
from pdf_parser.paragraph_split import PDFDocumentParser
from pdf_parser.paragraph_split4txt import TXTDocumentParser
# import pdf_parser.file_processor
tokenizer = AutoTokenizer.from_pretrained(r'D:\sth_funny\citi2024\RAG_glm\hugging-face-model\bge-reranker-base')
rerank_model = AutoModelForSequenceClassification.from_pretrained(r'D:\sth_funny\citi2024\RAG_glm\hugging-face-model\bge-reranker-base')
# client = chromadb.HttpClient(host='localhost',port=8000)
def extract_pdf_documents(folder_path):
    file_paths = glob.glob(f'{folder_path}/*')
    documents_list = {}
    for file_path in file_paths:
        parser = PDFDocumentParser(file_path)
        documents = parser.parse_pdf()
        documents_list[file_path] = documents
    return documents_list
def extract_txt_documents(folder_path):
    file_paths = glob.glob(f'{folder_path}/*')
    documents_list = {}
    for file_path in file_paths:
        parser = TXTDocumentParser(file_path)
        documents = parser.parse_txt()
        documents_list[file_path] = documents
    return documents_list
def vector_db_embed(documents_list,collection):
    for key,documents in documents_list.items():
        document = [doc.page_content for doc in documents]
        metadata = [doc.metadata for doc in documents]
        ids = [key+str(index) for index,doc in enumerate(documents)]
        if len(ids) !=0:
            collection.add(
                documents=document,
                metadatas = metadata,
                ids = ids
            )
txt_list = extract_txt_documents(r'D:\sth_funny\citi2024\dataset\bs_challenge_financial_14b_dataset\pdf_txt_file')
client  = chromadb.PersistentClient(path=r"D:\sth_funny\citi2024\chroma_data")
# collection = client.create_collection("first_document")
collection = client.get_or_create_collection("first_documents",embedding_function=MyEmbeddingFunction(model_path=r'D:\sth_funny\citi2024\RAG_glm\hugging-face-model\gte-small-zh'))
collection2 = client.get_or_create_collection("first_documents",embedding_function=MyEmbeddingFunction(model_path=r'D:\sth_funny\citi2024\RAG_glm\hugging-face-model\bge-small-zh-v1.5'))
vector_db_embed(txt_list,collection=collection)
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
# print(result1)
# tokenizer = AutoTokenizer.from_pretrained(r'D:\sth_funny\citi2024\RAG_glm\hugging-face-model\bge-reranker-base')
# rerank_model = AutoModelForSequenceClassification.from_pretrained(r'D:\sth_funny\citi2024\RAG_glm\hugging-face-model\bge-reranker-base')
# rerank_model.cuda()
# rerank_model.eval()
# result = rerank(result1['documents'][0]+result2['documents'][0],query="明天天气如何？",rerank_tokenizer=tokenizer,rerank_model=rerank_model,k=3)
# print(result)
# collection.add(
#     documents=["This is "]
# )