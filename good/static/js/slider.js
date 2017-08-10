$(document).ready(function(){

var active=0;
var agree=true;
var directionE='L';
var count =parseInt($('#count').attr('value'));

	setTimeout(	 NextSlide, 10000);

function NextSlide(){
	
	if(directionE=='L'){
		$('.controlleft').trigger("click");
	}else{
		$('.controlright').trigger("click");
	}
	setTimeout(	NextSlide, 10000);
}

$('.controlleft').click(function(event) {
	directionE='L';

if(agree==true){
		agree=false;
var nex=0;
	if(active==count-1){
		nex=0;
	}else {
		nex=active+1;
	}
	$('.slider').children('.slide:eq('+active+')').animate({'right': 1200}, 1000);
	$('.slider').children('.slide:eq('+active+')').attr('class', 'slide');
	$('.slider').children('.slide:eq('+(nex)+')').css('right',-1200);
	$('.slider').children('.slide:eq('+nex+')').animate({'right': 0}, 1000,function(){
		setTimeout(function(){agree=true;},500);
	});
	$('.slider').children('.slide:eq('+(nex)+')').attr('class', 'slide active');

positionSliderInc();
	}
});
$('.controlright').click(function(event) {
		directionE='R';
	if(agree==true){
		agree=false;
	var nex=0;
	if(active==0){
		nex=count-1;
	}else {
		nex=active-1;
	}

	$('.slider').children('.slide:eq('+active+')').animate({'right': -1200}, 1000);
	$('.slider').children('.slide:eq('+active+')').attr('class', 'slide');

	$('.slider').children('.slide:eq('+(nex)+')').css('right',1200);
	$('.slider').children('.slide:eq('+nex+')').animate({'right': 0}, 1000,function(){
		setTimeout(function(){agree=true;},500);
	});
	$('.slider').children('.slide:eq('+(nex)+')').attr('class', 'slide active');

positionSliderDec();
}

});



function positionSliderInc(){
	console.log('active='+active);
	active+=1;
	if(active==count){
		active=0;
	}
	console.log('->'+active);

}
function positionSliderDec(){
		console.log('active='+active);
	active-=1;
	if(active==-1){
		active=count-1;
	}console.log('->'+active);
}




































































/*

function NextSlide(){

	if(directionE=='L'){
		$('.controlleft').trigger("click");
	}else{
		$('.controlright').trigger("click");
	}
	setTimeout(	NextSlide, 60000);
}

$('.controlleft').click(function(event) {
	directionE='L';

if(agree==true){
		agree=false;
var nex=0;
	if(active==2){
		nex=0;
	}else {
		nex=active+1;
	}
	$('.slider').children('.slide:eq('+active+')').animate({'right': 1200}, 1000);
	$('.slider').children('.slide:eq('+active+')').attr('class', 'slide');
	$('.slider').children('.slide:eq('+(nex)+')').css('right',-1200);
	$('.slider').children('.slide:eq('+nex+')').animate({'right': 0}, 1000,function(){
		setTimeout(function(){agree=true;},500);
	});
	$('.slider').children('.slide:eq('+(nex)+')').attr('class', 'slide active');

positionSliderInc();
	}
});
$('.controlright').click(function(event) {
		directionE='R';
	if(agree==true){
		agree=false;
	var nex=0;
	if(active==0){
		nex=2;
	}else {
		nex=active-1;
	}

	$('.slider').children('.slide:eq('+active+')').animate({'right': -1200}, 1000);
	$('.slider').children('.slide:eq('+active+')').attr('class', 'slide');

	$('.slider').children('.slide:eq('+(nex)+')').css('right',1200);
	$('.slider').children('.slide:eq('+nex+')').animate({'right': 0}, 1000,function(){
		setTimeout(function(){agree=true;},500);
	});
	$('.slider').children('.slide:eq('+(nex)+')').attr('class', 'slide active');

positionSliderDec();
}

});



function positionSliderInc(){
	console.log('active='+active);
	active+=1;
	if(active==3){
		active=0;
	}
	console.log('->'+active);

}
function positionSliderDec(){
		console.log('active='+active);
	active-=1;
	if(active==-1){
		active=2;
	}console.log('->'+active);
}*/
});