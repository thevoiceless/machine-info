#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-n", metavar="HOSTNAME", help="The hostname from which to retrieve information")
group.add_argument("-f", metavar="FILENAME", help="A file containing a list of hostnames to use")

parser.add_argument("-d", metavar="DIRECTORY", help="Save the data in the specified directory")

parser.parse_args()