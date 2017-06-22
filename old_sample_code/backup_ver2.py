#!/usr/bin/env python
import os
import time
source=['~/code/c++','/home/leo/code/c']
target_dir='/home/leo/code'  #must use /home/leo/ use ~/ is not allowed
today=target_dir+os.sep+time.strftime('%Y%m%d')
if not os.path.exists(today):
	os.mkdir(today)
	print 'Success created dictionary',today
now=time.strftime('%H%M%S')
comment=raw_input('Input comment:')
if len(comment)==0:
	target=today+os.sep+now+'.zip'
else:
	target=today+os.sep+now+comment.replace(' ','_')+'.zip'
command='zip -r %s %s'%(target,' '.join(source))
if os.system(command)==0:
	print 'Success backup to',target
else:
	print 'Backup failed.'
