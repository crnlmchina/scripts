# -*- coding: utf-8 -*-
'''
Created on 2012-3-23

@author: wangyuxaun
'''

import xmpp

def get_conn():
    user='wend.spirit@gmail.com'
    password='wendui2011'
    server='gmail.com'
    jid = xmpp.JID(user)
    connection = xmpp.Client(server,debug=[])
    connection.connect(('talk.google.com',5222))
    connection.auth(jid.getNode(), password)
    return connection
