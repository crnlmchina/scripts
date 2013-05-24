from pymongo import Connection
import re

#host = '172.16.1.50'
host = '127.0.0.1'
db = Connection(host).wendui

for topic in db.topic.find():
	add_parts = []
	qid = topic['_id']
	print qid
	top_q = db.question.find_one({'_id' : qid})
	if top_q.get('agree_user_ids'):
		add_parts += top_q.get('agree_user_ids')
	if top_q.get('disagree_user_ids'):
		add_parts += top_q.get('disagree_user_ids')
	for answer in db.answer.find({'question_id' : qid}):
		add_parts.append(answer['author_id'])
		if answer.get('agree_user_ids'):
			add_parts += answer.get('agree_user_ids')
		if answer.get('disagree_user_ids'):
			add_parts += answer.get('disagree_user_ids')

	subqids = db.question.find({'path' : re.compile(r'^%s.*$' % qid)}).distinct('_id')
	subqids.append(qid)
	for sub_q in db.ques_sub_info.find({'qid' : {'$in' : subqids}}):
		if sub_q.get('likers'):
			add_parts += sub_q.get('likers')
	if add_parts:
		print add_parts
		db.topic.update({'_id' : qid}, {'$addToSet' : {'statistics.participations' : {'$each' : add_parts}}})
