from flask import Flask,render_template,request,jsonify
from flask_cors import CORS
import json
# import demo_code
# from Chatwhale.glm_demo.demo_code.GLM_set_up import GLM
import requests
# from chroma_db import get_query
import paramiko
from paramiko import SSHClient
import requests
import sshtunnel
from sshtunnel import SSHTunnelForwarder

# SSH服务器详情
SSH_ADDRESS = '106.120.183.117'
SSH_USERNAME = 'root'
SSH_PASSWORD = ''  # 替换为你的SSH密码
SSH_PORT = 29595  # SSH端口
# SSH_PORT = 49487
LOCAL_PORT = 1145  # 本地机器上用于转发的端口
REMOTE_HOST = '127.0.0.1'  # 远程服务器上的服务地址（通常是127.0.0.1）
REMOTE_PORT = 5001  # 远程服务器上服务的端口

ssh_client = paramiko.SSHClient()   
# 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接 ，此方法必须放在connect方法的前面
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
# 连接SSH服务端，以用户名和密码进行认证 ，调用connect方法连接服务器
ssh_client.connect(hostname=SSH_ADDRESS, port=SSH_PORT, username=SSH_USERNAME, password=SSH_PASSWORD)
print("Yes!")

glm_list = []
app=Flask(__name__)
CORS(app)
#大模型所在服务器ip地址
url = f"http://127.0.0.1:{LOCAL_PORT}"

@app.route('/')
def index():
    return "Hello World!"
    # return render_template("template.html")
@app.route('/api/ocr',methods=['POST'])
def handle_ocr():
    # if request.method == 'POST';
    pdf = request.files['pdf']
    return jsonify(message="PDF processed successfully."),200

#用户问问题，post到大模型所在服务器进行分析，预计需要一定响应时间
@app.route('/api/chat/<string:user_id>/ask<int:dialog_id>',methods=['POST'])
def get_question(user_id,dialog_id):
    # return "Hello World!"
    # data_ = request.form
    question = request.args.get('question')
    print(question)
    print(user_id)
    print(dialog_id)
    data = {
        'num':dialog_id,
        'question':question,
        'user_id':user_id,
        'classification':True,
        'keyword':False,
        'query_type':True,
        'text':None
    }
    try:
        with SSHTunnelForwarder(
                    (SSH_ADDRESS, SSH_PORT),
                    ssh_username=SSH_USERNAME,
                    ssh_password=SSH_PASSWORD,
                    remote_bind_address=(REMOTE_HOST, REMOTE_PORT),
                    local_bind_address=('127.0.0.1', LOCAL_PORT)
                ) as tunnel:
                    print(f'SSH tunnel established at localhost:{LOCAL_PORT}')
                    response = requests.get(url=url+'/ask',params=data)
                    if response.status_code!=200:
                         return jsonify({
                            'status':'error',
                            'answer':None
                        }),201
                    response = json.loads(response.text)
                    print(response)
        if response['classification'] == 'D' or response['classification'] == 'E':
            result = get_query(query=question)
            data = {
                    'num':dialog_id,
                    'question':question,
                    'text':result,
                    'user_id':user_id,
                    'keyword':False,
                    'classification':False,#表示问题是否参与分类
                    'query_type':True #表示prompt中是否加入提示
            }
            try:
                with SSHTunnelForwarder(
                    (SSH_ADDRESS, SSH_PORT),
                    ssh_username=SSH_USERNAME,
                    ssh_password=SSH_PASSWORD,
                    remote_bind_address=(REMOTE_HOST, REMOTE_PORT),
                    local_bind_address=('127.0.0.1', LOCAL_PORT)
                ) as tunnel:
                    print(f'SSH tunnel established at localhost:{LOCAL_PORT}')
                    response2 = requests.get(url=url+'/ask',params=data)
                    if response2.status_code==200:
                        response2 = json.loads(response2.text)
                        # if response2.status_code==
                        print(response2['answer'])
                        return jsonify(
                            {
                                'status':'success',
                                'answer':response2['answer']
                            }
                        ),200
                    else:
                         return jsonify({
                                'status':'error',
                                'answer':None
                            }),201
            except:
                return jsonify({
                'status':'error',
                'answer':None
            }),201
        else:
            return jsonify(
                    {
                        'status':'success',
                        'answer':response['answer']
                    }
                ),200
    except:
    # return jsonify(answer=f"Answer to '{question}'.")
        return jsonify({
                'status':'error',
                'answer':None
            }),201

