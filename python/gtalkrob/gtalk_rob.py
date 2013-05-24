# -*- coding:utf-8 -*-
'''
Created on 2012-3-23

@author: wangyuxaun
'''

import xmpp
import time
import messagebox
import sys

contacts = [
    'pany2peggy@gmail.com',
    'crnlmcn@gmail.com',
    'yongkaixie@gmail.com',
    'kratos00000@gmail.com',
    'kengcheng.wu@gmail.com',
    'linlanlan888@gmail.com',
    'ireneng666@gmail.com',
    'joyce.yang611@gmail.com'
]

import gtalk_conn

def startMoniter():
    connection = gtalk_conn.get_conn()
    while True:
        try:
            if not connection.isConnected():
                connection.reconnectAndReauth()
            messages = messagebox.findMessages()
            for msg in messages:
                for contact in contacts:
                    try:
                        connection.SendAndWaitForResponse(xmpp.Message(contact, msg + u'\n\n*_*'), timeout=1)
                    except:
                        print sys.exc_info()
        except:
            print sys.exc_info()
        try:
            connection.Process(1)
        except:
            print sys.exc_info()
        time.sleep(10)
    
if __name__ == '__main__':
    startMoniter()

