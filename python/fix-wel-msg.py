# -*-coding:UTF-8 -*-
from pymongo import Connection
import re

#host = '172.16.1.50'
host = '127.0.0.1'

db = Connection(host).wendui

def main():
	for msg in db.n_msg.find({'content': re.compile('尊敬的王豆豆，')}):
		print msg['content']
		print '-' * 10
		db.n_msg.update({'_id': msg['_id']}, {'$set': {'content': msg['content'].replace(u'尊敬的王豆豆，', u'')}})

if __name__ == '__main__':
	main()
