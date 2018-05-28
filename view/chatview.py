#coding:utf-8
import view
import s
import json
class ChatView(view.View):
    def __init__(self):
        '''
        连接数据库
        '''
        super(ChatView,self).__init__()


    def process(self,message):
        """
        对于客户端发送过来的数据进行处理
        :param message:
        :return:
        """
		#获取自己的用户名
        self.clientfd=message['clientfd']
        resluts=self.mongo.find_user_state_clifd(self.clientfd)
        message.pop('clientfd')
        user_name=resluts[0]["user_name"]
		#判断用户是否存在
        to_user_name = message['to_user_name']
        results=self.mongo.find_user_info(to_user_name)
        if results.count():
			#判断用户是否在线
            result = self.mongo.find_user_state_name(to_user_name) 
            if result.count():
                to_user_fd = result[0]['clientfd']
                s.sock_dict[to_user_fd].send(message['mess'])
                self.code = 0
            else:
                print message
                self.mongo.insert_delay_message(message)
                self.code = 1
            self.state = True
            return
        self.code = 2
        self.state = False



    def response(self):
        message = str()
        if self.state:
            message = "CHAT SEND SUCCESS"
        else:
            message = "CHAT SEND FAILUER "
        response_info={'code':self.code,'message':message}
        data=json.dumps(response_info)
        s.sock_dict[self.clientfd].send(data)
