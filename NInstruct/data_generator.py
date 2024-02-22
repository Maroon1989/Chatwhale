import pandas as pd 
import numpy as np 
import json
import pickle
from tqdm import tqdm
import os
stock_list = pd.read_excel(r'D:\sth_funny\citi2024\Chatwhale\NInstruct\data\AB股代码.xlsx')
# stock_list = stock_list['证券代码'].unique().tolist()
path = r'NInstruct\dataset'
# for i in tqdm(range(len(stock_list['证券代码']))):
for i in tqdm(range(len(stock_list['证券代码']))):
    data = {}
    data['id'] = i
    data['security_code'] = stock_list['证券代码'][i]
    data['stock_name'] = stock_list['证券名称'][i]
    data['stock_code'] = stock_list['股票代码'][i]
    filename =  data['security_code']+'.pkl'
    pickle_path = os.path.join(path,filename)
    with open(pickle_path,'wb') as file:
        pickle.dump(data,file,protocol=pickle.DEFAULT_PROTOCOL)

    # data['qualification'] = None
    # data['logo'] = None
    # data['']