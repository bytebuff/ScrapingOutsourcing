# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


CSVNAME = '西安大数据'

class JobspiderPipeline(object):

    def __init__(self):
        self.f = open(f'{CSVNAME}.csv', 'a', encoding='utf-8', newline='')
        self.csv_writer = csv.writer(self.f)

    def process_item(self, item, spider):

        self.csv_writer.writerow(item.get('data'))  # 里面传递的是列表

        return item

    def close_spider(self, spider):
        self.f.close()