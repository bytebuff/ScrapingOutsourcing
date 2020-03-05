# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZhihuspiderPipeline(object):

    def __init__(self):
        # 打开文件
        self.f = open('zhihu2.txt', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        # 写入数据
        item = dict(item)
        self.f.write(item['content']+'\n')
        return item

    # 关闭文件
    def close_spider(self, spider):
        self.f.close()
