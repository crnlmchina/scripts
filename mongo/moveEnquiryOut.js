db.enquiry.ensureIndex({qid:1});
db.enquiry.ensureIndex({author_id:1});
var cursor = db.question.find({enquirys:{$exists:true}});
while(cursor.hasNext()){
	var curr = cursor.next();
	if(curr.enquirys){
		curr.enquirys.forEach(function(item){
			item['qid'] = curr._id;
			db.enquiry.insert(item);
		});
	}
}
db.question.update({},{$unset:{enquirys:1}},false,true);