// Drop indices
var colls = db.getCollectionNames();
colls.forEach(function(coll){
	db.runCommand({dropIndexes: coll, index: '*'});
});

// Create indices
db.answer.ensureIndex({deleted:1});
db.answer.ensureIndex({hidden:1});
db.answer.ensureIndex({question_id:1});
db.answer.ensureIndex({create_time:1});
db.answer.ensureIndex({author_id:1});
db.answer.ensureIndex({status:1});
db.answer.ensureIndex({auth_ill_status:1});

db.comment.ensureIndex({deleted:1});
db.comment.ensureIndex({hidden:1});
db.comment.ensureIndex({create_time:1});
db.comment.ensureIndex({answer_id:1});
db.comment.ensureIndex({author_id:1});
db.comment.ensureIndex({status:1});

db.mail_queue.ensureIndex({status:1});
db.mail_queue.ensureIndex({try_count:1});
db.mail_queue.ensureIndex({create_time:-1});

db.n_msg.ensureIndex({session_id:1});
db.n_msg.ensureIndex({'partitions._id':1});
db.n_msg.ensureIndex({'read':1});

db.notification.ensureIndex({deleted:1});
db.notification.ensureIndex({hidden:1});
db.notification.ensureIndex({to:1});
db.notification.ensureIndex({category:1});
db.notification.ensureIndex({create_time:1});
db.notification.ensureIndex({status:1});

db.question.ensureIndex({deleted:1});
db.question.ensureIndex({hidden:1});
db.question.ensureIndex({author_id:1});
db.question.ensureIndex({create_time:1});
db.question.ensureIndex({domain:1});
db.question.ensureIndex({industry:1});
db.question.ensureIndex({no_reply:1});
db.question.ensureIndex({status:1});
db.question.ensureIndex({hot_lifecycle:-1});
db.question.ensureIndex({locked:1});
db.question.ensureIndex({recommend_top:1});
db.question.ensureIndex({target_users:1});
db.question.ensureIndex({path:1});
db.question.ensureIndex({ignore_by_ops:1});
db.question.ensureIndex({r_labels:1});
db.question.ensureIndex({labels:1});
db.question.ensureIndex({quality:1});
db.question.ensureIndex({auth_status:1});
db.question.ensureIndex({global_visible:1});
db.question.ensureIndex({auth_ill_status:1});

db.user.ensureIndex({deleted:1});
db.user.ensureIndex({email:1,pwd:1});
db.user.ensureIndex({inviter_id:1});
db.user.ensureIndex({name:1});
db.user.ensureIndex({pinyin_name:1});
db.user.ensureIndex({status:1});
db.user.ensureIndex({create_time:1});
db.user.ensureIndex({invited_code:1,email:1});
db.user.ensureIndex({industry:1});
db.user.ensureIndex({domain:1});

db.user_action.ensureIndex({user_id: 1, time:1});
db.user_action.ensureIndex({time: 1});
db.user_action.ensureIndex({type: 1, time:1});
db.user_action.ensureIndex({cookie_unique:1});

db.user_att_ques.ensureIndex({target_id:1});

db.user_att_user.ensureIndex({user_id:1, target_id:1});

db.advice.ensureIndex({uid:1});
db.advice.ensureIndex({visible:1});
db.advice.ensureIndex({create_time:-1});
db.advice.ensureIndex({deleted:-1});

db.question_visitors.ensureIndex({visitor_id:1});
db.question_visitors.ensureIndex({question_id:1});

db.answer_visitors.ensureIndex({visitor_id:1});
db.answer_visitors.ensureIndex({answer_id:1});

db.invitation_code.ensureIndex({dead_line:-1,quality:-1});

db.ques_sub_info.ensureIndex({splitor_id:1});
db.ques_sub_info.ensureIndex({qid:1});

db.fav_topic.ensureIndex({uid:1});

db.qq_ip.ensureIndex({start_num:-1,end_num:1});

db.report.ensureIndex({status:1});

db.mood.ensureIndex({uid:1});
db.mood.ensureIndex({deleted:1});
db.mood.ensureIndex({hidden:1});

db.user_trend.ensureIndex({from:1});
db.user_trend.ensureIndex({hidden:1});
db.user_trend.ensureIndex({ref_id:1});
db.user_trend.ensureIndex({category:1});
db.user_trend.ensureIndex({create_time:-1});

db.mood_comment.ensureIndex({author_id:1});
db.mood_comment.ensureIndex({deleted:1});
db.mood_comment.ensureIndex({hidden:1});

db.enquiry.ensureIndex({qid:1});
db.enquiry.ensureIndex({author_id:1});
db.enquiry.ensureIndex({deleted:1});
db.enquiry.ensureIndex({hidden:1});

db.p_queue.ensureIndex({type:1});

db.label.ensureIndex({paths:1});
db.label.ensureIndex({root:1});

db.key.ensureIndex({name:1},{unique:true,dropDups:true});
db.key.ensureIndex({level:1});
db.key.ensureIndex({free_count:1});
db.key.ensureIndex({nodes:1});
db.key.ensureIndex({q_count:1});
db.key.ensureIndex({deleted:1});

db.label_effection.ensureIndex({deleted:1});
db.label_effection.ensureIndex({uid:1});

db.out_share.ensureIndex({create_time:-1});
db.out_share.ensureIndex({uid:1, target_id:1}, {unique:true, dropDups:true});

db.profession_group.ensureIndex({deleted:1});

db.tips.ensureIndex({deleted:1});
db.tips.ensureIndex({create_time:1});

db.monthly_prestige.ensureIndex({uid:1});
db.monthly_prestige.ensureIndex({month:1});
db.monthly_prestige.ensureIndex({prestige:1});
db.monthly_prestige.ensureIndex({deleted:1});

db.daily_limit.ensureIndex({uid:1, date:1});

db.pres_inc.ensureIndex({uid:1, create_time:-1});

db.invalid_email.ensureIndex({create_time:-1});

db.circle_relation.ensureIndex({cid:1, uid: 1}, {unique:true, dropDups:true});

db.circle_relation.ensureIndex({ uid: 1});
