from pymongo import Connection

#host = '172.16.1.50'
host = '127.0.0.1'

db = Connection(host).wendui

def main():
	ids = ['fgmvhswldw','fgkmvlhmrl','fgqmkzymkh','ffwfvlnlrz','fgczsqkyny','fgkvgzmmjh','fglybgxwbx','fgmhdcyvwk','fgnbnfghzv','fgpfcqgdql','fgqgwqwbkg','fgqkxclhdt','fgrwfrxpsl','fgstycdxbr','fgthxrmfyz','fgttyqdckp','fgvzsrsldz','fgnqpqwscn','fgxphntxjd','fgkpdczlzx','fgpltrxshq']
	for user in db.user.find({'_id': {'$in': ids}}):
		print user['name'], user['email']

if __name__ == '__main__':
	main()
