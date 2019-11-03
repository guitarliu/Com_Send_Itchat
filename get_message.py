# coding: utf-8

import itchat, time, win32com
from itchat.content import *
from win32com.client import Dispatch

newInstance = itchat.new_instance()
newInstance.auto_login(hotReload=True, enableCmdQR=True, statusStorageDir='newInstance.pkl')
speaker = Dispatch("SAPI.SpVoice")


@newInstance.msg_register(TEXT)
def reply(msg):
        print(msg.user['RemarkName'], ": ", msg.text)
        speaker.Speak("Message From" + msg.user['RemarkName'] + msg.text)
        
newInstance.run()