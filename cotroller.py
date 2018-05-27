#coding:utf-8
from view.chatview import ChatView
from view.exitview import ExitView
from view.broadcastview import  BroadCastView
from view.registerveiw import RegisterView
from view.loginview import LoginView
import event
class Collertor(object):
    def __init__(self):
        self.views=dict()
        self.views[event.CHAT] =ChatView()
        self.views[event.LOGIN] =LoginView()
        self.views[event.EXIT] =ExitView()
        self.views[event.BROADCAST] =BroadCastView()
        self.views[event.REGISTER] =RegisterView()
    def deal_message(self,message):
        """
        :param message:
        调用不同的view 处理不同的消息
        :return:
        """
        str_tmp = dict()
        message_type=message['message_type']
        str_tmp=message['data']
        str_tmp['clientfd'] = message['clientfd']
        if message_type >-1 and message_type <len(self.views):
            self.views[message_type].process(str_tmp)
            self.views[message_type].response()

    def regisetr(self,message_type,view):
        if message_type >len(self.views):
            self.views[message_type] =view


