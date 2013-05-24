# -*- coding: utf-8 -*-
'''
Created on 2012-3-22

@author: wangyuxaun
'''
from pymongo import Connection
from datetime import datetime,timedelta
        
host = '127.0.0.1'
db_name = 'wendui'
        
def findMessages():
    conn = Connection(host)
    db = conn[db_name]
    msgs = []
    if True:
        msgs
    curr_time = datetime.utcnow() - timedelta(seconds=20)
    print curr_time
    for q in db.question.find({'create_time' : {'$gt' : curr_time}, 'checked' : {'$ne' : True}}):
        db.question.update({'_id' : q['_id']}, {'$set' : {'checked' : True}})
        author = db.user.find_one({'_id' : q['author_id']})['name']
        msgs.append(u'[提问] [%s]: %s \n[描述]: %s \n[链接]: http://www.wendui.com/qs/%s\n' % (author, q['content'], q.get('desc',''), q['_id']))
    for answer in db.answer.find({'create_time' : {'$gt' : curr_time}, 'checked' : {'$ne' : True}}):
        db.answer.update({'_id' : answer['_id']}, {'$set' : {'checked' : True}})
        author = db.user.find_one({'_id' : answer['author_id']})['name']
        msgs.append(u'[回答] [%s]: %s \n[链接]: http://www.wendui.com/qs/%s/%s\n' % (author, answer['content'], answer['question_id'], answer['_id']))
    for comment in db.comment.find({'create_time' : {'$gt' : curr_time}, 'checked' : {'$ne' : True}}):
        db.comment.update({'_id' : comment['_id']}, {'$set' : {'checked' : True}})
        author = db.user.find_one({'_id' : comment['author_id']})['name']
        answer = db.answer.find_one({'_id' : comment['answer_id']})
        msgs.append(u'[评论] [%s]: %s \n[链接]: http://www.wendui.com/qs/%s/%s/%s\n' % (author, comment['content'], answer['question_id'], answer['_id'], comment['_id']))
    conn.close()
    return msgs
