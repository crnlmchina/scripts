# -*- coding: UTF-8 -*-
from pymongo import Connection
from collections import Counter
import re

host = '127.0.0.1'
db = Connection(host).wendui

career_id = 'vmlrykwrbk'

# 衰减职场兴趣
#for career_label in db.label.find({'paths' : re.compile(r'^' + career_id)}):
#	print career_label
#	label_id = career_label.get('_id')
#	for user in db.user.find({'interests.' + label_id : {'$exists' : True}}, {'name' : 1, 'interests' : 1}):
#		curr_val = user.get('interests').get(label_id)
#		print 'Deal user interests: %s, label boost: %f' % (user.get('name'), curr_val)
#		db.user.update({'_id' : user.get('_id')}, {'$set' : {'interests.' + label_id : curr_val / 4}})
#	for user in db.user.find({'abilities.' + label_id : {'$exists' : True}}, {'name' : 1, 'abilities' : 1}):
#		curr_val = user.get('abilities').get(label_id)
#		print 'Deal user abilities: %s, label boost: %f' % (user.get('name'), curr_val)
#		db.user.update({'_id' : user.get('_id')}, {'$set' : {'abilities.' + label_id : curr_val / 4}})

# 重新计算门槛
for user in db.user.find({'status' : 'ACTIVATED'}):
	interests = user.get('interests')
	if interests:
		cnt = Counter(interests)
		abilities = user.get('abilities')
		if abilities:
			for (key, value) in abilities.items():
				cnt[key] += value
		total_val = sum(cnt.values())
		boss_val = total_val * 0.8
		print 'Boss value : %f' % boss_val
		items = 0
		incs = 0
		for (item, count) in cnt.most_common(len(cnt)):
			items += 1
			incs += count
			if incs > boss_val:
				threshold = total_val / items / 2
				print 'threshold: %f' % threshold
				db.user.update({'_id' : user.get('_id')}, {'$set' : {'threshold' : threshold}})
				break
