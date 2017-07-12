# -*- coding:utf-8 -*-
from .sql import Sql
from  ZongHeng.items import ZonghengItem
from  ZongHeng.items import DcontentItem
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class ZongHengPipeline(object):

    def process_item(self,item,spider):
        if isinstance(item,ZonghengItem):
            name_id = item['name_id']
            ret = Sql.select_name(name_id)
            if ret[0] == 1:
                print ('已经存在了')

            else:
                name = item['name']
                author = item['author']
                # print item['category']
                # print item['author']
                category = item['category']
                Sql.insert_dd_name(name,author,name_id,category)
                print '存储小说列表'
        if isinstance(item,DcontentItem):
            url = item['chapterurl']
            name_id = item['name_id']
            num_id = item['num']
            zh_chaptername = item['chaptername']
            zh_content = item['chaptercontent']
            Sql.insert_dd_chaptername(zh_chaptername, zh_content, name_id, num_id, url)
            print('小说存储完毕')
            return item