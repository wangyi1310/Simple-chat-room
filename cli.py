#coding:utf-8
import socket               # 导入 socket 模块
import json

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口好

s.connect(("127.0.0.1", 3000))
data = dict()
data['message_type'] =0 
usr = dict()
usr['user_name'] = "test"
usr['password']  =1310874029
data['data'] =usr
data=json.dumps(data)
s.send(data)
print s.recv(1024)
data =dict()
data['message_type'] = 2
usr=dict()
usr['user_name'] = 'wang'
usr['to_user_name'] = 'test'
usr['mess'] = 'fsdfdsafdsf'
data['data'] = usr
data=json.dumps(data)
s.send(data)
print s.recv(1024)
s.close()  
