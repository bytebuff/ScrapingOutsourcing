# -*- coding: utf-8 -*-
import scrapy


class SougouSpider(scrapy.Spider):
    name = 'sougou'
    allowed_domains = ['sougou.com']
    start_urls = [
        f'https://www.sogou.com/web?query=%E5%9B%BD%E5%AD%A6%E5%9F%B9%E8%AE%AD&page={page}' for  page in range(1,500)]

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
            'baiduguoxueSpider.pipelines.SougouguoxuespiderPipeline': 300,
        }
    }

    def parse(self, response):
        print(response.url)
        selectors = response.xpath('//div[@class="rb"]')
        for selector in selectors:
            print('*'*80)
            title = selector.xpath('.//a[@name="dttl"]//text()').extract()
            title = ''.join(title)
            #print(title)
            content = selector.xpath('.//div[@class="ft"]//text()').extract()
            content = ''.join(content)

            data = {
                'title': title,
                'content': content
            }

            yield data