#coding:utf-8
import view
class ChatView(view.View):
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
	#获取自己的用户名
	self.clientfd=user_info['clientfd']
	results = self.mongo.find_user_state_clifd(self.clientfd)
	user_name=resluts[0]['user_name']
	send_data= message
	send_data['user_name'] = user_name
	#判断用户是否存在
	to_user_name = message['to_user_name']
	results=self.mongo.find_user_info(to_user_name)
	if len(resluts):
		#判断用户是否在线
		results = self.mongo.find_user_state_name(to_user_name)
		if len(resluts):
			to_user_fd = resluts[0]['clientfd']
			s.sock_dict[to_user_fd].send(message['data'])
			self.code = 0
		else:
			self.mongo.insert_delay_message(send_data)
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
