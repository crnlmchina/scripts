var gids = ['pvpcrnwkh','pvpjqqrlk','pwrxnnxcp','pvrfpvbvm','pwrspjkkz','pvpcswjvm','pvpdkkbry','rgzmxqbwt'];
var cursor = db.op_user_group.find({_id:{$in:gids}});
while(cursor.hasNext()){
     var curr = cursor.next();
     var ids = curr.ids;
     var id = curr._id;
	 var friendlyUids = [];
     ids.forEach(function(uid){
		var user = db.user.findOne({_id:uid,status:"ACTIVATED",register_time:{'$exists':true}});
		if(user){
			friendlyUids.push(uid);
		}
    });
    db.op_user_group.update({_id:id},{$set:{ids:friendlyUids}});
}

