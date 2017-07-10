#!/usr/bin/python
#coding=utf-8

try:
    print ''
    open('12345.txt','r')

except IOError:
    print 'get it'
    pass

else:
    print 'ok'

finally:

    print 'over'