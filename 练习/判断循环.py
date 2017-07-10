#!/usr/bin/python
#coding=utf-8

age = 16

if age>=18:
    print '大了'
else:
    print '小了'

'''
if xxx1:
        事情1
    elif xxx2:
        事情2
    elif xxx3:
        事情3

'''
'''
i = 0
    while i<10000:
        print "媳妇儿，我错了"
        i+=1

'''
'''
while 条件:
        条件满足时，做的事情1
        条件满足时，做的事情2
        条件满足时，做的事情3
        ...(省略)...
'''

i = 0
while i<5:
        print "当前是第%d次执行循环"%(i+1)
        print "i=%d"%i
        i+=1

for i in range(10):
      print '----'
      if i == 3:
          break
      print i

for i in range(10):
      print '----'
      if i==3:
          continue
      print i