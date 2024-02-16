import torch
def rerank(docs, query, rerank_tokenizer, rerank_model, k=5):
    docs_ = []
    for item in docs:
        if isinstance(item, str):
            docs_.append(item)
        else:
            docs_.append(item.page_content)
    docs = list(set(docs_))
    pairs = []
    for d in docs:
        pairs.append([query, d])
    with torch.no_grad():
        inputs = rerank_tokenizer(pairs, padding=True, truncation=True, return_tensors='pt', max_length=512).to('cuda')
        # for key in inputs:
        #     inputs[key] = inputs[key].to('cuda')
        scores = rerank_model(**inputs, return_dict=True).logits.view(-1, ).float().cpu().tolist()
    docs = [(docs[i], scores[i]) for i in range(len(docs))]
    docs = sorted(docs, key = lambda x: x[1], reverse = True)
    docs_ = []
    for item in docs:
        # if item[1]>0:
        #     docs_.append(item[0])
        docs_.append(item[0])
    return docs_[:k]