# -*- coding: utf-8 -*-
import scrapy
import json

# 获取id.txt文件中的数据  id 号
def get_id():
    with open('toutiaoSpider/spiders/id.txt', 'r') as fp:
        for line in fp:
            _id = line.strip()
            yield _id


# 定义爬虫的类
class ToutiaoSpider(scrapy.Spider):
    name = 'toutiao' # 爬虫名字
    allowed_domains = ['toutiao.com'] # 爬虫允许的域名

    # 初始发送的网址
    def start_requests(self):
        # 请求数据的网址
        start_url = 'https://www.toutiao.com/api/comment/list/?group_id={0}&item_id={0}&offset=0&count=15'
        _ids = get_id() # 获取id
        for _id in _ids:
            start_url = start_url.format(_id) # 拼接网址
            # 发出请求
            yield scrapy.Request(start_url, callback=self.parse)

    def parse(self, response): # 解析数据
        # 将数据转换成json类型  本来数据就是json类型 scrapy的得到的是text文本类型
        json_data = json.loads(response.text)
        if json_data.get('data', False):
            # data = json_data['data']
            if json_data['data'].get('comments'):
                comments = json_data['data']['comments']
                for comment in comments:
                    # 提取点赞数
                    digg_count = comment['digg_count']
                    # 提取评论内容
                    text = comment['text']

                    # 准备保存数据
                    item = {
                        '点赞数': digg_count,
                        '评论': text
                    }
                    # 将数据交给管道文件 用来保存
                    yield item
