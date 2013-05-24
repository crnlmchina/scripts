var cursor = db.topic.find();
var partTypes = ['ANSWERACTION.VOTEAGREE', 'ANSWERACTION.VOTEDISAGREE', 'QUESTIONACTION.ADD', 'QUESTIONACTION.ANSWER', 'QUESTIONACTION.VOTEAGREE', 'QUESTIONACTION.ASK', 'QUESTIONACTION.ASKUSERANSWER', 'COMMENTACTION.SUBMIT'];
while(cursor.hasNext()){
	var curr = cursor.next();
	var qid = curr._id;
	var subQs = db.question.distinct('_id',{path:{$regex:'^'+qid+'.*'}, deleted:{$ne:true}, operation_deleted:{$ne:true}});
	if(subQs != null){
		var subQCount = subQs.length;
		subQs.push(qid);
		var subAs = db.answer.distinct('_id',{question_id:{$in:subQs}, deleted:{$ne:true}, operation_deleted:{$ne:true}});
		var subACount = subAs.length;
		var viewCount = db.user_action.count({target_id:{$in:subQs}, type:'QUESTIONACTION.INDEX'});
		var publishIds = subQs.concat(subAs);
		var partUids = db.user_action.distinct('user_id',{target_id:{$in:publishIds}, type:{$in:partTypes}});
		var partUsers = [];
		var partUCount = partUids.length;
		var uCursor = db.user.find({_id:{$in:partUids}},{face_authed : 1,has_authed_face : 1,has_face : 1,name : 1});
		while(uCursor.hasNext()){
			partUsers.push(uCursor.next());
		}
		var consulantIds = db.ques_sub_info.distinct('splitor_id',{qid:{$in:subQs}});
		var consulants = [];
		var uCursor = db.user.find({_id:{$in:consulantIds}},{face_authed : 1,has_authed_face : 1,has_face : 1,name : 1});
		while(uCursor.hasNext()){
			consulants.push(uCursor.next());
		}
		
		db.topic.update({_id:curr._id},{$set:{'statistics.consulant_team':consulants,'statistics.participation_count':partUCount,'statistics.participations':partUsers}});
		//db.topic.update({_id:curr._id},{$set:{'statistics.consulant_team':consulants,'statistics.sub_q_count':subQCount,'statistics.sub_a_count':subACount,'statistics.participation_count':partUCount,'statistics.participations':partUsers}});
//		db.topic.update({_id:curr._id},{$set:{'statistics.sub_a_count':subACount}});
	}
}
