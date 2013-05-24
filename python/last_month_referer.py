# -*- coding: UTF-8 -*-
from pymongo import Connection
from datetime import datetime, timedelta
import re
from collections import defaultdict

#host = '172.16.1.50'
host = '127.0.0.1'

def main():
	end = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)

	start = end - timedelta(days=30)

	print start, end
	file_name = 'month %s-referer.txt' % start.month

	referer_re = re.compile(r'^http.*$')

	classified_referers = defaultdict(list)

	db = Connection(host).wendui
	for user_action in db.user_action.find({'time': {'$gte': start, '$lt': end}, 'referer': referer_re}):
		referer = user_action['referer']
		classified_referers[getSimpleDomain(referer)].append(referer)

	out = open(file_name, 'wb')
	for k, v in classified_referers.items():
		print k
		if k == 'www.wendui.com' or k == 'wendui.com':
			continue
		for val in v:
			out.write(('%s, %s\n' % (k, val)).encode('utf-8'))

	out.close()


def getSimpleDomain(url):
	mat = re.compile(r'^https?://(.*?)(/.*)?$').match(url)
	if mat:
		return mat.group(1)

if __name__ == '__main__':
	main()
