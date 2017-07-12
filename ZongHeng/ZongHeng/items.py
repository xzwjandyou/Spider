# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZonghengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()

    author = scrapy.Field()

    novelurl = scrapy.Field()

    name_id = scrapy.Field()

    count =  scrapy.Field()

    category = scrapy.Field()



    pass

class DcontentItem(scrapy.Item):

    name = scrapy.Field()

    name_id = scrapy.Field()

    chaptercontent = scrapy.Field()

    num = scrapy.Field()

    chapterurl = scrapy.Field()

    chaptername = scrapy.Field()