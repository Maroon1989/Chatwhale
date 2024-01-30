import pandas as pd 
import numpy as np 
import json
import pickle
stock_list = pd.read_csv(r'D:\金融软工\algorithm\后端\月线行情.csv')
stock_list = stock_list['ts_code'].unique().tolist()
for i in stock_list:
    data = {}
    data['subject'] = i
    data['object']
    data['finance'] = []
    data['qualification'] = None
    data['logo'] = None
    data['']