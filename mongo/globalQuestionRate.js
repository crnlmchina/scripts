var categorys = ['A','B','C','D','E','F'];
var map = {};
var total = 0;
categorys.forEach(function(value){
        var count = db.question.count({category:value});
        total += count;
        map[value]=count;
});

categorys.forEach(function(value){
        map[value]=map[value]/total;
});
db.constants.update({_id:'global_question_map'},{$set:{value:map}});
