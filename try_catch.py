#!/usr/bin/env python
try:	
	name=raw_input("input the file name:")
	file=open(name,'r')
	for i in file:
		print i
except IOError,e:
	print "cannot open file.",e
