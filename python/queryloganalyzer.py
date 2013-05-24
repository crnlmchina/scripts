# -*- coding: UTF-8 -*-
from pymongo import Connection
from datetime import datetime
import pprint
import os, sys

splitor = ' - '
host = '127.0.0.1'
result_path = '/tmp/report'
mills_limit = 100

def get_query(log_item):
	if splitor in log_item:
		return log_item.split(splitor, 1)[1]

def iter_log_file(filepath):
	pp = pprint.PrettyPrinter(indent=4)
	db = Connection(host).wendui
	out_file = os.path.join(result_path, 'query_analyzer_result_' + datetime.now().strftime('%y%m%d-%H%M%S'))
	res_out = open(out_file, 'w')
	for line in open(filepath):
		query = get_query(line)
		if query:
			print 'Analyzing... %s' % query
			explain_res = eval(query.rstrip().replace('true', 'True').replace('false', 'False') + '.explain()')
			if explain_res.get(u'millis') > mills_limit:
				res_out.write(pp.pformat(explain_res) + os.linesep)
	res_out.close()
	print 'Ok, all querys analyzer completed, query explain more than %d ms print to file %s' % (mills_limit, out_file)

def check_report_path():
	if not os.path.exists(result_path):
		os.makedirs(result_path)


if __name__ == '__main__':
	args = sys.argv
	if len(args) < 2:
		raise ValueError, 'You must tell me which file to analyze, fuck!'
	check_report_path()
	query_file = args[1]
	print 'Ready to analyze file: %s' % query_file
	iter_log_file(query_file)
