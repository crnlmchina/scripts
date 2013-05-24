db.user.update({},{$unset:{q_category:1,q_category_rate:1}},false,true);

var partTypes = ['QUESTIONACTION.ASK','QUESTIONACTION.ANSWER','COMMENTACTION.SUBMIT'];
var viewTypes = ['QUESTIONACTION.INDEX','ANSWERACTION.VOTEAGREE','ANSWERACTION.VOTEDISAGREE','QUESTIONACTION.VOTEAGREE','QUESTIONACTION.VOTEDISAGREE'];
var types = [];
partTypes.forEach(function(type){types.push(type);});
viewTypes.forEach(function(type){types.push(type);});

var cursor = db.user_action.find({type:{$in:types}},{type:1,user_id:1,target_id:1});
while(cursor.hasNext()){
	var curr = cursor.next();
	var type = curr.type;
	var userId = curr.user_id;
	if(!userId) continue;
	var targetId = curr.target_id;
	var updates = {};
	var qid = null;
	var value = 0;
	if(type == 'QUESTIONACTION.ASK'){
		qid = targetId;
		value = 5;
	}else if(type == 'QUESTIONACTION.ANSWER'){
		qid = getQidByAid(targetId);
		value = 5;
	}else if(type == 'COMMENTACTION.SUBMIT'){
		qid = getQidByCid(targetId);
		value = 5;
	}else if(['QUESTIONACTION.INDEX','QUESTIONACTION.VOTEAGREE','QUESTIONACTION.VOTEDISAGREE'].indexOf(type) != -1){
		qid = targetId;
		value = 1;
	}else if(['ANSWERACTION.VOTEAGREE','ANSWERACTION.VOTEDISAGREE'].indexOf(type) != -1){
		qid = getQidByAid(targetId);
		value = 1;
	}
	if(qid){
		var qCategory = getField(db.question, qid, 'category');
		if(qCategory){
			inc(userId, qCategory, value);
		}
	}
}

var globalRate = getGlobalRate();
cursor = db.user.find({'deleted' : {'$ne' : true}, 'operation_deleted' : {'$ne' : true}}, {q_category : 1});
while(cursor.hasNext()){
	var curr = cursor.next();
	var category = curr.q_category;
	if(category){
		if(category.A == undefined){category.A = 0}
		if(category.B == undefined){category.B = 0}
		if(category.C == undefined){category.C = 0}
		if(category.D == undefined){category.D = 0}
		if(category.E == undefined){category.E = 0}
		if(category.F == undefined){category.F = 0}
		var total = category.A + category.B + category.C + category.D + category.E + category.F;
		if(total > 0){
			category.A = category.A / total;
			category.B = category.B / total;
			category.C = category.C / total;
			category.D = category.D / total;
			category.E = category.E / total;
			category.F = category.F / total;
			
			category.A = Math.sin((category.A - globalRate.A) / globalRate.A*2);
			category.B = Math.sin((category.B - globalRate.B) / globalRate.B*2);
			category.C = Math.sin((category.C - globalRate.C) / globalRate.C*2);
			category.D = Math.sin((category.D - globalRate.D) / globalRate.D*2);
			category.E = Math.sin((category.E - globalRate.E) / globalRate.E*2);
			category.F = Math.sin((category.F - globalRate.F) / globalRate.F*2);
			
			printjsononeline('Final:' + category);
			db.user.update({_id: curr._id}, {$set: {q_category_rate : category}});
		}
	}
}

function getGlobalRate(){
	var globalRate = {};
	var query = {'deleted' : {'$ne' : true}, 'operation_deleted' : {'$ne' : true}};
	query.category = 'A';
	globalRate.A = db.question.count(query);
	query.category = 'B';
	globalRate.B = db.question.count(query);
	query.category = 'C';
	globalRate.C = db.question.count(query);
	query.category = 'D';
	globalRate.D = db.question.count(query);
	query.category = 'E';
	globalRate.E = db.question.count(query);
	query.category = 'F';
	globalRate.F = db.question.count(query);
	javascript:print(globalRate);
	var total = globalRate.A + globalRate.B + globalRate.C + globalRate.D + globalRate.E + globalRate.F;
	globalRate.A = globalRate.A / total;
	globalRate.B = globalRate.B / total;
	globalRate.C = globalRate.C / total;
	globalRate.D = globalRate.D / total;
	globalRate.E = globalRate.E / total;
	globalRate.F = globalRate.F / total;
	javascript:print(globalRate);
	return globalRate;
}

function inc(uid, type, value){
	if(type == 'A')
		db.user.update({_id:uid},{$inc:{'q_category.A' : value}});
	else if(type == 'B')
		db.user.update({_id:uid},{$inc:{'q_category.B' : value}});
	else if(type == 'C')
		db.user.update({_id:uid},{$inc:{'q_category.C' : value}});
	else if(type == 'D')
		db.user.update({_id:uid},{$inc:{'q_category.D' : value}});
	else if(type == 'E')
		db.user.update({_id:uid},{$inc:{'q_category.E' : value}});
	else if(type == 'F')
		db.user.update({_id:uid},{$inc:{'q_category.F' : value}});
}

function getField(coll, id, field){
	if(!id)
		return null;
	var item = coll.findOne({_id:id});
	if(item)
		return item[field] 
}

function getQidByAid(aid){
	return getField(db.answer, aid, 'question_id');
}

function getQidByCid(cid){
	return getQidByAid(getField(db.comment, cid, 'answer_id'));
}