var gids = ['pvpcrnwkh','pvpjqqrlk','pwrxnnxcp','pvrfpvbvm','pwrspjkkz','pvpcswjvm','pvpdkkbry','rgzmxqbwt'];
var cursor = db.op_user_group.find({_id:{$in:gids}});
var friendlyUids = [];
while(cursor.hasNext()){
     var curr = cursor.next();
     var ids = curr.ids;
     friendlyUids = friendlyUids.concat(ids);
}
var end= new Date();
var start= new Date();
start.setHours(0);
start.setMinutes(0);
start.setSeconds(0);
start.setMilliseconds(0);

var query = {deleted:false,hidden:false,create_time:{$gte:start,$lt:end},author_id:{$in:friendlyUids}};
var questionsCursor = db.question.find(query);
while(questionsCursor.hasNext()){
     var qCurr = questionsCursor.next();
         var authorId = qCurr.author_id;
     var group = db.op_user_group.findOne({ids:qCurr.author_id,_id:{$in:gids}});
     db.ques_score.insert({_id:qCurr._id,create_time:qCurr.create_time,author_group_id:group._id});
}
