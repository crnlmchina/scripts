from pymongo import Connection
import sys
from datetime import datetime

host = '127.0.0.1'
#host = '172.16.1.50'

db = Connection(host).wendui

file_name = sys.argv[1]

print file_name

for email in open(file_name):
	email_add = email.strip()
	print email_add
	db.invalid_email.insert({'_id': email_add, 'create_time': datetime.now()})
