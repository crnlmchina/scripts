from pymongo import Connection

#host = '172.16.1.50'
host = '127.0.0.1'
db = Connection(host).wendui

for user in db.user.find({'name' : {'$exists' : True}}):
	db.user.update({'_id' : user['_id']}, {'$addToSet' : {'pinyin_name' : user.get('name').lower()}})
