function uncheck(){
    document.getElementById('check').checked = false;
}

$(window).resize(function(){
    if(window.innerWidth < 620){
      $('nav').removeClass('navcenter');
    }else{
      $('nav').addClass('navcenter');
    }
  });

$(document).ready(function () {
	$(window).scroll(function () {
		// console.log($(document).scrollTop());
		if ($(document).scrollTop() > 50) {
			$(".main-head").addClass("head-bg");
			$(".mob-head").addClass("head-bg");
			$(".head").hide();
		} else {
			$(".main-head").removeClass("head-bg");
			$(".mob-head").removeClass("head-bg");
			$(".head").show();
		}
	});
});

// $(function () {
//     $("#s1").scroll(function () {
//       var $nav = $(".black");
//       $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
//     });
//   });

// $(window).scroll(function(){
//     if($("#s1").scrollTop()){
//         $("nav").addClass(".black");
//     }
//     else{
//         $("nav").removeClass(".black");
//     }
// })

// $(document).ready(function(){       
//     var scroll_start = 0;
//     var startchange = $('#startchange');
//     var offset = startchange.offset();
//      if (startchange.length){
//     $(document).scroll(function() { 
//        scroll_start = $(this).scrollTop();
//        if(scroll_start > offset.top) {
//            $("navb").css('background-color', '#f0f0f0');
//         } else {
//            $('nav').css('background-color', 'transparent');
//         }
//     });
//      }
//  });