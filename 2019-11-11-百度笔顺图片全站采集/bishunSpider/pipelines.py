# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.exporters import JsonLinesItemExporter
import requests,json

# 保存信息
class BishunspiderPipeline(object):

    def __init__(self):
        self.f = open('bishun.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.f, ensure_ascii=False, encoding='utf-8')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.f.close()

# 保存图片
class BishunspiderImagesPipeline(object):

    def process_item(self, item, spider):
        img_url = item['img_url']
        chinese_character = item['chinese_character']
        if img_url:
            response = requests.get(img_url)
            with open(f'C:\\Users\\19609\\Desktop\\SpiderEnv\\百度汉字笔顺\\full\\{chinese_character}.gif', 'wb') as fp:
                fp.write(response.content)
        return item