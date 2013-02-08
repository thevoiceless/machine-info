#!/usr/bin/python

# Number of users: users | wc -w

# Number of processes: ps -A --no-headers | wc -l
# 	Running: ps axo state | grep R | wc -l
# 	Sleeping: ps axo state | grep S | wc -l
# 	Stopped: ps axo state | grep T | wc -l
# 	Zombie: ps axo state | grep Z | wc -l

# Processor:
#	Name: cat /proc/cpuinfo | grep "model name" | uniq
#	Speed: cat /sys/devices/system/cpu/cpu*/cpufreq/cpuinfo_max_freq | uniq
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

# Constants for SSH and commands to be executed
SSH_HOSTNAME_PREFIX = "rimoses@"
COMMAND_NUM_USERS = "users | wc -w;"

# Directory in which to save info
infoDir = ""

# Get info about the given host
def getInfo(hostname):
	with open(hostname, "w") as hostInfoFile:
		command = "ssh {}".format(SSH_HOSTNAME_PREFIX + hostname).split(" ")
		command.append(COMMAND_NUM_USERS)
		print command
		# p = subprocess.Popen(command)
		hostInfoFile.write(subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0])

# Command-line arguments
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-n", metavar="HOSTNAME", help="the hostname from which to retrieve information")
group.add_argument("-f", metavar="FILENAME", help="a file containing a list of hostnames to use")
parser.add_argument("-d", metavar="DIRECTORY", help="save the data in the specified directory")
args = parser.parse_args()

# Save info in user-specified directory, if given
if args.d:
	print "Save results in directory", args.d
	infoDir = args.d
# Otherwise, use 'mktemp -d' to create a temporary directory
else:
	mktemp = subprocess.Popen(['mktemp', '-d'], stdout=subprocess.PIPE)
	if mktemp.wait() == 0:
		infoDir = mktemp.communicate()[0].strip()
		print "Save results in {}".format(infoDir)
	else:
		print "Error creating temporary directory: {}".format(mktemp.communicate()[1].strip())
		exit(1)

# Either use the host given as a command-line parameter...
if args.n:
	print "Host given as argument:", args.n
	getInfo(args.n)
# Or read the hosts from the given file
else:
	print "Read hosts from {}:".format(args.f)
	with open(args.f, "r") as hostsInputFile:
		hosts = hostsInputFile.read().splitlines()
		for host in hosts:
			print host
			getInfo(host)


