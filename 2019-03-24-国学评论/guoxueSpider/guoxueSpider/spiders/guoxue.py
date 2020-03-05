# -*- coding: utf-8 -*-
import scrapy
import json, re


class GuoxueSpider(scrapy.Spider):
    name = 'guoxue'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v4/search_v3?t=general&q=%E5%9B%BD%E5%AD%A6%E5%9F%B9%E8%AE%AD&correction=1&offset=40&limit=20&lc_idx=42&show_all_topics=0&search_hash_id=d759338e874c39be9c93d319be9420e7&vertical_info=0%2C1%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C1']

    def parse(self, response):
        json_data = json.loads(response.text) # 将相应转化成json数据
        # 判断data是否为空
        if json_data.get('data', False):
            for dat in json_data['data']:
                content = ''
                if dat['object'].get('content', False):
                    # 楼主的评论
                    content = dat['object']['content']
                name = ''
                # 标题
                if dat['object'].get('question', False):
                    name = dat['object']['question']['name']
                # 提取id用来获取评论
                _id = dat['object']['id'] 

                content = re.sub('</p>|<p>|<br>|</em>|<em>', '', content)
                name = re.sub('</p>|<p>|<br>|</em>|<em>', '', name)

                data = f'{name},{content}'

                id_url = f'https://www.zhihu.com/api/v4/answers/{_id}/root_comments?include=data%5B*%5D.author%2Ccollapsed%2Creply_to_author%2Cdisliked%2Ccontent%2Cvoting%2Cvote_count%2Cis_parent_author%2Cis_author&order=normal&limit=20&offset=0&status=open'

                yield scrapy.Request(id_url, callback=self.parse_content, meta={'data':data})

                # # 3. 访问粉丝的粉丝
                # # 提取粉丝的url_token
                # url_token = dat['url_token']
                # # 提取出来是一个列表
                # old_url_token = re.findall('members/(.*?)/followers', response.url)[0]
                # new_old_token = re.sub(old_url_token, url_token, response.url)
                # # 发出粉丝的网址请求
                # yield scrapy.Request(new_old_token)


        # 2. 翻页

        # 先判断是否是最后一页
        if json_data.get('paging', False):
            # 判断是否是最后一页
            if not json_data['paging'].get('is_end', False):
                # 选择下一页 这个网址不能直接使用  要拼凑一下
                next_url = json_data['paging']['next']
                # 正则替换 拼凑成下一页的网址
                # next_url = re.sub('members', 'api/v4/members', next_url)
                # 发出请求
                yield scrapy.Request(next_url, callback=self.parse)


    def parse_content(self, response):
        
        all_contents = []

        data = response.meta['data']

        json_data = json.loads(response.text) # 将相应转化成json数据
        # 判断data是否为空
        if json_data.get('data', False):
            for dat in json_data['data']:
                # 楼主的评论
                all_contents.append(dat['content'])

        all_contents = [re.sub('</p>|<p>|<br>|</em>|<em>', '', contents) for contents in all_contents]

        data = f'{data},{all_contents}'

        data = {
            'data': data
        }

        yield data