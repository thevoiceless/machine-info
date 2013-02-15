$(document).ready(function() {
	$('tr#cpu-row').tooltip({'title':'Click to show/hide details','delay':100});
	$('tr#cpu-row').click(
		function() {
			$('tr.hidden.cpu').each(
				function() {
					$(this).fadeToggle()
				})
	});
	$('tr#mem-row').tooltip({'title':'Click to show/hide details','delay':100});
	$('tr#mem-row').click(
		function() {
			$('tr.hidden.mem').each(
				function() {
					$(this).fadeToggle()
				})
	});
});