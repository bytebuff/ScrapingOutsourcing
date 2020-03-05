# -*- coding: utf-8 -*-
import scrapy


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.cn']
    start_urls = [f'https://weibo.cn/1826792401/profile?filter=0&page={page}' for page in range(1, 153)]

    def parse(self, response):
        pinglun_urls = response.xpath('//a[@class="cc"]/@href').getall()
        for pinglun_url in pinglun_urls:

            yield scrapy.Request(pinglun_url, callback=self.parse_comment)

    def parse_comment(self, response):

        comments = response.xpath('//span[@class="ctt"]/text()').getall()
        for comment in comments:
            if comment != '回复':

                item = {
                    'data': comment
                }

                yield item

        # 下一页
        next_page = response.xpath("//a[text()='下页']/@href").get()
        if next_page:
            next_url = response.urljoin(next_page)
            yield scrapy.Request(next_url, callback=self.parse_comment)

