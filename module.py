#-*-coding:utf-8-*-
#模块通过将文件名命名为.py实现
#模块被调用后会生成同名的.pyc二进制文件
if __name__=='__main__':
	print 'this module is being used by intself'
else:
	print 'this module has been imported.'
