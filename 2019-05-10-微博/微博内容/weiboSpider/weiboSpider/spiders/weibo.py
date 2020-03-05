# -*- coding: utf-8 -*-
import scrapy


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.cn']
    start_urls = [f'https://weibo.cn/comment/H16rEvbUf?uid=1826792401&rl=1&page={page}' for page in range(1, 17992)]

    def parse(self, response):

        # 提取微博内容
        selectors = response.xpath('//div[@class="c"]')
        for selector in selectors:
            data = selector.xpath('.//text()').getall()

            data = ''.join(data).strip()
            item = {
                'data': data
            }

            # 提取个人信息  先提取网址
            user_url = selector.xpath('./a[1]/@href').get()
            user_url = response.urljoin(user_url)
            print(user_url)
            yield scrapy.Request(user_url, callback=self.parse_user_info, meta=item)


    def parse_user_info(self, response):

        data = response.meta.get('data')

        # 提取用户信息
        weibo_number = response.selector.re('微博\[\d+\]')
        weibo_guanzhu = response.selector.re('关注\[\d+\]') # # 关注[372]
        weibo_fensi = response.selector.re('粉丝\[\d+\]')

        items = {
            'data': data,
            'weibo_number': weibo_number,
            'weibo_guanzhu': weibo_guanzhu,
            'weibo_fensi': weibo_fensi,
        }

        # https://weibo.cn/1004427854/info
        # 制作个人资料的网址
        user_info_url = response.url.replace('u/', '') + '/info'
        print('个人资料的网址-->', user_info_url)
        yield scrapy.Request(user_info_url, callback=self.parse_detail_user_info, meta=items)

    # 解析个人资料信息
    def parse_detail_user_info(self,response):

        data = response.meta.get('data')
        weibo_number = response.meta.get('weibo_number')
        weibo_guanzhu = response.meta.get('weibo_guanzhu')
        weibo_fensi = response.meta.get('weibo_fensi')

        # 提取数据
        ni_cheng = response.selector.re('>昵称:(.*?)<')
        xing_bie = response.selector.re('>性别:(.*?)<')
        di_qu = response.selector.re('>地区:(.*?)<')
        sheng_ri = response.selector.re('>生日:(.*?)<')
        jian_jie = response.selector.re('>简介:(.*?)<')

        # items = {
        #     'data': data,
        #     'weibo_number': weibo_number,
        #     'weibo_guanzhu': weibo_guanzhu,
        #     'weibo_fensi': weibo_fensi,
        #     'ni_cheng': ni_cheng,
        #     'xing_bie': xing_bie,
        #     'di_qu': di_qu,
        #     'sheng_ri': sheng_ri,
        #     'jian_jie': jian_jie,
        # }

        items = {
            'items': [data, weibo_number, weibo_guanzhu, weibo_fensi, ni_cheng, xing_bie, di_qu, sheng_ri, jian_jie]
        }
        yield items