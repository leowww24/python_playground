#!/usr/bin/env python
#-*-coding:utf-8-*-
#括号中为继承的基类，默认使用object，注意后面 ：
#类中只能包含全局变量，之后是类方法
#所有的方法，及方法中定义的变量必须使用self标明指向对象自身
class myClass():
	version='1.0v'  #全局变量及类的变量，对象共享，但只有类可以引用,即只可以通过myClass.version引用，无论在类定义内部还是外部
	count=0;
	def __init__(self,nm='leo'):
		self.name=nm  #全局变量以外的变量可以直接通过self.引用   
		myClass.count+=1;  #注意全局变量引用必须使用类名
		print 'You\'ve created a instance',nm
		print "count is:",myClass.count
	def show(self):
		print 'your name is',self.name
		print 'my name is',self.__class__.__name__ #特殊变量 
	def double(self,x):
		print 'double x is:','%d' %(x+x)
	
	def __del__(self):  #__def__为析够函数
		print '\nI\'m dying....'
		myClass.count-=1
		print 'count is:%d now.'%(myClass.count)

mmm=raw_input("input your name:")
obj=myClass(mmm)
obj.show()
obj.double(6)
print myClass.version 
