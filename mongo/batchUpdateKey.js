var cursor = db.key.find({deleted:{$exists:false}},{_id:1}).limit(100000);
while(cursor.hasNext()){
	db.key.update({_id:cursor.next()._id},{$set:{deleted:false}})
}
