#coding=utf-8
#!/usr/bin/python


def printf():
    print  '类ddddddd'

class Car:

    #init方法最开始初始化默认调用，生成属性
    def __init__(self):
        self.wheelNum = 4
        self.color = '蓝色'

    #定义方法
    def getCarInfo(self):
        print '车子信息'




bmw = Car()#实例话
bmw.color = '黑色'#添加属性
bmw.getCarInfo()#调用方法


class BigCar:
    # init方法最开始初始化默认调用 带参数，生成属性
    def __init__(self,newWheelNum,NewColor):
        self.wheelNum = newWheelNum
        self.color = NewColor

    # 定义方法
    def getCarInfo(self):
        print '车子信息'

    def __str__(self):
        msg = "嘿，我是车子颜色是"+self.color+"我有"+str(self.wheelNum)+'个轮子'
        return msg

    #类方法用这个标识
    @classmethod
    def getCountry(cls):
        print '类方法被调用'

    def __del__(self):
        print  'over'


bmw = BigCar(4,'green')  # 实例化，调用的时候self默认参数不用添加
print ('车子颜色为：%s'%bmw.color)
print ('车子颜色为：%d'%bmw.wheelNum)

#根据__str__的返回值确定，否则直接打印地址
print bmw
bmw.getCountry()
BigCar.getCountry()

del  bmw
