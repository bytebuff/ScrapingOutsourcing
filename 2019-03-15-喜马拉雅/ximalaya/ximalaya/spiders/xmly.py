# -*- coding: utf-8 -*-
import scrapy
import json


class XmlySpider(scrapy.Spider):
    name = 'xmly'
    allowed_domains = ['ximalaya.com']
    start_urls = ['https://www.ximalaya.com/revision/category/queryCategoryPageAlbums?category=youshengshu&subcategory=wenxue&meta=&sort=0&page={}&perPage=30'.format(page) for page in range(1, 2)]

    def parse(self, response):
        # print(json.loads(response.text))
        json_data = json.loads(response.text)
        if json_data['data']:
            for data in json_data['data']['albums']:
                albumId = data['albumId']
                # https://www.ximalaya.com/revision/album?albumId=9617941
                detail_link = f'https://www.ximalaya.com/revision/album?albumId={albumId}'
                yield scrapy.Request(response.urljoin(detail_link), callback=self.parse_detail, meta={'data': data})


    def parse_detail(self, response):
        # 解析详情页
        data = response.meta['data']
        detail_json_data = json.loads(response.text)
        if detail_json_data['data']:
            detail_data = detail_json_data['data']['tracksInfo']['tracks']
            
            dict_data = {
                'data': data,
                'detail_data': detail_data
            }
            
            yield dict_data