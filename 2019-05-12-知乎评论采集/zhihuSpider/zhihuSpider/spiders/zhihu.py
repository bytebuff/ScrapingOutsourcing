# -*- coding: utf-8 -*-
import scrapy
import json


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = [f'https://www.zhihu.com/api/v4/answers/542641969/root_comments?include=data%5B%2A%5D.author%2Ccollapsed%2Creply_to_author%2Cdisliked%2Ccontent%2Cvoting%2Cvote_count%2Cis_parent_author%2Cis_author&limit=10&offset={offset}&order=normal&status=open' for offset in range(0,8365, 10)]

    def parse(self, response):
        json_data = json.loads(response.text)
        if json_data.get('data'):

            for data in json_data['data']:
                content = data.get('content')
                items = {
                    'content': content
                }
                yield items
