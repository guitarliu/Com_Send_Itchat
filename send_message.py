# coding: utf-8

import itchat, sys

newInstance = itchat.new_instance()
newInstance.auto_login(hotReload=True, statusStorageDir='newInstance.pkl')

remarkname = sys.argv[1]

username = newInstance.search_friends(remarkname)[0]['UserName']

newInstance.send("%s" % " ".join(sys.argv[2:]), username)




    
