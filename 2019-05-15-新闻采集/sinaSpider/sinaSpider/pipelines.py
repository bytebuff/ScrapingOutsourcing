# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
# from scrapy import log



class SinaspiderPipeline(object):
    def process_item(self, item, spider):
        return item



class MyMongoDBPipeline(object):
    def __init__(self):
        connection = MongoClient(
            'MONGODB_SERVER', # 127.0.0.1
            'MONGODB_PORT' #
        )
        db = connection['MONGODB_DB'] # 数据库
        self.collection = db['MONGODB_COLLECTION'] # 数据库表

    def process_item(self, item, spider):

        self.collection.insert(dict(item))

        return item