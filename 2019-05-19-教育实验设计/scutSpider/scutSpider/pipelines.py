# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScutspiderPipeline(object):

    def __init__(self):
        self.f = open('scut_urls.txt', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        self.f.write(item.get('url')+'\n')
        self.f.flush() # 立即写入文件中
        return item

    def close_spider(self, spider):
        self.f.close()