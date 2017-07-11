# -*- coding:utf-8 -*-

import re
import scrapy
from bs4 import  BeautifulSoup
from  scrapy.http import Request
from ZongHeng.items import  ZonghengItem

class MySpider(scrapy.Spider):

    name = 'ZongHeng'#名称需与前面执行的命令中同名

    baseUrl = 'http://book.zongheng.com/quanben/'
    endUrl = '/v9/s1/t0/ALL.html'
    list = ['c0','c1','c3','c6','c9','c15','c18','c21','c24']

    def start_requests(self):
        for str in self.list:
            url = self.baseUrl +str+'/c0/b0/u0/p1'+self.endUrl
            yield  Request(url,self.parse)


    def parse(self, response):

        #获取最大页码
        max_num = BeautifulSoup(response.text, 'lxml').find('div', class_='pagenumber pagebar').find_all('a')[-2].get_text()
        print  max_num

        # print (response.text)
        for num in range(1, int(max_num) + 1):
            page = 'p' + str(num)
            url = str(response.url).replace('p1', page)
            print url
            yield Request(url,callback = self.get_name)

    def get_name(self,response):

        li_s = BeautifulSoup(response.text, 'lxml').find('ul',class_ = 'main_con').find_all('li')

        for li in li_s:
            span = li.find('span',class_ = 'chap');
            if span:
                novelName = span.find_all('a', class_='fs14')[0].get_text()
                novelurl = span.find_all('a', class_='fs14')[0]['href']
                print '----'
                print novelName + novelurl
                print '----'

                yield Request(novelurl,callback=self.get_chapterUrl,meta={'name':novelName,'url':novelurl})


    def get_chapterUrl(self,response):


        pass