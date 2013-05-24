var cursor = db.mood.find({comments:{$exists:true}});
while(cursor.hasNext()){
	var curr = cursor.next();
	if(curr.comments){
		curr.comments.forEach(function(item){
			item['mid'] = curr._id;
			db.mood_comment.insert(item);
		});
	}
}
db.mood.update({},{$unset:{comments:1,comment_count:1}},false,true);