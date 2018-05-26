#coding:utf-8
import view
class RegisterView(view.View):
    def __init__(self):
        '''
        连接数据库
        '''
        super().__init__()
    def process(self,message):
        """
        对于客户端发送过来的数据进行处理
        :param message:
        :return:
        """
		user_name=message['user_name']
		resluts = self.mongo.find_user_info(user_name)
		self.clientfd=message['clientfd']
		if len(resluts):
			self.code = 2
			self.state = True
			return 
		self.mongo.insert_user_info(message)
		self.code = 0
		self.state = True
		
    def response(self):
        if self.state:
			message = "REGISTER  SUCCESS"
		else:
			message = "REGISTER FAILUER"
		data={'code',self.code,'message':message}
		data=json.dumps(data)
		s.sock_dict[self.clientfd].send(data)