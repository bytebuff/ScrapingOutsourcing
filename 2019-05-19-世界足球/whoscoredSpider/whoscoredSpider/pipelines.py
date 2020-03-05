# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from scrapy.exporters import JsonLinesItemExporter

class WhoscoredspiderPipeline(object):

    def __init__(self):
        self.f = open('whoscored.txt', 'a')
        # self.exporter = JsonLinesItemExporter(self.f, ensure_ascii=False, encoding='utf-8')
        # self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.f.write(str(item.get('data'))+'\n')
        # self.exporter.export_item(item.get('data'))
        return item

    def close_spider(self,spider):
        # self.exporter.finish_exporting()
        self.f.close()