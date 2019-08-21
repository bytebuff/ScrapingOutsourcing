# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os, csv
import requests
import pymysql.cursors


class ManmanbuyspiderPipeline(object):

    def __init__(self):
        self.f = open('manmanbuy.csv', 'w', encoding='utf-8', newline="")

    def process_item(self, item, spider):
        item = dict(item)
        data = list(item.values())
        #data = ','.join(data)
        #data = data.strip()
        csv_writer = csv.writer(self.f)

        csv_writer.writerow(data)

        return item

    def close_spider(self, spider):
        self.f.close()



class ManmanbuyspiderImagePipeline(object):

    def process_item(self, item, spider):

        name = item.get('title')
        if len(name)>5:
            pic_name = name[0:6]
        else:
            pic_name = name

        pic_url = item.get('picture_url')

        if 'http' in pic_url:
            response = requests.get(pic_url)
        else:
            pic_url = 'http:' + pic_url
            response = requests.get(pic_url)

        os.makedirs('images', exist_ok=True)
        with open(f'images/{pic_name}.png', 'wb') as fp:
            fp.write(response.content)

        return item


# 保存数据库
class ManmanbuyspiderMySQLPipeline(object):

    def __init__(self):
        self.connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='314159',
            db='jdspider',
            charset='utf8'
        )

        # 获取游标
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        sql = 'INSERT INTO manmanbuy ( href, picture_url, title, price, from_url, comment_num, ziying ) VALUES ( %s, %s, %s, %s, %s, %s, %s )'
        self.cursor.execute(sql,(item.get('href'), item.get('picture_url'), item.get('title'),item.get('price'),item.get('from_url'),item.get('comment_num'),item.get('ziying')))
        self.connect.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()