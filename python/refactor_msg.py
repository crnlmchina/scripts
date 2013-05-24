from pymongo import Connection

host = '127.0.0.1'
#host = '172.16.1.50'
db = Connection(host).wendui

for msg in db.message.find({'type': 'RECEIVE'}):
	print msg['_id']
	domain_id = msg['domain_id']
	target_id = msg['target_id']
	session_id = '%s:%s' % (domain_id, target_id) if domain_id < target_id else '%s:%s' % (target_id, domain_id)

	partitions = [{'_id': domain_id, 'role': 'RECIPIENT', 'deleted': msg['deleted']}, {'_id': target_id, 'role': 'SENDER', 'deleted': False}]
	db.n_msg.insert({
		'_id': msg['_id'], 
		'create_time': msg['create_time'],
		'hidden': msg.get('hidden', False),
		'content': msg['content'],
		'is_html': msg.get('is_html', False),
		'ignore': msg.get('ignore', False),
		'read': msg['status'] == 'READ',
		'op_sender': msg.get('fsend_id', None),
		'session_id': session_id,
		'partitions': partitions})
