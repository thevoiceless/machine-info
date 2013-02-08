#!/usr/bin/python

# Number of users: users | wc -w

# Number of processes: ps -A --no-headers | wc -l
# 	Running: ps axo state | grep R | wc -l
# 	Sleeping: ps axo state | grep S | wc -l
# 	Stopped: ps axo state | grep T | wc -l
# 	Zombie: ps axo state | grep Z | wc -l

# Processor:
#	Name: cat /proc/cpuinfo | grep "model name" | uniq
#	Speed (Hz): cat /sys/devices/system/cpu/cpu*/cpufreq/cpuinfo_max_freq | uniq
#	Number of real cores: cat /proc/cpuinfo | grep "cpu cores" | uniq | awk '{print $4}'
#	Number of virtual cores: cat /proc/cpuinfo | grep "^processor" | wc -l
#	Avg. load for the last...
#		1 min: uptime | awk '{print $10}' | sed s/,//
#		5 min: uptime | awk '{print $11}' | sed s/,//
#		15 min: uptime | awk '{print $12}' | sed s/,//

# Current utilization: top -b -n 1 | grep ^Cpu
#	Bonus - Show details for each core, run "top" and then press 1

# Cache:
#	Number of levels: ls /sys/devices/system/cpu/cpu0/cache/ | wc -w
#		Each line is a level, in increasing order:
#			Type: cat /sys/devices/system/cpu/cpu0/cache/index*/type
#			Size: cat /sys/devices/system/cpu/cpu0/cache/index*/size

# Memory: cat /proc/meminfo
#	Total: cat /proc/meminfo | grep MemTotal | awk '{print $2 " " $3}'
#	Free: cat /proc/meminfo | grep MemFree | awk '{print $2 " " $3}'

# Interrupts: cat /proc/interrupts

import argparse
import subprocess
import os

# SSH username
SSH_HOSTNAME_PREFIX = "rimoses@"
# Dictionary mapping a key to one or more commands
# The keys aren't really necessary, but they help to explain the purpose of their corresponding commands
INFO_COMMANDS = {
	'num_users': "echo num_users=`users | wc -w`;",
	'processes_total': "echo processes_total=`ps -A --no-headers | wc -l`;",
	'processes_num_running': "ps axo state | grep R | wc -l | awk '{print \"processes_num_running=\" $1}';",
	'processes_num_sleeping': "ps axo state | grep S | wc -l | awk '{print \"processes_num_sleeping=\" $1}';",
	'processes_num_stopped': "ps axo state | grep T | wc -l | awk '{print \"processes_num_stopped=\" $1}';",
	'processes_num_zombie': "ps axo state | grep Z | wc -l | awk '{print \"processes_num_zombie=\" $1}';",
	'processor_name': "echo processor_name=`cat /proc/cpuinfo | grep \"model name\" | uniq | sed s/^.*:\ *//`;",
	'processor_speed': "echo processor_speed=`cat /sys/devices/system/cpu/cpu*/cpufreq/cpuinfo_max_freq | uniq | awk '{print $1/1000000 }'` GHz;",
	'processor_num_real_cores': "echo processor_num_real_cores=`cat /proc/cpuinfo | grep \"cpu cores\" | uniq | awk '{print $4}'`;",
	'processor_num_virt_cores': "echo processor_num_virt_cores=`cat /proc/cpuinfo | grep \"^processor\" | wc -l`;",
	'load_avg_01min': "echo load_avg_01min=`uptime | awk '{print $10}' | sed s/,//`;",
	'load_avg_05min': "echo load_avg_05min=`uptime | awk '{print $11}' | sed s/,//`;",
	'load_avg_15min': "echo load_avg_15min=`uptime | awk '{print $12}' | sed s/,//`;",
	'cpu_utilization': "echo cpu_utilization=`top -b -n 1 | grep ^Cpu | sed s/^.*:\ *//`;",
	'cache_types': "let levels=`ls /sys/devices/system/cpu/cpu0/cache/ | wc -w`; for ((l=0; l<$levels; l++)); do let n=$l+1; echo \"lvl${n}_cache_type=`cat /sys/devices/system/cpu/cpu0/cache/index${l}/type | sed s/K/\ kB/`\"; done;",
	'cache_sizes': "let levels=`ls /sys/devices/system/cpu/cpu0/cache/ | wc -w`; for ((l=0; l<$levels; l++)); do let n=$l+1; echo \"lvl${n}_cache_size=`cat /sys/devices/system/cpu/cpu0/cache/index${l}/size | sed s/K/\ kB/`\"; done;",
	'memory_total': "cat /proc/meminfo | grep MemTotal | awk '{print \"memory_total=\" $2 " " $3}' | sed s/kB/\ kB/;",
	'memory_free': "cat /proc/meminfo | grep MemFree | awk '{print \"memory_free=\" $2 " " $3}' | sed s/kB/\ kB/;",
	'interrupt_data': "echo --START_INTERRUPT_TABLE--; cat /proc/interrupts; echo --END_INTERRUPT_TABLE--;" }

# Verify that the directory exists, create it otherwise
def verifyInfoDir(infoDir):
	if not os.path.exists(infoDir):
		os.makedirs(infoDir)
	return infoDir

# Convert the gathered data into a more readable form
def generateOutputFile(hostname, info, infoDir):
	with open(infoDir + "/" + hostname, "w") as hostInfoFile:
		for key in sorted(info.iterkeys()):
			hostInfoFile.write("{:<30}{}".format(key, info[key]))

# Parse the gathered information, save it in a dictionary, sort it
def organizeData(data):
	info = {}
	lines = data.splitlines(True)
	skipline = False
	for line in lines:
		if line == "--START_INTERRUPT_TABLE--\n":
			skipline = True
		elif line == "--END_INTERRUPT_TABLE--\n":
			skipline = False
			continue
		if not skipline:
			splitInfo = line.split("=")
			info[splitInfo[0]] = splitInfo[1]
	return info

# Get info about the given host
def getInfo(hostname, infoDir):
	command = "ssh {}".format(SSH_HOSTNAME_PREFIX + hostname).split(" ")
	for info, infoCommand in INFO_COMMANDS.iteritems():
		command.append(infoCommand)
	dataProcess = subprocess.Popen(command, stdout=subprocess.PIPE)
	data = dataProcess.communicate()[0]
	if dataProcess.returncode == 0:
		generateOutputFile(hostname, organizeData(data), infoDir)
	else:
		exit(dataProcess.returncode)

# Command-line arguments
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-n", metavar="HOSTNAME", help="the hostname from which to retrieve information")
group.add_argument("-f", metavar="FILENAME", help="a file containing a list of hostnames to use")
parser.add_argument("-d", metavar="DIRECTORY", help="save the data in the specified directory")
args = parser.parse_args()

# Save info in user-specified directory, if given
if args.d:
	infoDir = verifyInfoDir(args.d)
# Otherwise, use 'mktemp -d' to create a temporary directory
else:
	mktemp = subprocess.Popen(['mktemp', '-d'], stdout=subprocess.PIPE)
	if mktemp.wait() == 0:
		infoDir = mktemp.communicate()[0].strip()
	else:
		print "Error creating temporary directory: {}".format(mktemp.communicate()[1].strip())
		exit(1)

# Either use the host given as a command-line parameter...
if args.n:
	getInfo(args.n, infoDir)
# ...Or read the hosts from the given file
else:
	with open(args.f, "r") as hostsInputFile:
		hosts = hostsInputFile.read().splitlines()
		for host in hosts:
			getInfo(host, infoDir)

print os.path.realpath(infoDir)
print "TODO:\nInterrupts table"