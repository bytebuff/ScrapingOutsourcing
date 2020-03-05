# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class EastmoneyspiderPipeline(object):

    def __init__(self):
        self.f = open('东方财富-山东.csv', 'a', encoding='utf-8', newline='')
        self.csvWriter = csv.writer(self.f)
        self.header = [
            '公司名字',
            '年度',
            '期间费用',
            '财务费用',
            '销售费用',
            '管理费用',
            '营业收入'
        ]
        self.csvWriter.writerow(self.header)

    def process_item(self, item, spider):
        data = [
            item.get('companyName', ''),
            item.get('date', ''),
            item.get('qjfy', ''),
            item.get('cwfy', ''),
            item.get('xsfy', ''),
            item.get('glfy', ''),
            item.get('yysr', ''),
        ]
        self.csvWriter.writerow(data)
        return item

    def close_spider(self, spider):
        self.f.close()
