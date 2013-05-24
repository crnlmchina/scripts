# -*- coding: UTF-8 -*-
from pymongo import Connection

#host = '172.16.1.50'
host = '127.0.0.1'

db = Connection(host).wendui

def main():
	for ua in db.user_att_user.find():
		if ua['user_id'] == ua['target_id']:
			uid = ua['user_id']
			user = db.user.find_one({'_id': uid})
			print user['name']
			db.user_att_user.remove({'_id': ua['_id']})

if __name__ == '__main__':
	main()
