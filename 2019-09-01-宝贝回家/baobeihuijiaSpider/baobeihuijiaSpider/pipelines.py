# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class BaobeihuijiaspiderPipeline(object):

    def __init__(self):
        self.f = open('baobeihuijia.csv', 'a', encoding='utf-8', newline='\n')
        self.csv_writer = csv.writer(self.f) # dialect='excel' 指定换行符-->\r\n

    def process_item(self, item, spider):

        self.csv_writer.writerow(item.get('data'))

        return item

    def close_spider(self, spider):
        self.f.close()

class BaobeihuijiaspiderPipeline2(object):

    def __init__(self):
        self.f = open('baobeihuijia2.csv', 'a', encoding='utf-8', newline='\n')
        self.csv_writer = csv.writer(self.f) # dialect='excel' 指定换行符-->\r\n

    def process_item(self, item, spider):

        self.csv_writer.writerow(item.get('data'))

        return item

    def close_spider(self, spider):
        self.f.close()