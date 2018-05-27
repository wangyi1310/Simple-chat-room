#coding:utf-8
import view
class ExitView(view.View):
    def __init__(self):
        '''
        连接数据库
        '''
        super(ExitView,self).__init__()
    def process(self,message):
        """
        对于客户端发送过来的数据进行处理
        :param message:
        :return:
        """
        self.clientfd=message['clientfd'] 
        self.mongo.delete_user_state_clifd(self.clientfd)
        self.state = True


        def response(self):
            pass

