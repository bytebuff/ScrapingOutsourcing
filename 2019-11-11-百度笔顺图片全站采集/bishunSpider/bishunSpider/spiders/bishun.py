# -*- coding: utf-8 -*-
import scrapy
from parsel import Selector
import re
from urllib.parse import unquote


class BishunSpider(scrapy.Spider):
    name = 'bishun'
    allowed_domains = ['baidu.com']
    # 从‘王’开始
    start_urls = ['https://hanyu.baidu.com/zici/s?wd=王&query=王']

    def parse(self, response):
        # 提取图片网址
        selector = Selector(text=response.text)
        img_url = selector.xpath('//img[@class="bishun"]/@data-gif').get()

        chinese_character = re.search('wd=(.*?)&',response.url).group(1)
        
        item = {
            'img_url': img_url,
            'response_url': response.url,
            'chinese_character': unquote(chinese_character)
        }

        yield item
        # 提取相关字 提取热搜字 进行迭代
        new_character = selector.xpath('//a[@class="img-link"]/@href').getall()
        
        for character in new_character:
            # 拼接
            new_url = response.urljoin(character)   
            # 发送请求
            yield scrapy.Request(new_url, callback=self.parse)