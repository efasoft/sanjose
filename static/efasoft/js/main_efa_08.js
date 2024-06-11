(function($) {

	"use strict";

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	var carousel = function() {
		$('.featured-carousel-08').owlCarousel({
	    loop:true,
	    autoplay: true,
	    autoHeight: false,
	    margin:30,
	    animateOut: 'slideOutDown',
    animateIn: 'flipInX',
	    nav:true,
	    dots: false,
	    autoplayHoverPause: false,
	    items: 1,
	    navText : ["<p><small>Ant.</small><span class='ion-ios-arrow-round-back'></span></p>","<p><small>Sig.</small><span class='ion-ios-arrow-round-forward'></span></p>"],
	    responsive:{
	      0:{
	        items:1
	      },
	      600:{
	        items:1
	      },
	      1000:{
	        items:1
	      }
	    }
		});

	};
	carousel();

})(jQuery);