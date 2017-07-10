#!/usr/bin/python
#coding=utf-8

import random

a = random.uniform(1, 5)
print "a =",a

b = random.randint(10, 50)
print "b =",b

c = random.randrange(0, 51, 2)
print "c =",c


def test():
    print '----哈哈----'
    print '----这是我的第一个函数----'


test()


#双引号或者单引号中的数据，就是字符串

name = 'abcdef'

print(name[0])
print(name[1])
print(name[2])

name = 'abcdef'

print(name[0:3]) # 取 下标0~2 的字符

name = 'abcdef'

print(name[3:5]) # 取 下标为3、4 的字符

name = 'abcdef'

print(name[2:]) # 取 下标为2开始到最后的字符

name = 'abcdef'

print(name[1:-1]) # 取 下标为1开始 到 最后第2个  之间的字符

'''
1。如有字符串mystr = 'hello world itcast and itcastcpp'，以下是常见的操作

<1>find
检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1

mystr.find(str, start=0, end=len(mystr))

返回 str在start和end之间 在 mystr里面出现的次数

2。mystr.count(str, start=0, end=len(mystr))

把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.

mystr.replace(str1, str2,  mystr.count(str1))

3。以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串

mystr.split(str=" ", 2)    切片成list

4。把字符串的第一个字符大写

mystr.capitalize()

5。检查字符串是否是以 obj 开头, 是则返回 True，否则返回 False

mystr.startswith(obj)

6。检查字符串是否以obj结束，如果是返回True,否则返回 False.

mystr.endswith(obj)

7。转换 mystr 中所有大写字符为小写

mystr.lower()       mystr.upper()

8。去空格等剧中等参见文档

9。按照行分隔，返回一个包含各行作为元素的列表

mystr.splitlines()

10。如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False

mystr.isalnum()

11。如果 mystr 所有字符都是字母 则返回 True,否则返回 False

mystr.isalpha()

12。mystr 中每个字符后面插入str,构造出一个新的字符串

mystr.join(str)

'''

#列表
A = ['xiaoWang','xiaoZhang','xiaoHua']
print A[0]
print A[1]
print A[2]

A = ['xiaoWang','xiaoZhang','xiaoHua']
for tempName in A:
        print tempName

#定义变量A，默认有3个元素
A = ['xiaoWang','xiaoZhang','xiaoHua']

print "-----添加之前，列表A的数据-----"
for tempName in A:
    print tempName

#提示、并添加元素
temp = raw_input('请输入要添加的学生姓名:')
A.append(temp)

print "-----添加之后，列表A的数据-----"
for tempName in A:
    print tempName


#定义变量A，默认有3个元素
A = ['xiaoWang','xiaoZhang','xiaoHua']

print "-----修改之前，列表A的数据-----"
for tempName in A:
    print tempName

#修改元素
A[1] = 'xiaoLu'

print "-----修改之后，列表A的数据-----"
for tempName in A:
    print tempName

#待查找的列表
nameList = ['xiaoWang','xiaoZhang','xiaoHua']

#获取用户要查找的名字
findName = raw_input('请输入要查找的姓名:')

#查找是否存在
if findName in nameList:
    print '在字典中找到了相同的名字'
else:
    print '没有找到'

movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']

print '------删除之前------'
for tempName in movieName:
    print tempName

del movieName[2]

print '------删除之后------'
for tempName in movieName:
    print tempName

movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']

print '------删除之前------'
for tempName in movieName:
    print tempName

movieName.pop()

print '------删除之后------'
for tempName in movieName:
    print tempName

movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']

print '------删除之前------'
for tempName in movieName:
    print tempName

movieName.remove('指环王')

print '------删除之后------'
for tempName in movieName:
    print tempName