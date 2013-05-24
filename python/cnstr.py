# -*- coding:utf-8 -*-
'''
Created on 2012-3-23

@author: wangyuxaun
'''

def cn_str_list(slist):
    cn_str = '['
    for item in slist:
        cn_str += '%s, ' % item
    cn_str = cn_str[:len(cn_str) - 2]
    cn_str += ']'
    return cn_str

def cn_str_dict(sdict):
    cn_str = '{'
    for key in sdict.keys():
        cn_str += '%s : %s, ' % (key, sdict.get(key))
    cn_str = cn_str[:len(cn_str) - 2]
    cn_str += '}'
    return cn_str

    
if __name__ == '__main__':
    mylist = ['中国', '人民']
    mydict = {'a' : '王宇轩', '国家': '地方'}
    print cn_str_list(mylist)
    print cn_str_dict(mydict)
