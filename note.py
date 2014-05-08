#!/usr/bin/python
#-*-coding:utf-8-*-
a=[1,2,3]
a.append(4)
while True:
	n=int(raw_input("input a index:")) #输入默认为str型，int()为类型转换函数
        # \ 为代码换行
	print a,'your index is:',n,"\n"	\
                'a[%d]=%d'%(n,a[n])
