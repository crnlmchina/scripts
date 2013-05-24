from pymongo import Connection

db = Connection().wendui

for mail in db.mail_queue.find({'status': 'READY'}):
	db.delay_mail.insert(mail)
	db.mail_queue.remove({'_id': mail['_id']})
