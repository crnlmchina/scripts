# -*- coding: UTF-8 -*-
from pymongo import Connection
import re

#host = '172.16.1.50'
host = '127.0.0.1'

db = Connection(host).wendui

def main():
	curr_path = list()
	total = list()
	for rootLabel in db.label.find({'root': True}):
		del curr_path[:]
		curr_path.append(rootLabel['_id'])
		check_sub(curr_path, total)
	#print len(total)

def check_sub(path, total):
	total.append(1)
	current_path = '.'.join(path)
	#print current_path
	query = {'paths': re.compile('^' + current_path + '\.[^.]+$')}
	subs = db.label.find(query).count()
	if len(path) >= 5:
		if subs > 0:
			print_path(path)
	else:
		for sub in db.label.find(query):
			path.append(sub['_id'])
			check_sub(path, total)
	path.pop()

def print_path(path):
	cn_path = list()
	for node in path:
		nname = db.key.find_one({'_id': node}).get('name', u'')
		#print type(nname), nname
		cn_path.append(nname)
	#print cn_path
	print u' -> '.join(cn_path)


if __name__ == '__main__':
	main()
