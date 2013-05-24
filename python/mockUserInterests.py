# -*- coding: utf8 -*-
'''
Created on 2012-3-5

@author: wangyuxaun
'''
from pymongo import *
from pyExcelerator import *
import re

_output_report_name='/home/wendui/scripts/python/mock_user_interests.xls'
#_output_report_name='C:/data/mock_user_interests.xls'
_mongo_host='127.0.0.1'
_categories={
    'vmlrkfkytk' : u'管理和创业',
    'vmlrykwrbk' : u'职场攻略',
    'vmmjvqrdkb' : u'专业和业务'
}
_max_label_count=25

db = Connection(_mongo_host).wendui

wb = Workbook()
ws0 = wb.add_sheet('0')

row = 0
ws0.write(row, 0, u'行业')
ws0.write(row, 1, u'职位')
ws0.write(row, 2, u'兴趣')
ws0.write(row, 3, u'推荐问题数')
row += 1
            
def chooseLabels(industryId, domainId, rootId):
    labels = db.profession_label.find_one({'industry' : industryId, 'domain' : domainId})['labels']
    labels = filterLabels(labels, rootId)
    if labels:
        heavy_labels = findHeavyLabels(labels)
        return heavy_labels
    
    
def filterLabels(labels, rootId):
    return [label for label in labels if rootId in roots(label)]
    
def roots(label):
    record = db.label.find_one({'_id' : label}, {'paths' : 1})
    if record:
        paths = record['paths']
        return [path.split('.')[0] for path in paths]
    else:
        return []
    
def findHeavyLabels(labels):
    heavy_labels = []
    avgs = perfectAvg(_max_label_count, len(labels))
    for i in range(len(labels)):
        label = labels[i]
        path = db.label.find_one({'_id' : label})['paths'][0]
        descents = db.label.find({'paths' : re.compile('^'+path)}).distinct('_id')
        for key in db.key.find({'_id' : {'$in' : descents}}).sort('q_count', DESCENDING).limit(avgs[i]):
            heavy_labels.append(key['_id'])
    return heavy_labels
    
def perfectAvg(max_count, count):
    (div, mod) = divmod(max_count, count)
    avgArr = [div + (mod > i and 1 or 0) for i in range(count)]
    return avgArr
    
_basic_query={
    'auth_status' : 'PASSED',
    'quality' : {'$in' : ['EXCELLENT', 'GOOD']}
}
for industry in db.industry.find({'deleted' : {'$ne' : True}}).sort('order', DESCENDING):
    for domain_id in industry['domains']:
        domain = db.domain.find_one({'_id' : domain_id})
        for key in _categories.keys():
            labels = chooseLabels(industry['_id'], domain['_id'], key)
            if labels:
                _basic_query['labels'] = {'$in' : labels}
                counts = db.question.find(_basic_query).count()
                ws0.write(row, 0, industry['name'])
                ws0.write(row, 1, domain['name'])
                ws0.write(row, 2, _categories[key])
                ws0.write(row, 3, counts)
                row += 1
                
wb.save(_output_report_name)
