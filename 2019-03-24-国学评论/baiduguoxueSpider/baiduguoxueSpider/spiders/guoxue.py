# -*- coding: utf-8 -*-
import scrapy
import re


class GuoxueSpider(scrapy.Spider):
    name = 'guoxue'
    allowed_domains = ['baidu.com']
    start_urls = [f'https://www.baidu.com/s?wd=%E5%9B%BD%E5%AD%A6%E5%9F%B9%E8%AE%AD&pn={pn*10}' for pn in range(1, 500)]

    def parse(self, response):

        # 标题
        title = response.selector.re('data-tools=\'{"title":"(.*?)","url":')
        # 内容
        content = response.selector.re('class="c-abstract">(.*?)target="_blank"')

        # 对应起来
        if len(title) == len(content):
        
            for tit, con in zip(title, content):
                
                con = re.sub('</em>|<em>|</div>|<div class="f13"|\.\.\.|><a', '', con)

                data = {
                    'title': tit,
                    'content': con
                }

                yield data

        # 翻页
        # next_page = response.xpath('//a[@class="n"]/@href').extract()
        # if len(next_page) == 2:
        #     url = response.urljoin(next_page[1])
        #     yield scrapy.Request(url, callback=self.parse)

