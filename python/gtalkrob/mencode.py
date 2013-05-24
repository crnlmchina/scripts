# -*- coding:utf-8 -*-
'''
Created on 2012-3-23

@author: wangyuxaun
'''
def toutf8(text):
    if type(text) == type(u''):
        return text.encode('UTF-8')
    return str(text)
