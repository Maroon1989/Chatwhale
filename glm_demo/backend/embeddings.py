from chromadb import Documents, EmbeddingFunction,Embeddings
from sentence_transformers import SentenceTransformer
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer,AutoModel
# class MyEmbeddingFunction(EmbeddingFunction):
#     def __init__(self,model_path,rank_type='normal',batch_size=8,**kwargs) -> None:
#         self.rank_type = rank_type
#         self.batch_size = batch_size
#         self.model = None
#         self.tokenizer = None
#         if 'bge' not in model_path:
#             if rank_type != 'normal':
#                 raise ValueError('Wrong rank type!')
#             else:
#                 self.model = SentenceTransformer(model_path)
#         else:
#             if rank_type=='normal':
#                 self.model = SentenceTransformer(model_path)
#             else:
#                 self.tokenizer = AutoTokenizer.from_pretrained(model_path)
#                 self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
#                 self.model.cuda()
#                 self.model.eval()
#     def __call__(self, input: Documents) -> Embeddings:
#         return super().__call__(input)
class MyEmbeddingFunction(EmbeddingFunction):
    def __init__(self,model_path,batch_size=8,**kwargs):
        super().__init__(**kwargs)
        self.model = AutoModel.from_pretrained(model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.device = torch.device('cuda')
        self.model.half()
        self.model.to(self.device)
        self.batch_size = batch_size
        self.model_path = model_path
        # self.model = SentenceTransformer(model_path)
        print("embedding model for bge or gte loads successfully!")
    # def compute_kernel_bias(self,vecs,n_components=384):
    def __call__(self, input: Documents) -> Embeddings:
        texts = [t.replace("\n"," ") for t in input]
        num_texts = len(texts)
        embeddings = []
        for start in range(0, num_texts, self.batch_size):
            end = min(start + self.batch_size, num_texts)
            batch_texts = texts[start:end]
            encoded_input = self.tokenizer(batch_texts, max_length=512, padding=True, truncation=True,
                                           return_tensors='pt')
            encoded_input.to(self.device)
            with torch.no_grad():
                model_output = self.model(**encoded_input)
                # Perform pooling. In this case, cls pooling.
                if 'gte' in self.model_path:
                    batch_embeddings = model_output.last_hidden_state[:, 0]
                else:
                    batch_embeddings = model_output[0][:, 0]

                batch_embeddings = torch.nn.functional.normalize(batch_embeddings, p=2, dim=1)
                embeddings.extend(batch_embeddings.tolist())

        # sentence_embeddings = np.array(sentence_embeddings)
        # self.W, self.mu = self.compute_kernel_bias(sentence_embeddings)
        # sentence_embeddings = (sentence_embeddings+self.mu) @ self.W
        # self.W, self.mu = torch.from_numpy(self.W).cuda(), torch.from_numpy(self.mu).cuda()
        return embeddings
        # return super().__call__(input)

