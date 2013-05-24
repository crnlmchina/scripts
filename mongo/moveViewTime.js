var cursor = db.user.find({topic_view_time:{$exists:true}},{topic_view_time:1});
while(cursor.hasNext()){
	var curr = cursor.next();
	db.user_last_action.insert(curr);
}