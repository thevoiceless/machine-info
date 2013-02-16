Project 2 - Riley Moses
==========

Files
----------
1. `alamode-sentry`
2. `alamode-publish`
3. `results.html.erb`
4. `index.css`
5. `index.js`
6. `bootstrap.min.css`
7. `bootstrap.min.js`
8. `jquery-1.9.1.min.js`

Machine Information Format
----------
The specific commands used to collect information are detailed in the `alamode-sentry` script.

Information is saved in a text file with the same name as the machine from which it was gathered (no file extension). One file is created for each machine and contains one line for each property, with the exception of the interrupts table. The lines are of the format `key=value`, using the following keys:

* `cpu_utilization` - The entire CPU utilization string provided by `top`, which is then separated into:
	* `cpu_utilization_hi` - Hardware interrupts
	* `cpu_utilization_idle` - Idle
	* `cpu_utilization_ni` - Nice
	* `cpu_utilization_si` - Software interrupts
	* `cpu_utilization_st` - Steal time
	* `cpu_utilization_system` - System
	* `cpu_utilization_user` - User
	* `cpu_utilization_wa` - I/O Wait
* `date` - The current date when the information is collected
* `load_avg_01min` - Load average for the last 1 minute
* `load_avg_05min` - Load average for the last 5 minutes
* `load_avg_15min` - Load average for the last 15 minutes
* For each cache level:
	* `lvl\*_cache_size` - Size, in kB
	* `lvl\*_cache_type` - Type (data, instruction, unified)
* `memory_free` - Free memory, in kB
* `memory_total` - Total memory, in kB
* `num_users` - The number of users logged in
* `processes_total` - The total number of processes, divided into:
	* `processes_num_running` - The number of running processes
	* `processes_num_sleeping` - The number of sleeping processes
	* `processes_num_stopped` - The number of stopped processes
	* `processes_num_zombie` - The number of zombie processes
* `processor_name` - The human-readable processor name
* `processor_num_real_cores` - The number of real processor cores
* `processor_num_virt_cores` - The number of virtual processor cores
* `processor_speed` - The nominal processor speed, in GHz
* `table_interrupt_data` - This key is written last, on its own line, and followed by the exact output of `cat /proc/interrupts`

Unusual/Interesting Behavoir
----------
All behavoir satisfies at least the minimum requirements specified in the assignment document. In addition to marking a host as unreachable, the user is informed of any SSH errors when running `alamode-sentry` so that they know exactly what went wrong. This is the only other output given besides the location of the saved information. The interrupts table is returned as-is, without any parsing done by the host - because honestly, it would be too much of a pain to parse it using `sed`/`awk`/etc. The table is diplayed in HTML exactly as it appears on the command line. There's a lot of extra logic in `alamode-publish` to handle edge cases not caught by Ruby's OptionParser module. If no input flag is given, the script defaults to `stdin`. Otherwise, the user must specify a directory to read from and the script exits if the directory does not exist. The generated HTML is always saved as `index.html` in the output directory. The resources used for styling and behavior (Bootstrap and jQuery) are included with the scripts. Each resource is referenced by its absolute path in the file system (as determined by Ruby's `File.expand_path` method) rather than its position relative to the HTML file, so all of the resources _must_ remain in the same directory as `alamode-publish`. When viewing the final result, the color of each hostname is styled to indicate its "rating"; light gray if unreachable, green if good, yellow if somewhat burdened, and red if extremely busy. The overall CPU and memory usage are displayed using progress bars, with the option to click on the row to show/hide details. The number and types of processes are shown using stacked progress bars, color-coded and with a mouseover tooltip to display which one is which. Clicking the row shows/hides the exact numbers of each.

Time
----------
I would guess that it took somewhere around 5 to 7 hours to get `alamode-sentry` exactly how I wanted it. `alamode-publish` probably didn't take more than 4 or 5 hours, most of which was figuring out command-line arguments, and then I spent a whole afternoon with styling and behavior just for fun.