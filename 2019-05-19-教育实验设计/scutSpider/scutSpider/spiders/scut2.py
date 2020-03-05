# -*- coding: utf-8 -*-
import scrapy


class Scut2Spider(scrapy.Spider):
    name = 'scut2'
    allowed_domains = ['scut.com']
    start_urls = ['http://scut.com/']

    def parse(self, response):
        pass
