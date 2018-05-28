#coding:utf-8
import view
import sys
import json
import s
class LoginView(view.View):
    def __init__(self):
        '''
        连接数据库
        '''
        super(LoginView,self).__init__()
        self.delay_message=list()


    def process(self,message):
        """
        对于客户端发送过来的数据进行处理
        :param message: client sock  client data
        :return: None
        """
        user_info=message
        self.clientfd=user_info['clientfd']
        resluts=self.mongo.find_user_info(user_info['user_name'])
        if resluts.count():
            if resluts[0]['password'] == user_info['password']:
                self.code = 0
                self.state = True
                self.mongo.insert_user_state(user_info['user_name'],user_info['clientfd'])
                results=self.mongo.find_delay_message(user_info['user_name'])
                if results.count():
                    for item in results:
                        item.pop('_id')
                        item.pop('to_user_name')
                        self.delay_message.append(item) 
                    self.mongo.delete_delay_message(user_info['user_name'])
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
        repsonse_info['delay_message'] =self.delay_message
        print repsonse_info
        data=json.dumps(repsonse_info)
        s.sock_dict[self.clientfd].send(data)

