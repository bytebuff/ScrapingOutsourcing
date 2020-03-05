# -*- coding: utf-8 -*-
import re
import scrapy


class ThepaperSpider(scrapy.Spider):
    name = 'thepaper'
    # allowed_domains = ['thepaper.com']
    start_urls = ['https://www.thepaper.cn/load_moreFloorComment.jsp?contid=3900482&hotIds=23384174,23387471,23385075,23405310,23388204&startId=23404061']

    def parse(self, response):

        comments = response.xpath("//div[@class='ansright_cont']//a/text()").getall()

        for comment in comments:
            data = {}
            # print(comment.strip())
            comm = comment.strip()
            data['item'] = comm
            yield data

        # 提取startID
        # startid = response.xpath("//div[@id='startId']/@startId").get()
        startid = re.findall('<div id="startId" startId="(\d+)" pageIndex', response.text)
        if startid:
            print('*' * 10 + str(startid[0]) + '*' * 10)
            # 拼凑新的网址
            next_url = f'https://www.thepaper.cn/load_moreFloorComment.jsp?contid=3900482&hotIds=23384174,23387471,23385075,23405310,23388204&startId={startid[0]}'
            yield scrapy.Request(next_url, callback=self.parse)