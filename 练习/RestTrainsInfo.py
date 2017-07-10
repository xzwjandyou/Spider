# !/usr/bin/python
# -*- coding:utf-8 -*-

#匿名代理多进程

import ssl
import sys
import urllib2
import random
import httplib
import json
from cookielib import LWPCookieJar
import urllib
import re
import getpass
from datetime import *
import time
import logging
import string
import multiprocessing
import os
import signal
from multiprocessing import Process, Semaphore, Lock, Queue
# import logging

reload(sys)
sys.setdefaultencoding('UTF8')

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)

ssl._create_default_https_context = ssl._create_unverified_context

#打开代理ip列表
fp = open('./successHost.txt', 'r')
ips = fp.readlines()

# proxies={"http":"175.155.225.90:8118"}   #设置你想要使用的代理
# proxy_s=urllib2.ProxyHandler(proxies)
# opener=urllib2.build_opener(proxy_s)
# urllib2.install_opener(opener)
# content=urllib2.urlopen('http://ip.chinaz.com/').read()#读取指定网站的内容
# print content

trainsList = []
buffer = Queue(10)


def get(url):
    try:
        #每次从列表中随机选择ip
        ip = random.choice(ips)
        print  ip
        # logging.debug('代理ip：' + str(ip))
        proxies = {"http": ip}
        proxy_s = urllib2.ProxyHandler(proxies)
        opener = urllib2.build_opener(proxy_s)
        urllib2.install_opener(opener)

        request = urllib2.Request(url=url)
        request.add_header("Content-Type", "application/x-www-form-urlencoded; charset=utf-8")
        request.add_header('X-Requested-With', 'xmlHttpRequest')
        request.add_header('User-Agent',
                           'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
        request.add_header('Referer', 'https://kyfw.12306.cn/otn/login/init')
        request.add_header('Accept', '*/*')
        result = urllib2.urlopen(request).read()
        print '列车信息请求'
        assert isinstance(result,object)
        return  result
    except httplib.error as e:
        print e
        pass
    except urllib2.URLError as e:
        print e
        pass
    except urllib2.HTTPBasicAuthHandler, urllib2.HTTPError:
        print 'error'
        pass

def getResultOfQueryRequest(trainDate, From_city, To_city):

    f = open('./CityCode/CityCode.txt', 'r')
    content = f.read()
    global City_Code
    City_Code = eval(content)

    try:
        try:
            bagful = "https://kyfw.12306.cn/otn/leftTicket/query?" \
                     "leftTicketDTO.train_date={0}&" \
                     "leftTicketDTO.from_station={1}&" \
                     "leftTicketDTO.to_station={2}" \
                     "&purpose_codes=ADULT" \
                     "".format(trainDate, City_Code[From_city], City_Code[To_city])
        except KeyError:
            print "无法找到的站点"
            return False
        except NameError:
            print "无法找到输入的站点"
            return False

        global restTrainsResult
        data = get(bagful)

        restTrainsResult = json.loads(data, encoding='UTF-8')
        # print restTrainsResult
        # return restTrainsResult
        global trainsList
        trainsList = []
        list = restTrainsResult['data']['result']
        for item in list:
            item = item.split('|')
            # print 'item:::::::'+item[1]
            if cmp(item[1], '预订') == 0 and len(item[0]) > 0 and item[11] == 'Y':
                queryLeftNewDTO = {
                    "station_train_code": item[3],  # 车次
                    "from_station_name": "",  # 出发站
                    "to_station_name": "",  # 到达站
                    "start_time": item[8],  # 出发时间
                    "arrive_time": item[9],  # 到达时间
                    "lishi": item[10],  # 历时
                    "leftTicket": item[12],
                    "train_date": item[13],  # 出发日期
                    "train_location": item[15],  # 出发日期
                    "gjrz_num": str(item[21]),  # 高级软座
                    "rw_num": str(item[23]),  # 软卧
                    "rz_num": item[24],  # 软座
                    "tz_num": item[25],  # 特等座
                    "wz_num": item[27],  # 无座
                    "yw_num": item[28],  # 硬卧
                    "yz_num": item[29],  # 硬座
                    "ze_num": item[30],  # 二等座
                    "zy_num": item[31],  # 一等座
                    "swz_num": item[32],  # 商务座
                    "train_no": item[2],
                    "seat_types": [str(item[34])[i:i + 1] for i in xrange(0, len(str(item[34])), 1)],  # 可购买座位
                    "from_station_no": item[6],
                    "to_station_no": item[7],
                    "secretStr": urllib.unquote(item[0]),
                }
                # print urllib.unquote(item[0])
                list = ['Z112']
                if queryLeftNewDTO['station_train_code'] in list:
                    trainsList.append(queryLeftNewDTO)

        if len(trainsList) > 0:
            print ('有可以%d辆可以订购的火车' % (len(trainsList)))
            # print trainsList
            global buffer
            buffer.put(trainsList)
            # return trainsList

        else:
            print '暂无可购买车票'

    except urllib2.HTTPError as alter:
        print "错误: [%s]!" % alter
        return None
        pass
    except KeyError:
        print "找不到key"
        return None
    except NameError:
        print "无效变量"
        return None

def onsignal_term(a,b):
    # print '收到SIGTERM信号'
    pass

signal.signal(signal.SIGUSR1,onsignal_term)

def multiprocessGetTrainsInfo(trainDate, From_city, To_city):

    startTime = datetime.now()
    #先启动8个进程
    for i in range(4):
        p = multiprocessing.Process(target=getResultOfQueryRequest, args=(trainDate,From_city,To_city))
        # p.daemon = True
        p.start()
        # p.terminate()
    trainsList = []
    while(1):
        if not buffer.empty():
            trainsList = buffer.get()
            if len(trainsList)>0:
                childrenList = multiprocessing.active_children()
                for p in childrenList:
                    print('Child process name: ' + p.name + ' id: ' + str(p.pid))
                    os.kill(p.pid, signal.SIGUSR1)
                    p.terminate()

                break
        else:
            pass
            endTime = datetime.now()
            if (endTime-startTime).seconds>5:
                print  (endTime-startTime).seconds
                break

        # print "-"


    # childrenList = multiprocessing.active_children()
    # for p in childrenList:
    #     print('Child process name: ' + p.name + ' id: ' + str(p.pid))
    #     os.kill(p.pid, signal.SIGUSR1)
    #     p.terminate()

    # time.sleep(0.1)
    print multiprocessing.active_children()

    return trainsList


    # print('CPU number:' + str(multiprocessing.cpu_count()))
    # for p in multiprocessing.active_children():
    #     print('Child process name: ' + p.name + ' id: ' + str(p.pid))
    #     os.kill(p.pid, signal.SIGUSR1)

    # print('Process Ended')



if __name__ == "__main__":

    # print getResultOfQueryRequest('2017-06-14','深圳','上海')

    list = multiprocessGetTrainsInfo('2017-06-14','深圳','上海')
    print  list


    fp.close()

