# !/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import os
from bs4 import BeautifulSoup
import json
import ssl


def getProxyList():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
    url = 'http://www.xicidaili.com/nn/1'
    s = requests.get(url, headers=headers)
    # print  s.text
    soup = BeautifulSoup(s.text, "html.parser")
    ips = soup.findAll('tr')
    fp = open('host.txt', 'w')

    print len(ips)
    print ips[1]
    tds = ips[1].findAll("td")
    print tds
    print len(tds)
    print tds[1]
    print tds[2]
    print tds[2].contents[0]

    for tmp in ips:
        try:
            tds = tmp.findAll("td")
            ip_temp = tds[1].contents[0] + "\t" + tds[2].contents[0] + "\n"
            print  ip_temp
            fp.write(ip_temp)

        except Exception as e:
            print ('no ip !')

    fp.close()

def testProxy():

    url = 'http://www.ip138.com/'
    fp = open('./host.txt', 'r')
    fp2 = open('./successHost.txt', 'w')
    ips = fp.readlines()
    proxys = list()
    for p in ips:
        ip = p.strip('\n').split('\t')
        proxy = 'http:\\' + ip[0] + ':' + ip[1]
        proxies = {'proxy': proxy}
        proxys.append(proxies)
    for pro in proxys:
        try:

            s = requests.get(url, proxies=pro)
            print pro
            print s
            if str(s) =="<Response [200]>":
                print pro["proxy"]
                fp2.write(str(pro["proxy"][6:])+ "\n")

        except Exception as e:
            print (e)
    fp.close()
    fp2.close()



if __name__ == "__main__":

    #获取ip信息写入文件
    # getProxyList()
    #测试获得ip是否可用并写入文件
    testProxy()