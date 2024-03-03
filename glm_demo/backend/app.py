from flask import Flask,render_template,request,jsonify
import demo_code
from Chatwhale.glm_demo.demo_code.GLM_set_up import GLM
import requests
from chroma_db import get_query

glm_list = []
app=Flask(__name__)
#大模型所在服务器ip地址
url = 'http://ip'

@app.route('/')
def index():
    return render_template("template.html")
@app.route('/api/ocr',methods=['POST'])
def handle_ocr():
    # if request.method == 'POST';
    pdf = request.files['pdf']
    return jsonify(message="PDF processed successfully."),200

#用户问问题，post到大模型所在服务器进行分析，预计需要一定响应时间
@app.route('/api/chat<string:user_id>/ask<int:dialog_id>',methods=['GET'])
def get_question(user_id,dialog_id):
    data_ = request.form
    question = data_['question']
    data = {
        'num':dialog_id,
        'question':question,
        'user_id':user_id,
        'classification':True,
        'query_type':True
    }
    try:
        response = requests.get(url=url+'/ask',data=data)
        if response['classification'] == 'D' or response['classification'] == 'E':
            result = get_query(query=question)
            data = {
                    'num':dialog_id,
                    'question':question,
                    'text':result,
                    'user_id':user_id,
                    'classification':False,#表示问题是否参与分类
                    'query_type':True #表示prompt中是否加入提示
            }
            try:
                response2 = requests.get(url=url+'/ask',data=data)
                return jsonify(
                    {
                        'status':'success',
                        'answer':response2['answer']
                    }
                ),200
            except:
                return jsonify({
                'status':'error',
                'answer':None
            }),201
        else:
            return jsonify(
                    {
                        'status':'success',
                        'answer':response2['answer']
                    }
                ),200
    except:
    # return jsonify(answer=f"Answer to '{question}'.")
        return jsonify({
                'status':'error',
                'answer':None
            }),201

#创建新的对话窗口
@app.route('/api/glm<string:user_id>/<int:dialog_id>',method=['POST'])
def create_new_window(user_id,dialog_id):
    # glm = GLM()
    # model = glm.model
    # glm_list.appned(model)
    if dialog_id > 5:
        return jsonify(message=f"Dialogs have reached maximum."),201
    try:
        response = requests.post(url=url+'/get_new_dialog',data={'num':dialog_id,'user':user_id})
        return jsonify(message=f"New dialog {dialog_id} created."),200
    except:
        return jsonify(message=f"New dialog {dialog_id} creation failed."),201
    
#对话框删除
@app.route('/api/glm<string:user_id>/<int:dialog_id>',method=['POST'])
def delete_window(user_id,dialog_id):
    try:
        response = requests.post(url=url+'/delete_dialog',data={'num':dialog_id,'user':user_id})
        return jsonify(message=f"Dialog {dialog_id} deleted."),200
    except:
        return jsonify(message=f"Dialog {dialog_id} deletion failed."),201

#反馈接口
@app.route('/api/chat/feedback',method=['POST'])
def feedback():
    return jsonify(message='message received!'),200

#重新生成回复接口
@app.route('/api/chat<string:user_id>/regenerate<int:dialog_id>',method=['GET'])
def regenerate(user_id,dialog_id):
    question = "问题有所偏差，请重新生成答案"
    data = {
        'num':dialog_id,
        'question':question,
        'user_id':user_id,
        'classification':False,
        'query_type':False
    }
    try:
        response = requests.get(url=url+'/ask',data=data)
        return jsonify({
                'status':'success',
                'new_answer':response['answer']
            }),200
    except:
        return jsonify({
                'status':'error',
                'new_answer':None
            }),201

#主题提取接口
@app.route('/api/chat<string:user_id>/topic<int:dialog_id>',method=['GET'])
def topic(user_id,dialog_id):
    question = "请对刚刚提出的问题作出总结"
    data = {
        'num':dialog_id,
        'question':question,
        'user_id':user_id,
        'classification':False,
        'query_type': False
    }
    try:
        response = requests.get(url=url+'/ask',data=data)
        return jsonify({
                'status':'success',
                'new_answer':response['answer']
            }),200
    except:
        return jsonify({
                'status':'error',
                'new_answer':None
            }),201
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
