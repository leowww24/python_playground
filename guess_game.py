#!/usr/bin/env python
g=True;
res=34
while g:
	s=raw_input('guess a number:')
	a=int(s)
	if a==res:
		print 'you make it!'
		g=False
	elif a<res:
		print 'small guess again:'
	elif a>res:
		print 'big guess again'
else:
	print 'the hole loop is over.'

	
