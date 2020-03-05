# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class LagouspiderPipeline(object):

    def __init__(self):
        self.bj_f = open('beijing_data.csv', 'a', encoding='utf-8')
        self.xa_f = open('xian_data.csv', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        if item['city']=='北京':
            self.bj_f.write(item['positionName']+'\n')
        if item['city'] == '西安':
            self.xa_f.write(item['positionName']+'\n')
        return item

    def close_spider(self, spider):
        self.xa_f.close()
        self.bj_f.close()



# 保存数据库
class LagouspiderMySQLPipeline(object):

    def __init__(self):
        self.connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='314159',
            db='lagouspider',
            charset='utf8'
        )

        # 获取游标
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        sql = 'INSERT INTO lagou ( positionName, city, companyFullName, companySize, education, salary, positionAdvantage ) VALUES ( %s, %s, %s, %s, %s, %s, %s )'
        self.cursor.execute(sql,(item.get('positionName'),
                                 item.get('city'),
                                 item.get('companyFullName'),
                                 item.get('companySize'),
                                 item.get('education'),
                                 item.get('salary'),
                                 item.get('positionAdvantage')))
        self.connect.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()

