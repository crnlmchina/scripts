from pymongo import Connection

#host = '172.16.1.50'
host = '127.0.0.1'

db = Connection(host).wendui

def main():
	for n_msg in db.n_msg.find():
		nmsg_id = n_msg['_id']
		print nmsg_id
		n_msg['fsend_id'] = n_msg.get('op_sender', None)
		n_msg['deleted'] = False
		n_msg['status'] = 'UNREAD'

		parts = n_msg['partitions']
		for i in range(len(parts)):
			part = parts[i]
			n_msg['domain_id'] = part['_id']
			n_msg['target_id'] = parts[i ^ 1]['_id']
			n_msg['session_id'] = n_msg['domain_id'] + ':' + n_msg['target_id']
			if part['role'] == 'SENDER':
				n_msg['type'] = 'SEND'
				n_msg['_id'] = nmsg_id + '-reverse'
			else:
				n_msg['type'] = 'RECEIVE'
				n_msg['_id'] = nmsg_id
			db.message.insert(n_msg)

			if not db.message_session.find_one({'_id': n_msg['session_id']}):
				db.message_session.insert({'_id': n_msg['session_id'], 'last_update_time': n_msg['create_time'], 'domain_id': n_msg['domain_id']})

		db.n_msg.remove({'_id': nmsg_id})

if __name__ == '__main__':
	main()
