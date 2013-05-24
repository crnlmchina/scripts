from pymongo import Connection

host = '127.0.0.1'
#host = '172.16.1.50'
db = Connection(host).wendui

def updateData():
	count = 0
	for email in db.mail_queue.find():
		email_address = email['email']
		if not email_address.islower():
			count += 1
			print email_address, email['create_time']
			#db.mail_queue.update({'_id': email['_id']}, {'$set': {'email': email_address.lower()}})
	print count

if __name__ == '__main__':
	updateData()
