# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WeibospiderPipeline(object):

    def __init__(self):

        self.f = open('weibo_pinglun.txt', 'a', encoding='utf-8')

    def process_item(self, item, spider):

        string_data =''.join(item['data'])

        self.f.write(string_data+'\n')

        return item


    def close_spider(self, spider):
        self.f.close()