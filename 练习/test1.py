from datetime import *
import time

# print 'date.max:', date.max
# print 'date.min:', date.min
# print 'date.today():', date.today()
# print 'date.fromtimestamp():', date.fromtimestamp(time.time())

print  date.today().strftime('%Y-%m-%d')


s2='20120216';
b=datetime.strptime(s2,'%Y%m%d')
print  b.strftime('%Y-%m-%d')