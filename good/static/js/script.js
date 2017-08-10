$(document).ready(function(){
	$(window).scroll(function() {
		console.log($(window).scrollTop());
		if($(window).scrollTop()>570){

			$('header').addClass('px60');
			$('.buttotop').css('display','block');
		}
		else{
			$('.buttotop').css('display','none');
			$('header').removeClass('px60');

		}
	});
	$('.buttotop').click(function(event) {
		$("html,body").animate({ scrollTop: 0 }, "slow");
	});




	$('.moreCost:first-child').css('display','block');
	$('span.material:first-child').addClass('active');
    $('span.material').click(function (env) {
		$('.moreCost').each(function () {
			$(this).css('display','none');


        });
		$('span.material').each(function () {
			$(this).removeClass('active');
        });

		$(this).addClass('active');
		var id=$(this).attr('for');
		var link='#'+id;

		$(link).css('display','block');
    })

$('.display').css('background-image',$('.pointphoto>.photo:first-child').css('background-image'));

	$('.pointphoto>.photo').click(function () {
		var img=$(this).css('background-image');
		$('.display').css('background-image',img);
    })
	$('.complectation>.content>.exit').click(function () {
		$('.complectation').animate({'opacity':'0'},500);
		setTimeout(function () {
			$('.complectation').css('display','none');
        },500);
    })
$('div.date>.lookmore').click(function () {
			$('.complectation').css('display','block');
	$('.complectation').animate({'opacity':'1'},500);
})



	$('#id_telephone').mask('+7 (999) 999-9999');
})