# -*- coding:utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule, Request  ##CrawlSpider与Rule配合使用可以骑到历遍全站的作用、Request干啥的我就不解释了
from scrapy.linkextractors import LinkExtractor  ##配合Rule进行URL规则匹配
from tiantangBT.items import TiantangbtItem  ##不解释
from scrapy import FormRequest  ##Scrapy中用作登录使用的一个包
from lxml import html
import lxml.etree as etree
import lxml.html.soupparser as soupparser

import sys

reload(sys)
sys.setdefaultencoding('utf8')


class myspider(CrawlSpider):
    name = 'tiantangBT'
    allowed_domains = ['tiantangbt.com']
    start_urls = ['http://www.tiantangbt.com/']

    start_urls = [
        'http://www.tiantangbt.com/action/'
    ]

    # rules = (
    #     Rule(LinkExtractor(allow=(r'.*/action/.*',)), callback='parse_item', follow=True),
    # )
    rules = (
        Rule(LinkExtractor(allow=(r'action/index_[0-9]\.html',)), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)

        contentList = response.xpath('//*[@class="post-grid clearfix"]/div').extract()
        # print '**'
        # print contentList
        # print '**'
        for index, result in enumerate(contentList):
            item = TiantangbtItem()
            resultOK = html.fromstring(result)
            # print resultOK
            item['url'] = resultOK.xpath('//a[@class="entry-thumb lazyload"]/@href')
            item['title'] = resultOK.xpath('//h2[@class="entry-title"]/a//strong/text()')
            item['date'] = resultOK.xpath('//div[@class="entry-meta"]//span[@class="date"]/text()')
            # item['imgurl'] = result.xpath('//*[@class="post-grid clearfix"]/div').extract()
            print '**'
            # print resultOK
            print item['url']
            print item['title']
            print item['date']
            print '**'



        pass



