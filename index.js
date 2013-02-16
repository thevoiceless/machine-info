$(document).ready(function() {
	$('tr#cpu-row').tooltip({'title':'Click to show/hide details','delay':100});
	$('tr#cpu-row').hover(
		function() {
			$(this).css('background-color', '#EDEDED')
		},
		function() {
			$(this).css('background-color', 'white')
		});
	$('tr#cpu-row').click(
		function() {
			$('tr.hidden.cpu').each(
				function() {
					$(this).fadeToggle()
				})
	});

	$('tr#mem-row').tooltip({'title':'Click to show/hide details','delay':100});
	$('tr#mem-row').hover(
		function() {
			$(this).css('background-color', '#EDEDED')
		},
		function() {
			$(this).css('background-color', 'white')
		});
	$('tr#mem-row').click(
		function() {
			$('tr.hidden.mem').each(
				function() {
					$(this).fadeToggle()
				})
	});

	$('#running-procs-bar').tooltip({'title':'Running','placement':'bottom'})
	$('#sleeping-procs-bar').tooltip({'title':'Sleeping','placement':'bottom'})
	$('#stopped-procs-bar').tooltip({'title':'Stopped','placement':'bottom'})
	$('#zombie-procs-bar').tooltip({'title':'Zombie','placement':'bottom'})

	$('tr#proc-row').tooltip({'title':'Click to show/hide details','delay':100})
	$('tr#proc-row').hover(
		function() {
			$(this).css('background-color', '#EDEDED')
		},
		function() {
			$(this).css('background-color', 'white')
		});
	$('tr#proc-row').click(
		function() {
			$('tr.hidden.proc').each(
				function() {
					$(this).fadeToggle()
				})
		});

	$(".highlight-rows").hover(
		function() {
			$(this).find("td:not(.no-highlight)").addClass('highlight-gray')
			// $(this).css('background-color', '#EDEDED')
		},
		function() {
			$(this).find("td:not(.no-highlight)").removeClass('highlight-gray')
			// $(this).css('background-color', 'white')
		});
});