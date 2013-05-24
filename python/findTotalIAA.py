from pymongo import Connection

#host = '172.16.1.50'
host = '127.0.0.1'

db = Connection(host).wendui

for user in db.user.find({'status':'ACTIVATED'}):
	uInterests = user.get('interests')
	if uInterests:
		total = 0
		for value in uInterests.values():
			total += value
		if total > 200:
			print '%s %s: %d' % (user['_id'], user['name'], total)
