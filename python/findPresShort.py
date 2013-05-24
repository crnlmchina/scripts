# -*- coding:utf-8 -*-
from pymongo import Connection

import findUserPrestige as fup

#host = '172.16.1.50'
host = '127.0.0.1'

if __name__ == '__main__':
        db = Connection(host).wendui
        for user in db.user.find({'status':'ACTIVATED'}):
                uid = user['_id']
                if uid == 'jptxfyqvb':
                        continue
                curr_pres = user.get('prestige', 0)
                should_pres = fup.realPres(uid)
                if should_pres > curr_pres:
                        #db.user.update({'_id':uid},{'$set':{'prestige':should_pres}})
                        print 'User:[%s : %s], should prestige: %d, current prestige: %d, shorts: %d' % (uid, user.get('name'), should_pres, curr_pres, should_pres - curr_pres)
