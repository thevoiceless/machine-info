#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-n", metavar="HOSTNAME", help="The hostname from which to retrieve information")
group.add_argument("-f", metavar="FILENAME", help="A file containing a list of hostnames to use")
parser.add_argument("-d", metavar="DIRECTORY", help="Save the data in the specified directory")
parser.parse_args()

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

