# -*- coding: utf-8 -*-
import scrapy
import json, re
from scrapy_redis.spiders import RedisSpider

#class PonymaSpider(scrapy.Spider):
class PonymaSpider(RedisSpider):
    name = 'ponyma'
    allowed_domains = ['zhihu.com']
    # start_urls = ['https://www.zhihu.com/api/v4/members/ponyma/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20']
	
	# start_urls -->> redis_key  这个是redis中的一个键  后面用来向redis发送网址的
	
    redis_key = 'ponyma:start_urls'
	
    def parse(self, response):
        # 处理数据

        # 1. 提取数据
        json_data = json.loads(response.text)
        if json_data.get('data', False):
            for data in json_data['data']:
                print('*'*80)
                print(data) # 提取的数据
                print('*'*80)
                url_token = data['url_token']
                # 粉丝的信息
                fensi_url = f'https://www.zhihu.com/api/v4/members/{url_token}/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'
                # 发送请求 交给本身处理
                yield scrapy.Request(fensi_url, callback=self.parse)
        
        # 2， 翻页的问题
        if json_data.get('paging', False):
            # 判断是否是最后一页
            if not json_data['paging'].get('is_end'):
                # 下一页的网址
                next_url = json_data['paging']['next']
                #  修改这个网页 加上api/v4
                next_url = re.sub('members', 'api/v4/members', next_url)
                print(next_url)
                # 翻页 发出请求
                yield scrapy.Request(next_url, callback=self.parse)