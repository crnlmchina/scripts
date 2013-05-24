from pymongo import Connection
from datetime import datetime

host = '127.0.0.1'
#host = '172.16.1.50'
db = Connection(host).wendui

now = datetime.now()

for item in db.op_user_group.find():
	for uid in item['ids']:
		user = db.user.find_one({'_id' : uid})
		if user:
			email = db.user.find_one({'_id' : uid}).get('email')
			inval_e = db.invalid_email.find_one({'_id' : email})
			if not inval_e:
				print email
				db.invalid_email.insert({'_id' : email, 'create_time': now})
