import paramiko
from paramiko import SSHClient
import requests
import sshtunnel
from sshtunnel import SSHTunnelForwarder
import json

# SSH服务器详情
# SSH_ADDRESS = '106.120.183.117'
SSH_ADDRESS = '106.120.183.117'
SSH_USERNAME = 'root'
SSH_PASSWORD = ''  # 替换为你的SSH密码
# SSH_PORT = 29595  # SSH端口
SSH_PORT = 49487
LOCAL_PORT = 1145  # 本地机器上用于转发的端口
REMOTE_HOST = '127.0.0.1'  # 远程服务器上的服务地址（通常是127.0.0.1）
REMOTE_PORT = 5001  # 远程服务器上服务的端口

ssh_client = paramiko.SSHClient()
# 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接 ，此方法必须>放在connect方法的前面
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接SSH服务端，以用户名和密码进行认证 ，调用connect方法连接服务器
ssh_client.connect(hostname=SSH_ADDRESS, port=SSH_PORT, username=SSH_USERNAME, password=SSH_PASSWORD)
print("Yes!")


# 配置SSH隧道
with SSHTunnelForwarder(
    (SSH_ADDRESS, SSH_PORT),
    ssh_username=SSH_USERNAME,
    ssh_password=SSH_PASSWORD,
    remote_bind_address=(REMOTE_HOST, REMOTE_PORT),
    local_bind_address=('127.0.0.1', LOCAL_PORT)
) as tunnel:
    print(f'SSH tunnel established at localhost:{LOCAL_PORT}')
# 通过SSH隧道发送HTTP请求
    url = f"http://127.0.0.1:{LOCAL_PORT}/ask"
    data = {
        'user_id': '1',
        'num': 1,
        'classification': True,
        'keyword': False,
        'question': '南京药丸公司股东的主营业务和公司业务领域有何关联？',
        'query_type': True,
        'text':"'南京药丸公司股东的主营业务和公司业务领域有关联"
    }

    # 注意：根据你的实际请求类型（GET/POST）来选择合适的方法
    response = requests.get(url=url, params=data)  # 对于GET请求使用params参数
    # response = requests.post(url=url, json=data)  # 对于POST请求使用json参数
    response.encoding = 'gb2312'
    print(json.loads(response.text)['answer'])