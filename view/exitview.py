#coding:utf-8
import view
class ExitView(view.View):
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
	self.clientfd=user_info['clientfd']
	results = self.mongo.find_user_info(self.clientfd)
	for item in results:
		if item['clientfd'] ==  self.clientfd:
			user_name=item['user_name']
			self.mongo.delete_user_state(user_name)
			self.state = True
			return 
	self.state = False
    def response(self):
        pass

