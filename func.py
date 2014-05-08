#!/usr/bin/env python
def func(x):
	'''This is the docstrings.

	the descriptions of the func is here...'''
	print 'your x is:',x
	x=32;
	print 'the x inside func is:',x

func(3)
print func.__doc__
