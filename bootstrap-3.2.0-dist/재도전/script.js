$(document).ready(function(){
	$('.topmenu').hover(
		function(){
			$(this).fadeTo('fast',0.5);
		},
		function(){
			$(this).fadeTo('fast',1);
		}
		);
	$('.topmenu').click(function(){
		$('#left').toggleClass("hide");

		});
	});
});
