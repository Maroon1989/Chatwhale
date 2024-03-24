import requests
url = "http://127.0.0.1:5001/ask"
# url = "http://172.17.0.5:5001/ask"
data = {
    'user_id':'1',
    'num':1,
    'classification':True,
    'question': '南京药丸公司股东的主营业务和公司业务领域有何关联？',
    'query_type': True
    # '1':0
}
# print(data['1'])
response = requests.get(url=url,data=data)
# print(response.text)
# response = requests.get(url=url)