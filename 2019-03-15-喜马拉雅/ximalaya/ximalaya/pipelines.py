# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class XimalayaPipeline(object):

    def __init__(self):
        self.f = open('mydata.txt', 'a', encoding='utf-8')

    def process_item(self, item, spider):

        item = dict(item)

        self.f.write(json.dumps(item, ensure_ascii=False)+'\n')

        return item

    def close_spider(self,spider):
        self.f.close()