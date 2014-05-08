def func():
	global gi
	print 'global gi:',gi
	gi=22
	print 'global gi now is:',gi

gi=77
func()
