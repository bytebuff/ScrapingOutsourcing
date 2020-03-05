# -*- coding: utf-8 -*-
import re, string
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class SinaSpider(CrawlSpider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/hotnews']

    rules = (
        Rule(LinkExtractor(allow=r'https://news\.sina\.com\.cn/c/.*?shtml'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        # 提取数据
        title = response.xpath('//h1[@class="main-title"]/text()').get()
        date = response.xpath('//span[@class="date"]/text()').get()
        source = response.xpath('//a[@class="source"]/text()').get()

        article = response.xpath('//div[@class="article"]//text()').getall()
        article = ''.join([article.strip() for article in article])
        article = re.sub('|'.join(string.whitespace)+"|"+'|'.join(string.ascii_letters),'', article)

        # data = f'{title},{date},{source},{article}'

        items = {
            'title': title,
            'date': date,
            'source': source,
            'article': article,
        }
        print(items)
        yield items