#!/usr/bin/env python
#-*-coding:utf-8-*-
class person():
	def __init__(self,name,age):
		self.name=name
		self.age=age
		print 'person %s has been constructed.'%(self.name)
	def tell(self):
		print 'I\' %s \nmy age is %d'%(self.name,self.age),

class teacher(person):
	def __init__(self,name,age,salary):
		person.__init__(self,name,age) #注意：调用基类的构造函数或方法时需要显示使用基类名称调用，还必须定义self参数（self参数实现将实例名称传递给方法）
		self.salary=salary
		print 'teacher %s has been contructed.'%(self.name)
	def tell(self):
		person.tell(self)
		print 'my salary is %d'%(self.salary)

class student(person):
	def __init__(self,name,age,marks):
		person.__init__(self,name,age)
		self.marks=marks
		print 'student %s has been constructed.'%(self.name)
	def tell(self):
		person.tell(self)
		print 'my marks is %d'%(self.marks)

t=teacher('leo',24,8000)
s=student("Lucy",16,90)
school=[t,s]
for p in school:
	p.tell()
