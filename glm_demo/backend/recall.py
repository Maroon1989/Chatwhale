from flask import Flask,render_template,request,jsonify
from flask import g
import sys

sys.path.append('/root/autodl-tmp/Chatwhale-main-latest/Chatwhale-main/glm_demo/backend')
sys.path.append('/root/autodl-tmp/Chatwhale-main-latest/Chatwhale-main/glm_demo/demo_code')
sys.path.append('/root/autodl-tmp/Chatwhale-main-latest/Chatwhale-main/database')


from GLM_set_up import GLMforWhale
import requests
# from chroma_db import get_query
import pymysql
from Mysql_config import host,user,password,database
import os
import pandas as pd
from sql_correct import *
from prompt_utils import sql_prompt,RAG_prompt
app=Flask(__name__)
try:
    connection = pymysql.connect(
        host= host,
        user= user,
        password= password,
        database= database
    )
    cursor = connection.cursor()
except:
    cursor = None
glm_path = '/root/autodl-tmp/Chatwhale-main-latest/Chatwhale-main/glm_demo/backend/user_info/glm_dict.csv'

# g.glm_dict = {
#     '1': {0:GLMforWhale(0)},
#     '1': {1:GLMforWhale(1)},
#     '2': {1:GLMforWhale(2)}
# }
#list里面元素的example
# element_example = \
# {
#     "user_id"
# }

#主服务器所在地址
url = 'http://ip'
@app.before_request
def my_before_request():
    if os.path.exists(glm_path):
        # with app.app_context():
        g.glm_data = pd.read_csv(glm_path)
        # print(g.glm_data)
        g.glm_dict = {}
        for i in range(len(g.glm_data)):
            user_id = str(g.glm_data['user_id'][i])
            dialog_id = g.glm_data['dialog_id'][i]
            if user_id not in g.glm_dict.keys():
                print('a')
                g.glm_dict[user_id] = dict()
                g.glm_dict[user_id][dialog_id] = GLMforWhale(user_id = user_id,dialog_id=dialog_id)
            else:
                print('b')
                g.glm_dict[user_id][dialog_id] = GLMforWhale(user_id = user_id,dialog_id=dialog_id)
            print(g.glm_dict)
    else:
        # with app.app_context():
        g.glm_data = pd.DataFrame(columns=['user_id','dialog_id'])
        g.glm_dict = {}
    # return "Hello World!"    

@app.route('/',methods=['GET'])
def index():
    # if os.path.exists(glm_path):
    #     # with app.app_context():
    #     g.glm_data = pd.read_csv(glm_path)
    #     g.glm_dict = {}
    #     for i in range(len(g.glm_data)):
    #         user_id = g.glm_data['user_id'][i]
    #         dialog_id = g.glm_data['dialog_id'][i]
    #         if user_id not in g.glm_dict.keys():
    #             g.glm_dict[user_id] = {}
    #         else:
    #             g.glm_dict[user_id][dialog_id] = GLMforWhale(user_id = user_id,dialog_id=dialog_id)
    # else:
    #     # with app.app_context():
    #     g.glm_data = pd.DataFrame(columns=['user_id','dialog_id'])
    #     g.glm_dict = {}
    return "Hello World!"
    pass

@app.route('/ask',methods=['GET'])
def ask():
    user_id = request.args.get('user_id')
    num = request.args.get('num', type=int)  # 使用type参数转换为整数
    classification = request.args.get('classification', type=lambda v: v.lower() == 'true')  # 转换字符串'true'/'false'为布尔值
    keyword = request.args.get('keyword', type=lambda v: v.lower() == 'true')
    question = request.args.get('question')
    query_type = request.args.get('query_type', type=lambda v: v.lower() == 'true')
    retrieval = request.args.get('text')
    data = {
        'user_id': user_id,
        'num': num,
        'classification': classification,
        'keyword': keyword,
        'question': question,
        'query_type': query_type,
        'text':retrieval
    }
    
    user_id = data['user_id']
    print(type(user_id))
    classify = data['classification']
    keyword = data['keyword']
    print(classify)
    question  = data['question']
    print(question)
    dialog_id = int(data['num'])
    print(type(dialog_id))
    query_type = data['query_type']
    print(g.glm_dict[user_id][dialog_id])
    model = g.glm_dict[user_id][dialog_id]
    class_result = None
    
    if classify==True:
        try:
            classification = (model.get_response(question,query_type=0))[0]
        except:
            return 201
        print(classification)
        # print(111111111111111111111111)
        # exit(0)
        # classification = 'D'
        if classification!='D' and classification!='E':
            # model.unload_model()
            # keywords = model.get_response(question,query_type=1)
            # nl2_sql_prompt = f"{question},其关键词是{keywords}"
            # model.unload_model()
            nl2_sql_prompt = sql_prompt+question
            try:
                sql_response = model.get_response(nl2_sql_prompt,query_type=2)
            except:
                return None,201
            pattern = r'SELECT[\s\S]*?;'
            # 使用findall方法查找所有匹配的SQL查询
            queries = re.findall(pattern, sql_response[0])[0]
            # model.unload_model()
            answer,ero,sql_cursor = exc_sql(question,queries,cursor)
            # cursor.execute(sql_response)
            # result = cursor.fetchall()
            if ero == '':
                column_names = [column[0] for column in sql_cursor.description]
                markdown_table = ''
                for i in column_names:
                    markdown_table += f"|{i}"
                markdown_table += '\n'+"| ---- |"*len(column_names)+"\n"
                for row in answer:
                    markdown_table+="|"+'|'.join(row[name] for name in column_names)+"|\n"
                full_prompt = f"{question},其中关键数据为列名:{markdown_table}"
            else:
                full_prompt = question
            try:
                model.unload_model()
                response = model.get_response(full_prompt,query_type=3)[0]
                model.unload_model()
            except:
                return None,201
            # model.unload_model()
        else:
            response = classification
        data = {
            "answer":response,
            "classification":classification
        }
        return jsonify(data),200
    elif keyword:
        response = model.get_response(question,query_type=1)
        # nl2_sql_prompt = f"{question},其关键词是{keywords}"
        print("--------------------------------------------")
        print(response)
        return jsonify({'answer':response[0]}),200
    else:
        # True表示下一步进行RAG
        if query_type:
            content = data['text']
            full_prompt = RAG_prompt.format(content,question)
            # full_prompt = f"{RAG_prompt} {question}"
            try:
                response = model.get_response(full_prompt,query_type=3) 
            except:
                return None,201
        else:
            prompt = question
            try:
                response = model.get_response(prompt,query_type=3)
            except:
                return None,201
        return jsonify({'answer':response[0]}),200
    
