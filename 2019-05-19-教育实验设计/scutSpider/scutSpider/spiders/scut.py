# -*- coding: utf-8 -*-
import scrapy
import logging
# 链接提取器 提取所有的链接
from scrapy.linkextractors import LinkExtractor
# 导入提取网址的规则
from scrapy.spiders import CrawlSpider, Rule


# 爬虫的类  采集全站爬虫 继承自CrawlSpider
class ScutSpider(CrawlSpider):

    # 爬虫的名字
    name = 'scut'

    # 允许采集的域名
    allowed_domains = ['scut.edu.cn']

    # 开始的网址
    start_urls = ['http://scut.edu.cn/']

    # 网站过滤规则
    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=False),
    )

    # 用来处理响应的
    def parse_item(self, response):
        # 提取出网址
        url = response.url
        # 构造成字典格式提交出去
        items = {
            'url': url
        }
        # self.logger.info(items)
        # 返回数据
        yield items