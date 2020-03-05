# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 管道文件 用来保存数据 需要在配置文件中激活
class ToutiaospiderPipeline(object):

    def __init__(self):
        # 打开文件
        self.f = open('zhihu.txt', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        # 写入数据
        item = dict(item)
        self.f.write(item['content']+'\n')
        return item

    # 关闭文件
    def close_spider(self, spider):
        self.f.close()


# 管道文件 用来保存数据 需要在配置文件中激活
class ToutiaospiderCSVPipeline(object):

    def __init__(self):
        # 打开文件
        self.f = open('toutiao.csv', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        # 写入数据
        item = dict(item)
        data = f"{item.get('点赞数')},{item.get('评论')}"
        self.f.write(data+'\n')
        return item

    # 关闭文件
    def close_spider(self, spider):
        self.f.close()
