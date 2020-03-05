# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter


class KagglespiderPipeline(object):

    def __init__(self):
        self.f = open('kaggle.csv','a')
        #self.exporter = CsvItemExporter(self.f)
        #self.exporter.start_exporting()

    def process_item(self, item, spider):
        #self.exporter.export_item(item)
        self.f.write(item['allItem']+'\n')
        return item

    def close_spider(self, spider):
        #self.exporter.finish_exporting()
        self.f.close()