from flask import Flask,render_template,request,jsonify
import demo_code
from Chatwhale.glm_demo.demo_code.GLM_set_up import GLM
import requests
from chroma_db import get_query
import pymysql
from Chatwhale.database.Mysql_config import host,user,password,database
import os
import pandas as pd
from sql_correct import *
from prompt_utils import sql_prompt,RAG_prompt
connection = pymysql.connect(
    host= host,
    user= user,
    password= password,
    database= database
)
cursor = connection.cursor()
glm_dict = {
    '1': {1:GLM()},
    '2': {1:GLM()}
}
#list里面元素的example
# element_example = \
# {
#     "user_id"
# }
app=Flask(__name__)
#主服务器所在地址
url = 'http://ip'

@app.route('/')
def index():
    pass

@app.route('/ask',method=['GET'])
def ask():
    data = request.form
    user_id = data['user_id']
    classify = data['classification']
    question  = data['question']
    dialog_id = data['num']
    query_type = data['query_type']
    model = glm_dict[user_id][dialog_id]
    class_result = None
    if classify:
        classification = model.get_response(question,query_type=0)
        if classification!='D' and classification!='E':
            model.unload_model()
            # keywords = model.get_response(question,query_type=1)
            # nl2_sql_prompt = f"{question},其关键词是{keywords}"
            # model.unload_model()
            nl2_sql_prompt = sql_prompt+question
            sql_response = model.get_response(nl2_sql_prompt,query_type=2)
            model.unload_model()
            answer,ero,sql_cursor = exc_sql(question,sql_response,cursor)
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
            response = model.get_response(full_prompt,query_type=3)
            model.unload_model()
        else:
            response = classification
        data = {
            "answer":response,
            "classification":classification
        }
        return jsonify({'answer':response}),200
    else:
        # True表示下一步进行RAG
        if query_type:
            content = data['text']
            full_prompt = RAG_prompt.format(content,question)
            # full_prompt = f"{RAG_prompt} {question}"
            response = model.get_response(full_prompt,query_type=3) 
        else:
            prompt = question
            response = model.get_response(prompt,query_type=3)
        return jsonify({'answer':response}),200
    
@app.route('/get_new_dialog',method=['POST'])
def get_new_dialog():
    data = request.form
    dialog_id = data['dialog_id']
    user_id = data['user_id']
    model = GLM()
    glm_dict[user_id] = {}
    glm_dict[user_id][dialog_id] = model
    return jsonify(message=f"New dialog {dialog_id} created."),200

@app.route('/delete_dialog',method=['POST'])
def delete_dialog():
    data = request.form
    dialog_id = data['dialog_id']
    user_id = data['user_id']
    glm_dict[user_id][dialog_id].unload_model()
    del glm_dict[user_id][dialog_id]
    return jsonify(message=f"Dialog {dialog_id} deleted."),200

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')



