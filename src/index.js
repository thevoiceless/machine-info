$(document).ready(function() {
	// Click machine name to show information
	// Get all .machine-header and .machine-info elements, which occur in pairs
	// When a .machine-header is clicked, expand its associated .machine-info
	var $elements = $('.machine-header, .machine-info');
	$('.machine-header').click(
		function() {
			$elements.eq($elements.index(this) + 1).slideToggle();
		});

	// Show/hide CPU details on click
	$('tr#cpu-row').click(
		function() {
			$('tr.hidden.cpu').each(
				function() {
					$(this).fadeToggle()
				})
	});

	// Show/hide memory details on click
	$('tr#mem-row').click(
		function() {
			$('tr.hidden.mem').each(
				function() {
					$(this).fadeToggle()
				})
	});

	// Show/hide process details on click
	$('tr#proc-row').click(
		function() {
			$('tr.hidden.proc').each(
				function() {
					$(this).fadeToggle()
				})
		});

	// Show/hide interrupts table on click
	$('tr#int-row').click(
		function() {
			$('tr.hidden.int').each(
				function() {
					$(this).fadeToggle()
				})
		});

	// Set tooltips for the different sections of the Processes bar
	$('div#running-procs-bar').tooltip({'title':'Running','placement':'bottom'});
	$('div#sleeping-procs-bar').tooltip({'title':'Sleeping','placement':'bottom'});
	$('div#stopped-procs-bar').tooltip({'title':'Stopped','placement':'bottom'});
	$('div#zombie-procs-bar').tooltip({'title':'Zombie','placement':'bottom'});
});