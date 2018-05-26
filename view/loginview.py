#coding:utf-8
import view
import sys
import json
class LoginView(view.View):
    def __init__(self):
        '''
        连接数据库
        '''
        super().__init__()


    def process(self,message):
        """
        对于客户端发送过来的数据进行处理
        :param message: client sock  client data
        :return: None
        """
        user_info=message
        self.clientfd=user_info['clientfd']
        user_data=self.mongo.find_user_info(user_info['username'])
        for item in user_data:
            if item['password'] == user_info['passowrd']:
                self.code = 0
                self.state = True
                self.mongo.insert_user_state(user_info['name'],user_info['clientfd'])
                return
            else:
                self.code=1
                self.state  = False
                return
        self.code = 2
        self.state = False


    def response(self):
        """
        根据不同的状态给客户端回复不同的信息
        """
        message=str()
        if self.state:
            message = "LOGIN SUCCESS"
        else:
            message =  "LOGIN FAILUER"
        repsonse_info = {'code':self.code,'message':message}
        data=json.dumps(repsonse_info)
        s.sock_dict[self.clientfd].send(data)

