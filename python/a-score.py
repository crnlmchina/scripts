# -*- coding: UTF8 -*-
from pymongo import Connection
import random

my_gid = 'pvpjqqrlk'

host = '127.0.0.1'
#host = '172.16.1.50'

db = Connection(host).wendui

query = {'author_group_id': {'$ne': my_gid}, 'scorer': {'$ne': my_gid}}
cursor = db.ques_score.find(query)

print '%d questions to score' % cursor.count()

choices = [6, 8, 10]

for q in cursor:
	score = random.choice(choices)
	qid = q['_id']
	print qid, score
	db.ques_score.update({'_id': qid}, {'$addToSet': {'scorer': my_gid}, '$inc': {'score': score}})