#创建新的对话窗口
@app.route('/api/add/glm/<string:user_id>/<int:dialog_id>/<int:len>',methods=['POST'])
def create_new_window(user_id,dialog_id,len):
    # glm = GLM()
    # model = glm.model
    # glm_list.appned(model)
    # return "Hello World!"
    if len > 5:
        return jsonify(message=f"Dialogs have reached maximum."),201
    try:
        with SSHTunnelForwarder(
                    (SSH_ADDRESS, SSH_PORT),
                    ssh_username=SSH_USERNAME,
                    ssh_password=SSH_PASSWORD,
                    remote_bind_address=(REMOTE_HOST, REMOTE_PORT),
                    local_bind_address=('127.0.0.1', LOCAL_PORT)
                ) as tunnel:
                    print(f'SSH tunnel established at localhost:{LOCAL_PORT}')
                    response = requests.post(url=url+'/get_new_dialog',params={'num':dialog_id,'user_id':user_id})
                    if response.status_code==200:
                        return jsonify(message=f"New dialog {dialog_id} created."),200
                    else:
                         return jsonify(message=f"New dialog {dialog_id} creation failed."),201
    except:
        return jsonify(message=f"New dialog {dialog_id} creation failed."),201
    
#对话框删除
@app.route('/api/delete/glm/<string:user_id>/<int:dialog_id>',methods=['POST'])
def delete_window(user_id,dialog_id):
    try:
        with SSHTunnelForwarder(
                    (SSH_ADDRESS, SSH_PORT),
                    ssh_username=SSH_USERNAME,
                    ssh_password=SSH_PASSWORD,
                    remote_bind_address=(REMOTE_HOST, REMOTE_PORT),
                    local_bind_address=('127.0.0.1', LOCAL_PORT)
                ) as tunnel:
                    print(f'SSH tunnel established at localhost:{LOCAL_PORT}')
                    response = requests.post(url=url+'/delete_dialog',params={'num':dialog_id,'user_id':user_id})
                    if response.status_code==200:
                        return jsonify(message=f"Dialog {dialog_id} deleted."),200
                    else:
                         return jsonify(message=f"Dialog {dialog_id} deletion failed."),201
    except:
        return jsonify(message=f"Dialog {dialog_id} deletion failed."),201

#删除所有对话框
@app.route('/api/delete_all/glm/<string:user_id>',methods=['POST'])
def delete_all_window(user_id):
    try:
        with SSHTunnelForwarder(
                    (SSH_ADDRESS, SSH_PORT),
                    ssh_username=SSH_USERNAME,
                    ssh_password=SSH_PASSWORD,
                    remote_bind_address=(REMOTE_HOST, REMOTE_PORT),
                    local_bind_address=('127.0.0.1', LOCAL_PORT)
                ) as tunnel:
                    print(f'SSH tunnel established at localhost:{LOCAL_PORT}')
                    response = requests.post(url=url+'/delete_all_dialogs',params={'user_id':user_id})
                    if response.status_code==200:
                        return jsonify(message=f"User {user_id} dialogs deleted."),200
                    else:
                         return jsonify(message=f"User {user_id} dialogs deletion failed."),201
    except:
        return jsonify(message=f"User {user_id} dialogs deletion failed."),201

#反馈接口
@app.route('/api/chat/feedback',methods=['POST'])
def feedback():
    return jsonify(message='message received!'),200

#重新生成回复接口
@app.route('/api/chat/<string:user_id>/regenerate<int:dialog_id>',methods=['GET'])
def regenerate(user_id,dialog_id):
    question = request.args.get('question')
    question = f"问题{question}答案有所偏差，请重新生成答案"
    data = {
        'num':dialog_id,
        'question':question,
        'user_id':user_id,
        'classification':True,
        'keyword':False,
        'query_type':False,
        'text':None
    }
    try:
        with SSHTunnelForwarder(
                    (SSH_ADDRESS, SSH_PORT),
                    ssh_username=SSH_USERNAME,
                    ssh_password=SSH_PASSWORD,
                    remote_bind_address=(REMOTE_HOST, REMOTE_PORT),
                    local_bind_address=('127.0.0.1', LOCAL_PORT)
                ) as tunnel:
                    print(f'SSH tunnel established at localhost:{LOCAL_PORT}')
                    response = requests.get(url=url+'/ask',params=data)
                    response = json.loads(response.text)
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
@app.route('/api/chat/<string:user_id>/topic<int:dialog_id>',methods=['GET'])
def topic(user_id,dialog_id):
    question = request.args.get('question')
    question = f"刚刚的问题是{question},请概括刚刚的问题,并限制在七个汉字以内"
    data = {
        'num':dialog_id,
        'question':question,
        'user_id':user_id,
        'classification':False,
        'keyword':False,
        'query_type': False,
        'text':None
    }
    try:
        with SSHTunnelForwarder(
                    (SSH_ADDRESS, SSH_PORT),
                    ssh_username=SSH_USERNAME,
                    ssh_password=SSH_PASSWORD,
                    remote_bind_address=(REMOTE_HOST, REMOTE_PORT),
                    local_bind_address=('127.0.0.1', LOCAL_PORT)
                ) as tunnel:
                    print(f'SSH tunnel established at localhost:{LOCAL_PORT}')
                    response = requests.get(url=url+'/ask',params=data)
                    response = json.loads(response.text)
                    print(response['answer'])
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
    app.run(debug=True,host='0.0.0.0',port=8900)
