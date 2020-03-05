# -*- coding: utf-8 -*-
import re
import scrapy


class HexunSpider(scrapy.Spider):
    name = 'hexun'
    allowed_domains = ['hexun.com']
    start_urls = [f'http://bank.hexun.com/yhjrdd/index-{index}.html' for index in range(1, 900 + 1)]
    # start_urls = [f'http://bank.hexun.com/yhlcyw/index-{index}.html' for index in range(1, 267 + 1)]

    def parse(self, response):
        # 数据提取
        selectors = response.xpath('//div[@class="temp01"]/ul/li')
        for selector in selectors:
            timeSpan = selector.xpath('./span/text()').get(default='')
            # 网址链接 提取时间
            timeA = selector.xpath('./a/@href').get(default='')
            # 时间拼接
            timeResult = self.parseTime(timeSpan, timeA)

            title = selector.xpath('./a/text()').get(default='')

            items = {
                'title': title,
                'timeResult': timeResult,
            }

            yield items

    @staticmethod
    def parseTime(timeSpan, timeA):
        timeYear = re.search('com/(.*?)-\d+-\d+/\d+.html', timeA).group(1)
        timeResult = timeYear + timeSpan
        return timeResult
