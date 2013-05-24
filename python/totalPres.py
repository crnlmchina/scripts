#-*- coding:utf-8 -*-

from pymongo import Connection

db = Connection().wendui
for item in db.monthly_prestige.find().sort('prestige', -1).limit(100):
	name = db.user.find_one({'_id':item['uid']})['name']
	print '%s : %d' % (name, item['prestige'])
