# coding: utf-8

import itchat, time, win32com
from itchat.content import *
from win32com.client import Dispatch

newInstance = itchat.new_instance()
newInstance.auto_login(hotReload=True, enableCmdQR=True, statusStorageDir='newInstance.pkl')
speaker = Dispatch("SAPI.SpVoice")


@newInstance.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def reply(msg):
        print(msg.user['RemarkName'], ":", msg.text)
        speaker.Speak("Message From" + msg.user['RemarkName'] + msg.text)

@newInstance.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    print(msg.user['RemarkName'], ":", 'Received %s, look on phone' % msg.fileName)
    if msg.fileName.split('.')[-1] != 'gif':
        msg.download(msg.fileName)

@newInstance.msg_register(TEXT, isGroupChat = True)
def text_reply(msg):
    print("[Group]", msg.user['NickName'], '-', msg.actualNickName, ":", msg.text)
    speaker.Speak("Message From Group" + msg.user['NickName'] + msg.actualNickName + msg.text)


newInstance.run()