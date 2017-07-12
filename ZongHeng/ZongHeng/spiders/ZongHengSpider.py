# -*- coding:utf-8 -*-

import re
import scrapy
from bs4 import  BeautifulSoup
from  scrapy.http import Request
from ZongHeng.items import  ZonghengItem
from ZongHeng.items import DcontentItem
import sys

reload(sys)
sys.setdefaultencoding('utf8')

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
            nameSpan = li.find('span',class_ = 'chap');
            if nameSpan:
                novelName = nameSpan.find_all('a', class_='fs14')[0].get_text()
                novelurl = nameSpan.find_all('a', class_='fs14')[0]['href']
            authorSpan = li.find('span', class_='author')

            if authorSpan:
                novelAuthor = authorSpan.find_all('a')[0].get_text()
            kindSpan = li.find('span', class_='kind')
            if kindSpan:
                novelKind = kindSpan.find_all('a')[0].get_text()
            countSpan = li.find('span', class_='number')
            if countSpan:
                count = countSpan.get_text().replace("\n", "").strip()

            if nameSpan and authorSpan and kindSpan:

                # print novelName+'*'+novelurl+'*'+novelAuthor+'*'+novelKind+'*'+str(count)
                # print '**'
                # print count
                # print '**'
                yield Request(novelurl,callback=self.get_chapterUrl,meta={'name':novelName,'url':novelurl,'author':novelAuthor,'kind':novelKind,'count':count})

    def get_chapterUrl(self,response):


        item = ZonghengItem()
        item['name'] = str(response.meta['name']).replace('\n','').strip()
        item['novelurl'] = str(response.meta['url'])
        item['author'] = str(response.meta['author'])
        item['category'] = str(response.meta['kind'])
        item['count'] = str(response.meta['count'])
        name_id = BeautifulSoup(response.text, 'lxml').find('body')['bookid']
        item['name_id'] = name_id

        contentsText = BeautifulSoup(response.text, 'lxml').find('a',class_ = 'btn_dl')
        contentsUrl = None
        if contentsText:
            contentsUrl = contentsText['href']


        if contentsUrl:
            # return item
            # print '***'
            # print contentsUrl
            # print '***'
            yield item
            yield Request(url=contentsUrl,callback=self.get_chapter,meta={'name_id':name_id})


    def get_chapter(self,response):

        # print '-----'
        # print  response.url
        # print '-----'
        urls = re.findall(r'<td class="chapterBean".*?><a href="(.*?)".*?>(.*?)</a></td>',response.text)
        # print  urls
        num = 0
        for url in urls:
            num = num +1
            chapterurl = str(url[0])
            chaptername = str(url[1])
            yield Request(chapterurl,callback=self.get_chaptercontent,meta={'num':str(num),'name_id':response.meta['name_id'],'chaptername':chaptername,'chapterurl':chapterurl})

        pass

    def get_chaptercontent(self,response):

        item = DcontentItem()
        item['num'] = response.meta['num'];
        item['name_id'] = response.meta['name_id']
        item['chaptername'] = str(response.meta['chaptername'])
        item['chapterurl'] = str(response.meta['chapterurl'])
        content = BeautifulSoup(response.text,'lxml').find('div',id="readerFs")
        item['chaptercontent'] = str(content)
        # print content

        yield item

        pass


