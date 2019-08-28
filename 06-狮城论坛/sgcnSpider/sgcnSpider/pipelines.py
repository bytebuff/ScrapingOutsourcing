# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SgcnspiderPipeline(object):

    def __init__(self):
        self.f = open('sgcn.csv', 'a', encoding='utf-8')

    def process_item(self, item, spider):

        item = dict(item)

        self.f.write(item['data']+'\n')

        return item

    def close_spider(self, response):
        self.f.close()