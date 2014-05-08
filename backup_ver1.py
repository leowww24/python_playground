#!/usr/bin/env python
import os
import time
source=['~/code/c++','/home/leo/code/c']
target_dir='~/code/'
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'
command='zip -r %s %s'%(target,' '.join(source))
if os.system(command)==0:
	print 'Success backup to',target
else:
	print 'Backup failed.'
