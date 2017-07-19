# -*- coding:utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule, Request ##CrawlSpider与Rule配合使用可以骑到历遍全站的作用、Request干啥的我就不解释了
from scrapy.linkextractors import LinkExtractor ##配合Rule进行URL规则匹配
from scrapy import FormRequest ##Scrapy中用作登录使用的一个包
from tapdLogin.items import TapdloginItem
import scrapy

import sys

reload(sys)
sys.setdefaultencoding('utf8')

account = '573068185@qq.com'
password = 't12345zq'

#哈哈哈哈哈   cookie自动保存来着，在setting里的COOKIES_ENABLED设置中

class myspider(scrapy.Spider):

    name = 'tapdlogin'
    allowed_domains = ['tapd.cn']
    # start_urls = ['https://www.tapd.cn/cloud_logins/login?']

    def start_requests(self):
        return [scrapy.FormRequest('https://www.tapd.cn/cloud_logins/login?',
                                   formdata={
        'data[Login][ref]': 'https://www.tapd.cn/my_worktable',
        'data[Login][encrypt_key]': 'uBLeVlP3b6r8bf85dY63lHEfPDVd8RT/o3O3pZwPhyQ=',
        'data[Login][encrypt_iv]': "kR4zFCY9ODN/HgvsX7/yzQ==",
        'data[Login][site]': "TAPD",
        'data[Login][via]': "encrypt_password",
        'data[Login][email]': "573068185@qq.com",
        'data[Login][password]': "B4of7jJZDqi7ugZvck7eYA==",
        'data[Login][login]': "login",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '423',
        'Referer': 'https://www.tapd.cn/cloud_logins/login?',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'

    },
                                   callback=self.after_login)]

    # def parse_start_url(self, response):
    #     ###
    #     #如果你登录的有验证码之类的，你就可以在此处加入各种处理方法；
    #     #比如提交给打码平台，或者自己手动输入、再或者pil处理之类的
    #     formdate = {
    #         'data[Login][ref]': 'https://www.tapd.cn/my_worktable',
    #         'data[Login][encrypt_key]': 'uBLeVlP3b6r8bf85dY63lHEfPDVd8RT/o3O3pZwPhyQ=',
    #         'data[Login][encrypt_iv]': "kR4zFCY9ODN/HgvsX7/yzQ==",
    #         'data[Login][site]': "TAPD",
    #         'data[Login][via]': "encrypt_password",
    #         'data[Login][email]': "573068185@qq.com",
    #         'data[Login][password]': "B4of7jJZDqi7ugZvck7eYA==",
    #         'data[Login][login]': "login",
    #         'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0',
    #         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #         'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    #         'Accept-Encoding':'gzip, deflate, br',
    #         'Content-Type':'application/x-www-form-urlencoded',
    #         'Content-Length':'423',
    #         'Referer':'https://www.tapd.cn/cloud_logins/login?',
    #         'Connection':'keep-alive',
    #         'Upgrade-Insecure-Requests':'1'
    #
    #     }
    #     return [FormRequest.from_response(response, formdata=formdate, callback=self.after_login)]


    def after_login(self, response):
        ###
        #可以在此处加上判断来确认是否登录成功、进行其他动作。

        # print  response.text
        lnk = 'https://www.tapd.cn/20055091/board/index?board_id=1120055091001000001'
        # return Request(lnk)

        Cookie = response.request.headers.getlist('Cookie')
        print '------'
        print Cookie
        print '------'
        yield Request(lnk,callback= self.parse_item)

    # rules = (
    #     Rule(LinkExtractor(allow=('board_id=1120055091001000001',)), callback='parse_item', follow=True),
    # )

    def parse_item(self, response):
        # tapdloginItem = TapdloginItem()
        # print response.meta['cookie']
        print '**'
        print response.text
        print '**'
        # return tapdloginItem