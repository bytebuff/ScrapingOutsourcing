# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from .items import JdcrspiderModel

class JdcrspiderPipeline(object):

    def open_spider(self, spider):
        if not JdcrspiderModel.table_exists():
            JdcrspiderModel.create_table()
            print(spider.settings['TABLE_TITLE_NAME_ZH'])
            JdcrspiderModel.create(**spider.settings['TABLE_TITLE_NAME_ZH'])


    def process_item(self, item, spider):
        try:
            JdcrspiderModel.create(**item)
        except Exception as e:
            print(f"管道错误->{e}")
        return item

    def close_spider(self, spider):
        pass