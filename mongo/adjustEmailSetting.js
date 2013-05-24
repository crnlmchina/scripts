// Open all email settings of message for the users did not open the email setting page
// Author: yuxuan

var seenUsers = db.user_action.distinct('user_id',{type:'SETTINGACTION.INITEMAILREMIND'}); 
javascript:print('User count open email setting:'+seenUsers.length);

db.user.update({_id:{$nin:seenUsers}},{$addToSet:{settings:{$each:['EMAIL_INVITE_ME_QUESTION','EMAIL_NEW_ANSWER']}}},false,true);
javascript:print('ok, complete.');
