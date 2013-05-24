# -*- coding: utf-8 -*-
from pymongo import Connection

#host = '172.16.1.50'
host = '127.0.0.1'

def realPres(uid):
    db = Connection(host).wendui
    totalPres = 0
    for ques in db.question.find({'author_id':uid}):
        # 顶问题
        if ques.get('agree_user_size'):
            totalPres += ques.get('agree_user_size')
        # 踩问题
        if ques.get('disagree_user_size'):
            totalPres -= ques.get('disagree_user_size')
        # 问题被收藏
        totalPres += db.user_att_ques.find({'target_id' : ques['_id']}).count()

    for answ in db.answer.find({'author_id':uid}):
        # 顶回答
        if answ.get('agree_user_size'):
            totalPres += 2 * answ.get('agree_user_size')
        # 踩回答
        if answ.get('disagree_user_size'):
            totalPres -= 2 * answ.get('disagree_user_size')
        # 回答被采纳
        if answ.get('best'):
            totalPres += 3

    # 粉丝
    fans = db.user_att_user.find({'target_id':uid, 'relation':{'$in':['ATTENTION','FRIEND']}}).count()
    totalPres += fans

    # 纵咨询思路被喜欢
    for q_sub in db.ques_sub_info.find({'splitor_id':uid}):
        likers = q_sub.get('likers')
        if likers:
            totalPres += len(likers)*5

    # 纵咨询被收藏
    tids = db.topic.find({'statistics.consulant_team' : uid}).distinct('_id')
    if tids:
        totalPres += db.fav_topic.find({'tid' : {'$in' : tids}}).count()
    return totalPres

if __name__ == '__main__':
    print realPres('kdywvqtps')
