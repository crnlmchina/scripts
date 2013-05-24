from pymongo import Connection

#host = '172.16.1.50'
host = '127.0.0.1'
db = Connection(host).wendui

for user in db.user.find():
	uid = user['_id']
	if user.get('has_authed_face'):
		db.user.update({'_id' : uid}, {'$inc' : {'prestige' : 10}})
	if db.question.find_one({'author_id':uid}):
		db.user.update({'_id' : uid}, {'$inc' : {'prestige' : 10}})
	if db.answer.find_one({'author_id':uid}):
		db.user.update({'_id' : uid}, {'$inc' : {'prestige' : 10}})
