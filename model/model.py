#coding:utf-8
import pymongo
class Mongo:
    def __init__(self):
        self.mongo=self.connect()
        if not self.mongo:
            exit(0)


    def connect(self):
        try:
            mongoclient = pymongo.MongoClient('127.0.0.1',27017)
            return mongoclient
        except Exception as e:
            print(str(e))
            return False


    def find_user_state_name(self,user_name):
        db=self.mongo['ts']
        coll=db['user_state']
        resluts =coll.find({'user_name':user_name})
        return resluts


    def find_user_state_clifd(self,clifd):
        db=self.mongo['ts']
        coll=db['user_state']
        resluts =coll.find({'clientfd':clifd})
        return resluts


    def find_delay_message(self,user_name):
        db = self.mongo['ts']
        coll = db['delay_message']
        results = coll.find({'to_user_name': user_name})
        return results


    def insert_delay_message(self,message):
        db=self.mongo['ts']
        coll = db['delay_message']
        try:
            coll.insert(message)
            return True
        except:
            return False


    def delete_delay_message(self,user_name):
        db=self.mongo['ts']
        coll=db['delay_message']
        coll.remove({'to_user_name':user_name})

    def find_user_info(self,user_name):
        db=self.mongo['ts']
        coll=db['user_info']
        results=coll.find({'user_name':user_name})
        return results


    def insert_user_state(self,user_name,clientfd):
        db=self.mongo['ts']
        coll=db['user_state']
        try:
            coll.insert({'user_name':user_name,'clientfd':clientfd})
        except:
            print ("insert  user_state error")

    def insert_user_info(self,user_info):
        db=self.mongo['ts']
        coll=db['user_info']
        try:
            coll.insert(user_info)
        except:
            print ("insert user_info failuer")


    def delete_user_state_name(self,user_name):
        db=self.mongo['ts']
        coll=db['user_state']
        coll.remove({'user_name',user_name})


    def delete_user_state_clifd(self,clifd):
        db=self.mongo['ts']
        coll=db['user_state']
        coll.remove({'clientfd':clifd})
