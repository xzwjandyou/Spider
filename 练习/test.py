# !/usr/bin/python
# -*- coding:utf-8 -*-

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
import os
import codecs


ssl._create_default_https_context = ssl._create_unverified_context

City_Code = {}

dict = {}

def Get_City_code():
    print "读取站点数据库..."
    try:
        #read Code from .txt
        f = codecs.open('./CityCode/CityCode.txt', 'r','utf-8')
        content = f.read()
        global City_Code
        City_Code = eval(content)
        print City_Code
        print City_Code['北京']

        # download Code to .txt
        # Ci_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8994'
        # Ci_text = urllib2.urlopen(Ci_url).read()
        # Ci_text = Ci_text.replace('\'', '').replace('var station_names =\'', '')
        # city = re.findall('\|\W+\|[A-Z]{3}', Ci_text)
        # for i in city:
        #     City_Code[re.split('\|', i)[1]] = re.split('\|', i)[2]
        #
        # if os.path .exists("./CityCode/") ==True :
        #     pass
        # else:
        #     os.makedirs("./CityCode/")
        #     pass
        # f = open('./CityCode/CityCode.txt', 'w')
        # data_string = json.dumps(City_Code,'a',encoding='utf-8',ensure_ascii=False)
        # # print "dddddddddd"+data_string
        # f.write(data_string)
        # print "读取成功!\n输入h或help获取帮助"



    except urllib2.URLError as erron:
        print "错误:%s无法读取站点数据,请检查网络后重试!"%erron
        sys.exit()


Get_City_code()

print City_Code['北京']