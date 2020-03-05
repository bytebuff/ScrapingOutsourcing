# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re


class XiaozhuspiderPipeline(object):

    def __init__(self):
        self.f = open('xiaozhu.csv', 'a', encoding='utf-8')

    def process_item(self, item, spider):

        data = dict(item)
        data = re.sub('\n|\r', '', str(data['data']))

        self.f.write(data+'\n')

        return item

    def close_spider(self,spider):
        self.f.close()
