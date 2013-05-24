db.prestige_map.remove();
var prestiges = [
	{_id:1,name:"新手",upgrade_point:51,att_limit:50},
	{_id:2,name:"见习顾问",upgrade_point:201,att_limit:200},
	{_id:3,name:"顾问",upgrade_point:2001,att_limit:400},
	{_id:4,name:"资深顾问",upgrade_point:50001,att_limit:1000},
	{_id:5,name:"董事顾问",upgrade_point:2000001,att_limit:1000000},
	{_id:6,name:"资深董事顾问",upgrade_point:-1,att_limit:1000000}
];
prestiges.forEach(function(item){db.prestige_map.insert(item);});