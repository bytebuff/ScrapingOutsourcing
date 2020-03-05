# -*- coding: utf-8 -*-
import re
import scrapy


class JobSpider(scrapy.Spider):

    name = 'job'
    allowed_domains = ['51job.com']
    # 网址里面包含了西安
    start_urls = ['https://search.51job.com/list/200200,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,1.html']


    def parse(self, response):

        selectors = response.xpath('//div[@class="dw_table"]/div[@class="el"]')
        for selector in selectors:
            detail_url = selector.xpath('./p/span/a/@href').get()
            print(detail_url)
            yield scrapy.Request(detail_url, callback=self.detail_parse)

        page = re.search('共(\d+)页', response.text).group(1)
        for p in range(2, int(page)+1):
            url = re.sub(',(\d+)\.html', f',{p}.html', response.url)
            yield scrapy.Request(url)


    def detail_parse(self, response):
        # print(respon.text)
        title = response.xpath('//h1/@title').get()
        gongsimingzi = response.xpath('//p[@class="cname"]/a/@title').get()
        jiage = response.xpath('//div[@class="cn"]/strong/text()').get()
        yaoqiu = response.xpath('//p[@class="msg ltype"]/@title').get()
        fuli = response.xpath('//span[@class="sp4"]/text()').getall()

        # 处理工作要求
        yaoqiu = re.sub('\xa0\xa0', '', yaoqiu)
        yqoaiu_diqu, yaoqiu_year, yaoqiu_benke, yaoqiu_renshu, yqoaiu_fabu = yaoqiu.split('|')
        # 福利处理
        fuli = '|'.join(fuli)

        data = [title, gongsimingzi, jiage, yqoaiu_diqu, yaoqiu_year, yaoqiu_benke, yaoqiu_renshu, yqoaiu_fabu, fuli]

        item = {
         'data': data
        }

        yield item