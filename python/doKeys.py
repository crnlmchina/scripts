# -*- coding: UTF-8 -*-
from pymongo import Connection
import os

KEY_PATH = '/tmp'

print 'Del keys'

#host = '172.16.1.50'
host = '127.0.0.1'
db = Connection(host).wendui

print db.key.find().count()
for dkey in open(os.path.join(KEY_PATH, 'del.txt')):
	dkey = dkey.rstrip()
	db.key.remove({'name' : dkey})
print db.key.find().count()

print 'Move keys'
print db.key.find({'level' : 2}).count()
for mkey in open(os.path.join(KEY_PATH, 'move.txt')):
	mkey = mkey.rstrip()
	db.key.update({'name' : mkey}, {'$set' : {'level' : 1}})
print db.key.find({'level' : 2}).count()
