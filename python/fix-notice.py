from pymongo import Connection

#host = '172.16.1.50'
host = '127.0.0.1'

db = Connection(host).wendui


def enquiryReplyed():
	for notice in db.notification.find({'category': 'ENQUIRE_REPLYED'}):
		print 'id is : %s' % notice['_id']
		refId = notice.get('ref_id')
		if refId:
			enquiry = db.enquiry.find_one({'_id': refId})
			if not enquiry:
				enquiry = db.enquiry.find_one({'qid': refId, 'author_id': notice['from']})
				print enquiry['_id']
				db.notification.update({'_id': notice['_id']}, {'$set': {'ref_id': enquiry['_id']}})

def moodComment():
	for notice in db.notification.find({'category': 'REPLY_ON_MOOD_COMMENT'}):
		refId = notice.get('ref_id')
		if refId:
			mComment = db.mood_comment.find_one({'_id': refId})
			if not mComment:
				print notice['_id']
				for mc in db.mood_comment.find({'mid': refId, 'author_id': notice['from']}).sort('create_time', -1):
					print mc['create_time'], notice['create_time']
					if mc['create_time'] <= notice['create_time']:
						print 'Choose mood: %s' % mc['_id']
						db.notification.update({'_id': notice['_id']}, {'$set': {'ref_id': mc['_id']}})
						break


def main():
	enquiryReplyed()
	moodComment()

if __name__ == '__main__':
	main()

