# -*- coding: utf-8 -*-
from datetime import date
from datetime import timedelta
import os


log_path = '/home/wendui/wdweb/logs'
mark = '用时：'

def yesterdayRequest():
	yesterday = date.today() - timedelta(days=1)
	log_file = os.path.join(log_path, 'log_timing.log.' + yesterday.strftime('%Y-%m-%d'))
	print 'Analyzing log file: %s ...' % log_file
	allTime = dict()
	for line in open(log_file):
		if mark in line:
			secPart = line.split(mark, 1)[1]
			thePart = secPart.split(',', 1)[0]
			parts = thePart.split(' msURI:', 1)
			vals = allTime.setdefault(parts[1], [0, 0])
			vals[0] += int(parts[0])
			vals[1] += 1

	for key in allTime.keys():
		vals = allTime.get(key)
		print 'Url: %s,%f,%d' % (key, float(vals[0])/vals[1], vals[0])


if __name__ == '__main__':
	yesterdayRequest()

