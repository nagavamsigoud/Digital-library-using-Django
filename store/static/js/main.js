$(function() {
	$("body").on("click", "#addTocart", function(event){
		var id = $(this).attr("data-book-id");
		event.preventDefault();
		$.ajax({
			url : "/cart/add/"+id,
			type: "POST",
			headers: {"X-CSRFToken": getCookie("csrftoken")},
			data : {},
			success : function(data){

				$("#snackbar").html("Added to cart");
				var x = document.getElementById("snackbar");
				x.className = "show";
				setTimeout(function(){ x.className = x.className.replace("show", ""); }, 1000);
				totalCart();
			},
			error: function(xhr) {
				var message = (xhr.responseJSON && xhr.responseJSON.error) || "Could not add this book. Please refresh and try again.";
				$("#snackbar").html(message).addClass("show");
			}
		})
	});


	// Initialize SKD Slider only when slider images exist
const slider = $('#demo3');
const sliderImages = slider.find('img');

if (slider.length && sliderImages.length > 0) {
    slider.skdslider({
        delay: 2000,
        animationSpeed: 1000,
        showNextPrev: true,
        showPlayButton: true,
        autoSlide: true,
        animationType: 'fading'
    });
}

	$('#stars li').on('mouseover', function(){
		var onStar = parseInt($(this).data('value'), 10); 
	   
		$(this).parent().children('li.star').each(function(e){
		  if (e < onStar) {
			$(this).addClass('hover');
		  }
		  else {
			$(this).removeClass('hover');
		  }
		});
	  }).on('mouseout', function(){
		$(this).parent().children('li.star').each(function(e){
		  $(this).removeClass('hover');
		});
	  });
	  
	$('#stars li').on('click', function(){
		var onStar = parseInt($(this).data('value'), 10); 
		var stars = $(this).parent().children('li.star');
		
		for (i = 0; i < stars.length; i++) {
		  $(stars[i]).removeClass('selected');
		}
		for (i = 0; i < onStar; i++) {
		  $(stars[i]).addClass('selected');
		}
		var ratingValue = parseInt($('#stars li.selected').last().data('value'), 10);
		var msg = "";
		if (ratingValue > 1) {
			msg = ratingValue;
		}
		else {
			msg = ratingValue;
		}
		responseMessage(msg);
	}); 
	function responseMessage(msg) {
		document.getElementById("id_review_star").value = msg;
	}	

	  $('.responsive').slick({
	  dots: false,
	  infinite: true,
	  speed: 300,
	  autoplay:true,
	  autoplaySpeed:1500,
	  slidesToShow: 11,
	  slidesToScroll: 11,
	  responsive: [
		{
		  breakpoint: 1200,
		  settings: {
			slidesToShow: 3,
			slidesToScroll: 3,
			infinite: true,
			dots: false
		  }
		},
		{
		  breakpoint: 1000,
		  settings: {
			slidesToShow: 8,
			slidesToScroll: 8
		  }
		},
		{
		  breakpoint: 800,
		  settings: {
			slidesToShow: 6,
			slidesToScroll: 6
		  }
		},
		{
		  breakpoint: 600,
		  settings: {
			slidesToShow: 4,
			slidesToScroll: 4
		  }
		},
		{
		  breakpoint: 480,
		  settings: {
			slidesToShow: 2,
			slidesToScroll: 2
		  }
		}
		]
	});
	  
	  $('.regulara').slick({
	  dots: false,
	  infinite: false,
	  speed: 300,
	  slidesToShow: 4,
	  slidesToScroll: 4,
	  responsive: [
		{
		  breakpoint: 1200,
		  settings: {
			slidesToShow: 3,
			slidesToScroll: 3
		  }
		},
		{
		  breakpoint: 950,
		  settings: {
			slidesToShow: 2,
			slidesToScroll: 2
		  }
		}
		]
	});
	  
    $(window).on('load', function() {
        $('.pre_loader').fadeOut('slow');
        $('.pre_loader').remove('slow');
    });  

});

function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length === 2) return parts.pop().split(";").shift();
    return "";
}

function totalCart(){
	$.ajax({
		url: "../cart/totalcart",
		success: function(data){
			$("#gettotalcart").html(data);
			console.log(data)
		}
	})
}


$("input[name='qty']").TouchSpin({
	min: 1,
	max: 10,
	verticalbuttons: false
});
$('article').readmore({speed: 500});



