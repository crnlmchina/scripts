# -*- coding: UTF-8 -*-
from pymongo import Connection
import re

host = '127.0.0.1'
#host = '172.16.1.50'
db = Connection(host).wendui

invEmails = db.user.find({'status' : 'INVITED'}).distinct('email')
actEmails = db.user.find({'status' : 'ACTIVATED'}).distinct('email')

for email in actEmails:
	if email in invEmails:
		invEmails.remove(email)

print len(invEmails)
db.mail_queue.update({'email':{'$in' : invEmails},'status':'SENT', 'title' : re.compile(r'.*加入问对网$')}, {'$set':{'status':'READY'}}, multi=True)
queue_count = db.mail_queue.find({'status':'READY'}).count()
print '%d mails in queue' % queue_count
