# -*- coding: utf-8 -*-
import scrapy


class Baobeihuijia2Spider(scrapy.Spider):
    name = 'baobeihuijia2'
    allowed_domains = ['baobeihuijia.com']
    start_urls = [f'https://www.baobeihuijia.com/list.aspx?tid=1&sex=&photo=&page={page}' for page in range(1, 1333)]

    def parse(self, response):
       detail_urls =  response.xpath('//dd/a[1]/@href').getall()
       for url in detail_urls:
            url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.parseDetail)

        # 翻页
    def parseDetail(self, response):
        # 提取信息
        data = []
        selectors = response.xpath('//div[@id="table_1_normaldivr"]/ul')
        for selector in selectors:
            # 选择数据

            # 家寻宝贝
            data1 = selector.xpath('./li[1]/text()').get()
            data2 = selector.xpath('./li[2]/a/text()').get()
            data3 = selector.xpath('./li[3]/text()').get()
            data4 = selector.xpath('./li[4]/text()').get()
            data5 = selector.xpath('./li[5]/text()').get()
            data6 = selector.xpath('./li[6]/text()').get()
            data7 = selector.xpath('./li[7]/text()').get()
            data8 = selector.xpath('./li[8]/text()').get()
            data9 = selector.xpath('./li[9]/text()').get()
            data10 = selector.xpath('./li[10]/text()').get()
            data11 = selector.xpath('./li[11]/text()').get()
            data12 = selector.xpath('./li[12]/text()').get()
            data13 = selector.xpath('./li[13]/text()').get()
            all_data = [data1, data2, data3 ,data4, data5, data6, data7, data8, data9, data10, data11, data12, data13]
            data.extend(all_data)
            item = {}
            item['data'] = data
            yield item