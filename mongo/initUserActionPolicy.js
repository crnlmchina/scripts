﻿db.user_action_policy.remove();
var datas = [
['REGISTRE',					10,  0,  0,  0,  0,  0],
['DAILY_LOGIN',					 5,  0,  0,  0,  0,  0],
['INFO_PICTURE',				10, 10,  0,  0,  0,  0],
['FIR_ASK',						 2, 10,  0,  0,  2,  0],
['FIR_ANSWER',					 2, 10,  0,  0,  2,  0],
['VISIT_FRIEND_SPACE',			 0,  0,  2,  0,  0,  0],
['VISIT_OTHERS_SPACE',			 0,  0,  1,  0,  0,  0],
['AGREE_QUESTION',				 1,  0,  2,  1,  2,  0],
['AGREE_ANSWER',				 1,  0,  2,  2,  1,  3],
['DISAGREE_QUESTION',			 1,  0, -4, -1,  0,  0],
['DISAGREE_ANSWER',				 1,  0, -1, -2,  0, -3],
['ADD_QUESTION',				 2,  0,  0,  0,  2,  0],
['ADD_ANSWER',					 2,  0,  1,  0,  2,  0],
['ADD_COMMENT',					 2,  0,  1,  0,  2,  0],
['ADD_ENQUIRY',					 1,  0,  1,  0,  1,  0],
['ADMIN_DEL_QUESTION',			 0,  0,  0,-10,  0,  0],
['ADMIN_DEL_ANSWER',			 0,  0,  0,-10,  0,  0],
['UNDO_ADMIN_DEL_QUESTION',		 0,  0,  0, 10,  0,  0],
['UNDO_ADMIN_DEL_ANSWER',		 0,  0,  0, 10,  0,  0],
['ATT_QUESTION',				 1,  0,  2,  1,  4,  0],
['CANCEL_ATT_QUESTION',			 1,  0, -2, -1, -4,  0],
['ATT_USER',					 1,  0, 20,  1,  0,  0],
['CANCEL_ATT_USER',				 1,  0,-20, -1,  0,  0],
['INVITE_USER',					 5,  0,  0,  0,  0,  0],
['BE_CONSULTANT',				 0,  0,  0, 50,  0,  0],
['SEND_MESSAGE',				 1,  0,  5,  0,  0,  0],
['INVITE_USER_ON_QUESTION',		 2,  0, 10,  0,  0,  0],
['ANSWER_WITH_INVITATION',		 0,  0, 10,  0,  0,  0],
['ACCEPT_ANSWER',				 1,  0,  0,  3,  0,  4],
['LONG_TIME_NO_SEE',			-2,  0,  0,  0,  0,  0],
['FAV_TOPIC',					 1,  0,  0,  2,  4,  0],
['CANCEL_FAV_TOPIC',			 1,  0,  0, -2, -4,  0],
['MOOD',						 1,  0,  0,  0,  0,  0],
['MOOD_COMMENT',				 1,  0,  3,  0,  0,  0],
['LAUNCH_POLL',					 1,  0,  0,  0,  0,  0],
['POLL',						 1,  0,  0,  0,  2,  0],
['TOPIC_SUGGESTION',			 2,  0,  0,  0,  2,  0],
['LIKE_SUGGESTION',				 1,  0,  0,  5,  2,  4],
['TOPIC_SUMMARY',				 2,  0,  0,  0,  2,  0],
['VIEW_QUESTION',				 0,  0,  0,  0,  1,  0],
['VIEW_TOPIC',					 0,  0,  0,  0,  1,  0],
['INNER_SHARE',					 1,  0,  3,  0,  4,  0]
];
for(var item in datas){
	var data = datas[item];
	db.user_action_policy.insert({_id:data[0],orig_exp:data[1],orig_pres:data[2],orig_att:data[3],dest_pres:data[4],orig_interest:data[5],dest_ability:data[6]});
}