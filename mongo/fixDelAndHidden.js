db.answer.update({deleted:{$exists:false}},{$set:{deleted:false}},false,true);
db.answer.update({hidden:{$exists:false}},{$set:{hidden:false}},false,true);
db.question.update({deleted:{$exists:false}},{$set:{deleted:false}},false,true);
db.question.update({hidden:{$exists:false}},{$set:{hidden:false}},false,true);
db.comment.update({deleted:{$exists:false}},{$set:{deleted:false}},false,true);
db.comment.update({hidden:{$exists:false}},{$set:{hidden:false}},false,true);
db.mood_comment.update({deleted:{$exists:false}},{$set:{deleted:false}},false,true);
db.mood_comment.update({hidden:{$exists:false}},{$set:{hidden:false}},false,true);
db.mood.update({deleted:{$exists:false}},{$set:{deleted:false}},false,true);
db.mood.update({hidden:{$exists:false}},{$set:{hidden:false}},false,true);
db.enquiry.update({deleted:{$exists:false}},{$set:{deleted:false}},false,true);
db.enquiry.update({hidden:{$exists:false}},{$set:{hidden:false}},false,true);
db.notification.update({deleted:{$exists:false}},{$set:{deleted:false}},false,true);
db.notification.update({hidden:{$exists:false}},{$set:{hidden:false}},false,true);
db.message.update({deleted:{$exists:false}},{$set:{deleted:false}},false,true);
db.message.update({hidden:{$exists:false}},{$set:{hidden:false}},false,true);


db.key.update({deleted:{$exists:false}},{$set:{deleted:false}},false,true);
db.advice.update({deleted:{$exists:false}},{$set:{deleted:false}},false,true);
db.user.update({deleted:{$exists:false}},{$set:{deleted:false}},false,true);
db.label_effection.update({deleted:{$exists:false}},{$set:{deleted:false}},false,true);
db.profession_group.update({deleted:{$exists:false}},{$set:{deleted:false}},false,true);
db.tips.update({deleted:{$exists:false}},{$set:{deleted:false}},false,true);