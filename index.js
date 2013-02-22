$(document).ready(function() {
	// Click machine name to show information
	// Get all .machine-header and .machine-info elements, which occur in pairs
	// When a .machine-header is clicked, expand its associated .machine-info
	var $elements = $('.machine-header, .machine-info');
	$('.machine-header').click(
		function() {
			$elements.eq($elements.index(this) + 1).fadeToggle();
		});

	$('tr#cpu-row').click(
		function() {
			$('tr.hidden.cpu').each(
				function() {
					$(this).fadeToggle()
				})
	});

	$('tr#mem-row').click(
		function() {
			$('tr.hidden.mem').each(
				function() {
					$(this).fadeToggle()
				})
	});

	$('tr#proc-row').click(
		function() {
			$('tr.hidden.proc').each(
				function() {
					$(this).fadeToggle()
				})
		});

	$('tr#int-row').click(
		function() {
			$('tr.hidden.int').each(
				function() {
					$(this).fadeToggle()
				})
		});

	$('div#running-procs-bar').tooltip({'title':'Running','placement':'bottom'});
	$('div#sleeping-procs-bar').tooltip({'title':'Sleeping','placement':'bottom'});
	$('div#stopped-procs-bar').tooltip({'title':'Stopped','placement':'bottom'});
	$('div#zombie-procs-bar').tooltip({'title':'Zombie','placement':'bottom'});
});