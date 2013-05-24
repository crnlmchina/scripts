from pymongo import Connection
from datetime import datetime

host = '127.0.0.1'
#host = '172.16.1.50'
db = Connection(host).wendui

now = datetime.now()
start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

print start, now

for user in db.user.find({'create_time': {'$gte': start, '$lt': now}}):
	print user['_id'], user['name'], user['email'], user['status']
