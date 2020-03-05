# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class KagglespiderPipeline(object):

    def __init__(self):
        self.f = open('kaggle2.csv', 'a', encoding='utf-8', newline='\n')
        self.csv_writer = csv.writer(self.f) # dialect='excel' 指定换行符-->\r\n
        names = ['帖子名称','发帖人ID','发帖人progression','发帖时间','发帖人competition名次',
                 'Total Posts','Comments','Topics','Net Votes','所在地','注册时间','followers','following',

                 '回帖人ID', '回帖人progression', '回帖时间', '回帖人competition名次',
                 'Total Posts', 'Comments', 'Topics', 'Net Votes', '所在地', '注册时间', 'followers', 'following',
                 ]
        self.csv_writer.writerow(names)
        self.f.flush()

    def process_item(self, item, spider):

        self.csv_writer.writerow(item.get('data'))

        return item

    def close_spider(self, spider):
        self.f.close()