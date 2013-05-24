from pymongo import Connection

host = '127.0.0.1'
#host = '172.16.1.50'
db = Connection(host).wendui

for topic in db.topic.find():
	print topic['_id']
	statistics = topic.get('statistics')
	if statistics:
		pc = statistics.get('participation_count', 0)
		statistics['participation_count'] = int(pc)
		suba = statistics.get('sub_a_count', 0)
		statistics['sub_a_count'] = int(suba)
		subq = statistics.get('sub_q_count', 0)
		statistics['sub_q_count'] = int(subq)
		vc = statistics.get('view_count', 0)
		statistics['view_count'] = int(vc)

		db.topic.update({'_id': topic['_id']}, {'$set': {'statistics': statistics}})
