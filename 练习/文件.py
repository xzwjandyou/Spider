#!/usr/bin/python
#coding=utf-8
f = open('test.txt','r')
#f.write('hello')

#content = f.read(3)
content = f.readline()
print(type(content))
print content
f.close()