from pymongo import Connection

host = '127.0.0.1'
#host = '172.16.1.50'

db = Connection(host).wendui

email_settings = ['EMAIL_SEND_ME_PRIVATE','EMAIL_INVITE_ME_QUESTION','EMAIL_NEW_ANSWER','ACCEPT_MASSIVE_EMAIL']
pri_settings = ['PRIVATE_ALL', 'PRIVATE_CONCERNED']

for user in db.user.find({'status':'ACTIVATED','accept_all_msg':{'$exists': False}}):
	uid = user['_id']
	settings = user.get('settings')
	if not settings:
		print uid
	else:
		eset = [item for item in email_settings if item in settings]
		accept_msg_set = 'PRIVATE_ALL' in settings
		for rem in email_settings + pri_settings:
			if rem in settings:
				settings.remove(rem)
		db.user.update({'_id': uid}, {'$set': {
		 'msg_settings': settings,
		 'email_settings': eset, 
		 'accept_all_msg': accept_msg_set}, 
		                              '$addToSet': {
		 'email_settings': 'ACCEPT_MASSIVE_EMAIL', 
		 'msg_settings': {'$each': ['MESSAGE_REF_ME','REPLY_ON_MOOD_COMMENT','ENQUIRE_ME','ENQUIRE_REPLYED','NEW_COMMENT_ON_MOOD','NEW_SUGGESTED','NEW_SUMMARIED','NEW_SHARE']}}})
