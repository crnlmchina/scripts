# -*- coding: UTF-8 -*-
import smtplib
import sys
from email.mime.text import MIMEText

smtp_host = 'smtp.cosmail.cn'
smtp_port = 25
sender_acc = 'd60@cosmail.cn'
sender_pwd = 'cXcnew2012'
#sender_pwd = 'cxcit2011#'

#test_emails = [
#	'crnlm@163.com',
#	'crnlmcn@sina.com',
#	'crnlmcn@gmail.com',
#	'crnlmcn@yahoo.com',
#	'yuxuanwang@139.com',
#	'yongkaixie@hotmail.com'
#]
test_emails = [
	'yuxuanwang@139.com'
]

def send_mail(to, subject, content):
	msg = MIMEText(content)
	msg['Subject'] = subject
	msg['From'] = 'service@wendui.com'

	msg['To'] = to

	s = smtplib.SMTP(smtp_host, smtp_port)
	s.login(sender_acc, sender_pwd)
	s.sendmail('service@wendui.com', to, msg.as_string())
	s.quit()


if __name__ == '__main__':
	subject = u'daily report'
	content = u'sales: 100 billion'
	for test_e in test_emails:
		try:
			send_mail(test_e, subject.encode('utf8'), content.encode('utf8'))
		except:
			print 'Send mail fail to : ' + test_e
			print sys.exc_info()
