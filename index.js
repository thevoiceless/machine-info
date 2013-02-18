$(document).ready(function() {
	$('.machine-header').tooltip({'title':'Click to show/hide machine information'});

	// Click machine name to show information
	var $elements = $('.machine-header, .machine-info');
	$('.machine-header').click(
		function() {
			$elements.eq($elements.index(this) + 1).fadeToggle();
		});

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
});