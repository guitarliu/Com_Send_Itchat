# coding: utf-8

import itchat, time
from itchat.content import *

newInstance = itchat.new_instance()
newInstance.auto_login(hotReload=True, enableCmdQR=True, statusStorageDir='newInstance.pkl')

@newInstance.msg_register(TEXT)
def reply(msg):
        print(msg.user['RemarkName'], ": ", msg.text)

newInstance.run()