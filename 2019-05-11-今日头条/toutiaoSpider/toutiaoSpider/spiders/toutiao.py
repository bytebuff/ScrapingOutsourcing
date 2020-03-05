# -*- coding: utf-8 -*-
import scrapy
import json, re

class ToutiaoSpider(scrapy.Spider):
    name = 'toutiao'
    # allowed_domains = ['toutiao.com']
    
    start_urls = ['https://www.toutiao.com/c/user/following/?user_id=105471557363&cursor=0&count=20&_signature=QOCS3hATHDhJrOjLPep2b0Dgks']

    def parse(self, response):
        json_data = json.loads(response.text)

        # print(json_data)
        if json_data.get('data'):
            for data in json_data.get('data'):
                user_id = data.get('user_id')
                user_url = f'https://www.toutiao.com/c/user/{user_id}/'
                user_loop_url = f'https://www.toutiao.com/c/user/following/?user_id={user_id}&cursor=0&count=20&_signature=fU.V6hAbIZt0A6..VPjzu31P1f'
                yield scrapy.Request(user_loop_url, callback=self.parse)
                yield scrapy.Request(user_url, callback=self.parse_detail) # 详情页

        # 翻页
        cursor = json_data.get('cursor')
        user_id = re.search('user_id=(\d+)&', response.url).group(1)
        if cursor:
            next_url = f'https://www.toutiao.com/c/user/following/?user_id={user_id}&cursor={cursor}&count=20&_signature=eqEEQxAcJnpz7X5WpK5dAHqhBF'
            yield scrapy.Request(next_url, callback=self.parse)

    # 解析详情页 为了获取 media_id
    def parse_detail(self, response):
        # media_id的获取是为了视频所在的那个网址
        media_id = response.selector.re("mediaId: (.*?),")
        fen_si = response.selector.re("fensi:'(\d+)',")
        if media_id:
            media_id_url = f'https://www.toutiao.com/api/pc/media_hot/?media_id={media_id[0]}'
            print(media_id_url)
            # headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
            yield scrapy.Request(media_id_url, callback=self.parse_item_id, meta={'fen_si': fen_si})

    # 获取item_id
    def parse_item_id(self, response):
        # print(response.text)
        fen_si = response.meta.get('fen_si')
        json_data = json.loads(response.text)
        if json_data.get('data'):
            if json_data.get('data').get('hot_articles'):
                item_id = json_data.get('data').get('hot_articles')[0].get('item_id')
                # print(item_id)
                item_id_url = f'http://www.365yg.com/i{item_id}/'
                yield scrapy.Request(item_id_url, callback=self.parse_is_origina, meta={'fen_si': fen_si})


    def parse_is_origina(self, response):
        fen_si = response.meta.get('fen_si')
        name = response.selector.re("name: '(.*?)',")
        # 判断是否原创
        if 'isOriginal: true' in response.text and 'videoPlayCount' in response.text:

            # print('原创', fen_si, name) # 打印作者

            data = f'{fen_si},{name}'

            items = {
                'data': data
            }
            print(items)
            yield items