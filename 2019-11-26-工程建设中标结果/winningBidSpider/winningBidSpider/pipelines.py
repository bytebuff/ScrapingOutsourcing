# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


# 广东
class WinningbidspiderPipelinegdggzy(object):

    def __init__(self):
        self.f = open('gdggzy.csv', 'a', encoding='utf-8', newline='')
        self.csvWriter = csv.writer(self.f)

    def process_item(self, item, spider):
        data = [
            item.get('name', ''),
            item.get('amountMoney', ''),
            item.get('time', ''),
            item.get('meiti', ''),
            item.get('xiangmuName', ''),
            item.get('zhaobiaoRen', ''),
            item.get('zhaobiaoFangShi', ''),
            item.get('city', ''),
            item.get('detailUrl', ''),
        ]
        self.csvWriter.writerow(data)
        return item

    def close_spider(self, spider):
        self.f.close()


# 湖北
class WinningbidspiderPipelinehbggzyfwpt(object):

    def __init__(self):
        self.f = open('hbggzyfwpt.csv', 'a', encoding='utf-8', newline='')
        self.csvWriter = csv.writer(self.f)

    def process_item(self, item, spider):
        data = [
            item.get('bulletinIssueTime', ''),
            item.get('zhaoBiaoRen', ''),
            item.get('bulletinName', ''),
            item.get('diZHi', ''),
            item.get('zhongBiaoRen', ''),
            item.get('zhongBiaoJia', ''),
            item.get('city', ''),
            item.get('detailUrl', ''),
        ]
        self.csvWriter.writerow(data)
        return item

    def close_spider(self, spider):
        self.f.close()


# 上海
class WinningbidspiderPipelineshanghai(object):

    def __init__(self):
        self.f = open('shanghai.csv', 'a', encoding='utf-8', newline='')
        self.csvWriter = csv.writer(self.f)

    def process_item(self, item, spider):
        data = [
            item.get('tenderName', ''),
            item.get('projectName', ''),
            item.get('address', ''),
            item.get('winBidderName', ''),
            item.get('evaluationPrice', ''),
            item.get('bidOpenTime', ''),
        ]
        self.csvWriter.writerow(data)
        return item

    def close_spider(self, spider):
        self.f.close()


# 四川
class WinningbidspiderPipelineggzyjy(object):

    def __init__(self):
        self.f = open('ggzyjy.csv', 'a', encoding='utf-8', newline='')
        self.csvWriter = csv.writer(self.f)

    def process_item(self, item, spider):
        data = [
            item.get('title', ''),
            item.get('zhaoBiaoRen', ''),
            item.get('shiJian', ''),
            item.get('diYiMing', ''),
            item.get('jingBiaoJia', ''),
            item.get('zhiCheng', ''),
            item.get('zhuanzai', ''),
        ]
        self.csvWriter.writerow(data)
        return item

    def close_spider(self, spider):
        self.f.close()


# 广西
class WinningbidspiderPipelinejxsggzy(object):

    def __init__(self):
        self.f = open('jxsggzy.csv', 'a', encoding='utf-8', newline='')
        self.csvWriter = csv.writer(self.f)

    def process_item(self, item, spider):
        data = [
            item.get('jianSheDanWei', ''),
            item.get('gongChengMingCheng', ''),
            item.get('gongChengDiZhi', ''),
            item.get('kaiBiaoShiJian', ''),
            item.get('danWeiMingCheng', ''),
            item.get('touBiaoZiZhi', ''),
            item.get('touBiaoBaoJia', ''),
        ]
        self.csvWriter.writerow(data)
        return item

    def close_spider(self, spider):
        self.f.close()


# 江苏
class WinningbidspiderPipelinejszwfw(object):

    def __init__(self):
        self.f = open('jszwfw.csv', 'a', encoding='utf-8', newline='')
        self.csvWriter = csv.writer(self.f)

    def process_item(self, item, spider):
        data = [
            item.get('biaoTi', ''),
            item.get('jianSheDanWei', ''),
            item.get('zhongBiaoDanWei', ''),
            item.get('zhongBiaoJia', ''),
            item.get('zhongBiaoShiJian', ''),
            item.get('laiYuan', ''),
            item.get('fieldvalue', ''),
        ]
        self.csvWriter.writerow(data)
        return item

    def close_spider(self, spider):
        self.f.close()


# 重庆
class WinningbidspiderPipelinecqggzy(object):

    def __init__(self):
        self.f = open('cqggzy.csv', 'a', encoding='utf-8', newline='')
        self.csvWriter = csv.writer(self.f)

    def process_item(self, item, spider):
        data = [
            item.get('biaoTi', ''),
            item.get('jianSheDanWei', ''),
            item.get('zhongBiaoDanWei', ''),
            item.get('zhongBiaoJia', ''),
            item.get('zhongBiaoShiJian', ''),
        ]
        self.csvWriter.writerow(data)
        return item

    def close_spider(self, spider):
        self.f.close()