@app.route('/get_new_dialog',methods=['POST'])
def get_new_dialog():
    # data = request.form
    dialog_id = request.args.get('num', type=int)
    user_id = request.args.get('user_id')
    user_ids = g.glm_data['user_id'].tolist()
    dialog_ids = g.glm_data['dialog_id'].tolist()
    model = GLMforWhale(user_id=user_id,dialog_id=dialog_id)
    print(g.glm_dict)
    if user_id not in g.glm_dict.keys():
        g.glm_dict[user_id] = dict()
    if dialog_id not in g.glm_dict[user_id].keys():
        # g.glm_dict[user_id][dialog_id] = {}
        g.glm_dict[user_id][dialog_id] = model
    # for key,value in g.glm_dict.items():
    #     dialog_list = value.keys()
        dialog_ids.append(dialog_id)
        user_ids.append(user_id)
    print(g.glm_dict)
    try:
        # g.glm_data['user_id'] = user_ids
        # g.glm_data['dialog_id'] = dialog_ids
        g.glm_data = pd.DataFrame({'user_id':user_ids,'dialog_id':dialog_ids})
        g.glm_data.to_csv(glm_path,index=False)
        return jsonify(message=f"New dialog {dialog_id} created."),200  
    except:
        return jsonify(message=f"New dialog {dialog_id} creation failed."),201

@app.route('/delete_dialog',methods=['POST'])
def delete_dialog():
    # data = request.form
    dialog_id = request.args.get('num', type=int)
    user_id = request.args.get('user_id')
    try:
        print(1)
        print(g.glm_dict)
        print(g.glm_data)
        g.glm_dict[user_id][dialog_id].unload_model()
        print(2)
        del g.glm_dict[user_id][dialog_id]
        # for key,value in g.glm_dict.items():
        #     dialog_id = int(value.keys()[0])
        #     user_id = key
        # print(1)
        g.glm_data = g.glm_data[~((g.glm_data['user_id'] == int(user_id)) & (g.glm_data['dialog_id'] == dialog_id))]
        print(g.glm_data)
        g.glm_data.to_csv(glm_path,index=False)
        return jsonify(message=f"Dialog {dialog_id} deleted."),200
    except:
        return jsonify(message=f"Dialog {dialog_id} deletion failed."),201

@app.route('/delete_all_dialogs',methods=['POST'])
def delete_all_dialog():
    # user_id = data['user_id']
    # dialog_id = request.args.get('num', type=int)
    user_id = request.args.get('user_id')
    print(user_id)
    print(type(user_id))
    # data = request.form
    try:
        for dialog_id in g.glm_dict[user_id].keys():
            print(1)
            g.glm_dict[user_id][dialog_id].unload_model()
            print(2)
        del g.glm_dict[user_id]
        print(g.glm_dict)
            # print(3)
        print(g.glm_data)
        g.glm_data = g.glm_data[~(g.glm_data['user_id']==int(user_id))]
        print(4)
        g.glm_data.to_csv(glm_path,index=False)
        return jsonify(message=f"User {user_id} dialogs deleted."),200
    except:
        return jsonify(message=f"User {user_id} dialogs deletion failed."),201
#chat的对话返回不了，classification
#return 状态码写错
#glm_dict的存储问题
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)



