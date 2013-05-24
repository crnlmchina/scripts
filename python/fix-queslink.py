# -*-coding:UTF-8 -*-
from pymongo import Connection
import re

#host = '172.16.1.50'
host = '127.0.0.1'

db = Connection(host).wendui

def main():
	for msg in db.n_msg.find({'content': re.compile(r'http://www.wendui.com/q/\s')}):
		ncontent = msg['content'].replace('http://www.wendui.com/q/ ', 'http://www.wendui.com/q/')
		print ncontent
		db.n_msg.update({'_id': msg['_id']}, {'$set': {'content': ncontent}})

if __name__ == '__main__':
	main()
