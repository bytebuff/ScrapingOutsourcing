# -*- coding: utf-8 -*-
import scrapy


class BaobeihuijiaSpider(scrapy.Spider):
    name = 'baobeihuijia'
    allowed_domains = ['baobeihuijia.com']
    start_urls = [f'https://www.baobeihuijia.com/succeed.aspx?keywords=&page={page}' for page in range(1, 89)]

    def parse(self, response):
        # print(response.text)

        selectors = response.xpath('//table/tr')
        for selector in selectors:
            data = selector.xpath('./td[@class="bscont"]/text()').getall()
            if data:
                data.pop()
                print(data)
                item = {}
                item['data'] = data
                yield item