import requests
url = "http://127.0.0.1:8900"
response = requests.get(url=url)
# import paramiko
# from paramiko import SSHClient
# import requests
# import sshtunnel
# from sshtunnel import SSHTunnelForwarder
# SSH_ADDRESS = '106.54.38.134'
# SSH_USERNAME = 'ubuntu'
# SSH_PASSWORD = 'CitiGroup@<2024>'  # 替换为你的SSH密码
# # SSH_PORT = 29595  # SSH端口
# SSH_PORT = 19530
# LOCAL_PORT = 1145  # 本地机器上用于转发的端口
# REMOTE_HOST = '127.0.0.1'  # 远程服务器上的服务地址（通常是127.0.0.1）
# REMOTE_PORT = 5001  # 远程服务器上服务的端口

# ssh_client = paramiko.SSHClient()   
# # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接 ，此方法必须放在connect方法的前面
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
# # 连接SSH服务端，以用户名和密码进行认证 ，调用connect方法连接服务器
# ssh_client.connect(hostname=SSH_ADDRESS, port=SSH_PORT, username=SSH_USERNAME, password=SSH_PASSWORD)
# print("Yes!")
# user_id = "3"
# dialog_id = 1
# len = 0
# with SSHTunnelForwarder(
#                     (SSH_ADDRESS, SSH_PORT),
#                     ssh_username=SSH_USERNAME,
#                     ssh_password=SSH_PASSWORD,
#                     remote_bind_address=(REMOTE_HOST, REMOTE_PORT),
#                     local_bind_address=('127.0.0.1', LOCAL_PORT)
#                 ) as tunnel:
#                 # url = f"http://106.54.38.134:5001/glm{user_id}/{dialog_id}/{len}"
#                 url = f"http://127.0.0.1:{LOCAL_PORT}/glm{user_id}/{dialog_id}/{len}"
#                 response = requests.post(url=url)