# -*- coding: utf-8 -*-
import scrapy


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['google.com']
    start_urls = ['https://www.google.com.hk/search?q=%E5%9B%BD%E5%AD%A6%E5%9F%B9%E8%AE%AD&start=20']

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
        },
        'ITEM_PIPELINES': {
            #'baiduguoxueSpider.pipelines.SougouguoxuespiderPipeline': 300,
        }
    }


    def parse(self, response):
        selectors = response.xpath('//div[@class="g"]')
        for selector in selectors:
            title = selector.xpath('.//div[@class="g"]//h3/text()').extract()
            content = selector.xpath('.//span[@class="st"]//text()').extract()
            print('*'*80)
            print(title)
            print(content)
            print('*'*80)


