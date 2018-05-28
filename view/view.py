#coding:utf-8
'''
定义view父类，所有不同的模块都派生这个父类
'''
import sys
sys.path.append('../../Simple-chat-room')
import s
from model.model import Mongo
class View(object):
    def __init__(self):
        '''
        state 代表process执行成功没有
        '''
        self.mongo=Mongo()
        self.state=True
        self.clientfd=-1
        self.code=0


    def process(self,message):
        pass


    def response(self):
        pass


