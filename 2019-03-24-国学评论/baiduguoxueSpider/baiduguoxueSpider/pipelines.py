# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaiduguoxuespiderPipeline(object):

    def __init__(self):
        self.f = open('baiduguoxue2.jl', 'a', encoding='utf-8')

    def process_item(self, item, spider):

        data = dict(item)

        self.f.write(str(data)+'\n')

        return item

    def close_spider(self,spider):
        self.f.close()


class SougouguoxuespiderPipeline(object):

    def __init__(self):
        self.f = open('sougou.jl', 'a', encoding='utf-8')

    def process_item(self, item, spider):

        data = dict(item)

        self.f.write(str(data)+'\n')

        return item

    def close_spider(self,spider):
        self.f.close()