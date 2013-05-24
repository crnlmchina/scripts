# -*- coding:utf-8 -*-
'''
Created on 2012-3-23

@author: wangyuxaun
'''

import xmpp
import cnstr
import mencode
import sys
from datetime import datetime

commands = {
    'help' : '帮助',
    'who' : '查看用户信息'
}

u_categories = {
    'A' : u'浏览用户',
    'B' : u'浅度用户',
    'C' : u'深度用户',
    'XA' : u'流失浏览用户',
    'XB' : u'流失浅度用户',
    'XC' : u'流失深度用户'
}

from pymongo import Connection

host = '127.0.0.1'
#host = '172.16.1.50'
db_name = 'wendui'

def get_user_info(id_or_name):
    db = Connection(host)[db_name]
    users = []
    for user in db.user.find({'status' : 'ACTIVATED', '$or' : [{'_id' : id_or_name}, {'name' : id_or_name}]}):
        uid = user['_id']
        groups = []
        for user_group in db.op_user_group.find({'ids' : user['_id']}):
            groups.append(user_group['name'])
        industry = u''
        domain = u''
        leave_days = 0
        pres_inc = 0
        user_category = u_categories.get(user.get('category',u''),u'')
        industry_id = user.get('industry')
        if industry_id:
            industry = db.industry.find_one({'_id':industry_id})['name']
        domain_id = user.get('domain')
        if domain_id:
            domain = db.domain.find_one({'_id':domain_id})['name']
        curr_time = datetime.now()
        user_pres = db.monthly_prestige.find_one({'uid':uid})
        if user_pres:
            pres_inc = user_pres['prestige']
        for item in db.user_action.find({'user_id':uid}).sort('time', -1).limit(1):
            r_time = item['time']
            leave_days = (datetime.utcnow() - r_time).days
        users.append(u'用户id：%s\n用户姓名：%s\n注册时间：%s\n所属用户组：%s\n行业：%s\n职能：%s\n几天没来了: %d\n本月威望增长值：%d\n用户类型：%s\n' % \
            (user.get('_id'), user.get('name'), user.get('register_time').strftime('%Y-%m-%d %H-%M-%S'), cnstr.cn_str_list(groups).decode('utf-8'), industry, domain, leave_days, pres_inc, user_category))
    return users

def message_handler(connect_object, message_node):
    return_msg = u'小小姑娘，清早起床，提着裤子上茅房...\n输入help获得命令集'
    income = message_node.getBody()
    address = message_node.getFrom()
    #print u'From: %s, content: %s' % (address, income)
    fregs = income.split(' ', 1)
    comm = fregs[0]
    if commands.has_key(comm):
        if u'help' == comm:
            return_msg = cnstr.cn_str_dict(commands).decode('utf-8')
        elif u'who' == comm:
            if len(fregs) == 1:
                return_msg = u'你需要输入用户姓名或id，格式：who 王宇轩, (不要习惯性得在后面加上帅哥两个字)'
            else:
                return_msg = cnstr.cn_str_list(get_user_info(fregs[1]))
    #print u'Reply: %s' % return_msg
    connect_object.SendAndWaitForResponse(xmpp.Message(address, return_msg), timeout=1)
    
import gtalk_conn
    
def start_reciever():
    connection = gtalk_conn.get_conn()
    connection.RegisterHandler('message', message_handler)
    connection.sendInitPresence()
    while True:
        try:
            connection.Process(1)
        except:
            pass
            #print sys.exc_info()
        
if __name__ == '__main__':
    start_reciever()
    #print cnstr.cn_str_list(get_user_info(u'李敏'))

