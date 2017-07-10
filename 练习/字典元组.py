#!/usr/bin/python
#coding=utf-8

info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}

print(info['name'])
print(info['address'])

info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}

newId = raw_input('请输入新的学号')

info['id'] = int(newId)

print('修改之后的id为%d:'%info['id'])

info = {'name':'班长', 'sex':'f', 'address':'地球亚洲中国北京'}

# print('id为:%d'%info['id'])#程序会终端运行，因为访问了不存在的键

newId = raw_input('请输入新的学号')

info['id'] = newId

print('添加之后的id为:%d'%info['id'])

info = {'name':'班长', 'sex':'f', 'address':'地球亚洲中国北京'}

print('删除前,%s'%info['name'])

del info['name']

print('删除后,%s'%info['name'])

#删除整个字典
info = {'name':'monitor', 'sex':'f', 'address':'China'}

print '删除前,',info

del info

print '删除后,',info

#清空
info = {'name':'monitor', 'sex':'f', 'address':'China'}

print '清空前,',info

info.clear()

print '清空后,',info

#元组  Python的元组与列表类似，不同之处在于元组的元素不能修改。也可进行分片 和 连接操作. 元组使用小括号，列表使用方括号。
aTuple = ('et',77,99.9)