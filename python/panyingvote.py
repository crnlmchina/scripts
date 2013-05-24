#-*- coding: UTF-8 -*-
from datetime import datetime,timedelta
from pymongo import Connection

host = '127.0.0.1'
#host = '172.16.1.50'
db = Connection(host).wendui
newtime = datetime.now() + timedelta(days=365)
db.question.update({'_id' : 'wjppydnfhn'}, {'$set' : {'poll_deadline' : newtime}})
