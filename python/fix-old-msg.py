from pymongo import Connection

#host = '172.16.1.50'
host = '127.0.0.1'

db = Connection(host).wendui

def main():
	for n_msg in db.message.find({'partitions': {'$exists': True}}):
		nmsg_id = n_msg['_id']
		print nmsg_id

		parts = n_msg['partitions']
		domainId = n_msg['domain_id']
		for i in range(len(parts)):
			part = parts[i]
			if domainId == part['_id']:
				if part['role'] == 'SENDER':
					db.message.update({'_id': nmsg_id}, {'$set': {'type': 'SEND'}})
				else:
					db.message.update({'_id': nmsg_id}, {'$set': {'type': 'RECEIVE'}})

if __name__ == '__main__':
	main()
