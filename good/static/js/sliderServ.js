$(document).ready(function() {

  var butleft = $('.controls .left');
  var butright = $('.controls .right');
  var slides = $('.display .slide');
  var marks = $('.marks .mark');
  var ActiveSlide = 0;
  var CountSlides = slides.length;
  var canMove = true;
  /*alert(marks.length);*/

  function setSlide(a, direction) {
    if(canMove==true){
      var i=0;
          canMove=false;
    var prev = ActiveSlide;
    if(a==-1){
    switch (direction) {
      case 'R':
        ActiveSlide++;


        break;
      case 'L':
        ActiveSlide--;

        break;
    }
    i = ActiveSlide;
  }else{
i=a;
  }

    slides.each(function(index, el) {
      $(el).removeClass('active');
      $(el).css('z-index', 30);
    });
    marks.each(function(index, el) {
     $(el).removeClass('active');

    });



    if (i >= CountSlides) {
      i = 0;
    }
    if (i < 0) {
      i = CountSlides - 1;
    }
    ActiveSlide = i;
    console.log(i);

  $(marks).eq(i).addClass('active');
    $(slides).eq(i).css('left', 0);
    $(slides).eq(i).css('z-index', 50);
    $(slides).eq(prev).css('z-index',59);
switch (direction) {
  case 'R':

  $(slides).eq(prev).animate({
    'left': '840'
  }, 1000);
    break;
    case 'L':

    $(slides).eq(prev).animate({
      'left': '-840'
    }, 1000);
      break;


}

    //$(slides).eq(i).css('z-index', 50);
    setTimeout(function() {
      console.log(i + direction);
      $(slides).eq(i).addClass('active');
      canMove=true;
    }, 1000);
    /*$(slides).eq(prev).css('z-index', 50);*/

}
  }


  /*first slide is active*/
  if(CountSlides>1){
    setSlide(CountSlides-1, 'L');
  }
  else{
    $('.photolist .galery .controls').css('display','none');
  }








  function NextSlide(direction) {
    switch (direction) {
      case 'R':

        setSlide(ActiveSlide);

        break;
      case 'L':

        setSlide(ActiveSlide);
        break;

      default:
        break;
    }
  }
  /*Left buttom*/
  $(butleft).click(function(event) {
    setSlide(-1, 'L');
  });

  /*right buttom*/
  $(butright).click(function(event) {
    setSlide(-1, 'R');
  });
  $('.marks .mark').click(function(event) {
    if(ActiveSlide!=$(this).index())
    setSlide($(this).index(),'L');
  });

})
