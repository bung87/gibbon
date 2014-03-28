var btms=[200,240,280,320,280,240,200,160]
var upspeed=200,downspeed=1000;
var seq=[]
var effect=function(idx){
    $(this).animate(
    {
    bottom:btms[idx]
    }, upspeed, 'ease-out',function () {

       $(this).animate({bottom:60},downspeed,'ease-in',function(){
           $(this).prev().css('background','#999');
       });
    });
};
$(document).on('click','.dot_blue',function(e){
    var idx=$('.dot_blue').index(this);
    if(seq.indexOf(idx+1)==-1){
        seq.push(idx+1);
        effect.call(this,idx);
    }else{
        //clicked
    }


});

$('#btn2').on('click',function(){
    if(seq.length==8){
        var s=seq.join(' ');
        $('#showname_input').val(s);
        $.post('create_event',{showtime: $('#showtime_input').val(),showname:$('#showname_input').val()},function(result){
        console.log(result);
         });
    }else{

    }

});

$('#btn1').on('click',function(){
    $('#showtime_input').val($('#y').val().toString().concat('-').concat($('#m').val().toString()).concat('-').concat($('#d').val().toString())+' '.concat($('#h').val().toString()).concat(':').concat($('#mm').val().toString()));

});
var myDate=new Date();
var y=myDate.getFullYear(); //获取完整的年份(4位,1970-????)
var m=myDate.getMonth()+1; //获取当前月份(0-11,0代表1月)
var d=myDate.getDate(); //获取当前日(1-31)
var h=myDate.getHours(); //获取当前小时数(0-23)
var mm=myDate.getMinutes(); //获取当前分钟数(0-59)
$('#y').val(y);
$('#m').val(m);
$('#d').val(d);
$('#h').val(h);
$('#mm').val(mm);
 $('#showtime_input').val(y.toString().concat('-').concat(m.toString()).concat('-').concat(d.toString())+' '.concat(h.toString()).concat(':').concat(mm.toString()));