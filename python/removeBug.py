from pymongo import Connection

db = Connection().wendui

sus = u'wprhrvvfmt'

for answ in db.answer.find({'author_id':'wfvfsfcnbd'}):
    auids = answ.get('agree_user_ids')
    if auids and sus in auids:
        print 'sus'
        db.answer.update({'_id':answ['_id']},{'$pull':{'agree_user_ids':sus}, '$inc':{'agree_user_size':-1}})
