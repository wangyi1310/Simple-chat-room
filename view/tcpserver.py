#! /usr/bin/python
#coding:utf-8
import sys
import socket
from select import epoll
import select
import json
import cotroller
import s
sys.path.append("model")
Coller=cotroller.Collertor()
s.sock_dict={}
class TcpServer(object):
    def __init__(self,ip,port):
        """
        初始话socker 进行bind and listen
        """
        try:
            self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #开启端口复用
        except socket.error as e:
            print ((str(e)))
        self.sock.bind((ip,port)) #绑定ip和port
        self.sock.setblocking(0) #设置成非阻塞
        self.mlisten_fd=self.sock.fileno() #获取sock 对应的fd
        self.epoller=epoll()
        self.sock.listen(5)
        self.epoller.register(self.mlisten_fd,select.EPOLLIN)  #添加到epoll中


    def deal_accept(self,fileno):
        """
        处理accept事件
        :param fileno: listenfd
        :return: None
        """
        (client, address) = self.sock.accept()
        print ("new client connect server")
        client.setblocking(0)
        self.epoller.register(client.fileno(), select.EPOLLIN)
        s.sock_dict[client.fileno()]=client


    def parese_message(self,message):
        """
        解析出客户端发的消息。调用不同的方法进行处理
        :param message:
        :return: 返回消息的类型
        """
        try:
            temp_data=json.loads(message)
            return temp_data
        except:
            return False

    def deal_client_message(self,fileno):
        message=s.sock_dict[fileno].recv(1024)
        if len(message) != 0:
            message=self.parese_message(message)
            if not message:
                return
            #调用Coller的 方法去处理客户端发送过来的信息。
            message['clientfd'] =  fileno
            Coller.deal_message(message)

        else:
            #如果没有读到数据则说明客户端需要关闭删除epoll
            message = {'message_type':1,'clientfd':fileno,'data':{}}
            Coller.deal_message(message)
            self.close_client(fileno)


    def close_client(self,fileno):
        print ("a client close")
        self.epoller.unregister(fileno)
        s.sock_dict.pop(fileno)

    def run(self):
        while True:
            events = self.epoller.poll(-1)
            for fileno,event in events:
                if fileno==self.mlisten_fd:
                    self.deal_accept(fileno)
                else:
                    self.deal_client_message(fileno)


if __name__  == '__main__':
    tcpserver=TcpServer('127.0.0.1',3000)
    tcpserver.run()

