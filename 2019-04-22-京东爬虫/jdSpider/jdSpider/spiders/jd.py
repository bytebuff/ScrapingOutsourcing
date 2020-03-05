# -*- coding: utf-8 -*-
import scrapy
import json, re
from copy import deepcopy


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = [f'https://search.jd.com/Search?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%86%9C%E4%BA%A7%E5%93%81&stock=1&page={page}' for page in range(1,100)] + [f'https://search.jd.com/s_new.php?keyword=农产品&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=农产品&stock=1&page={page}&scrolling=y&tpl=3_M' for page in range(1,100)]

    def parse(self, response):

        # 数据提取
        selectors = response.xpath('//div[@id="J_goodsList"]/ul/li')
        for selector in selectors:
            price = selector.xpath('.//div[@class="p-price"]//i/text()').get()
            title = selector.xpath('.//div[contains(@class,"p-name")]//em//text()').getall()
            productId = selector.xpath('./@data-sku').get()
            item = {
                'price': price,
                'title': ''.join(title),
                'productId': productId
            }
            #print(item)
            # comments_list = []
            # 评论信息
            comments_url = f'https://sclub.jd.com/comment/productPageComments.action?productId={productId}&score=0&sortType=5&page=0&pageSize=10'
            yield item
            yield scrapy.Request(comments_url, meta={'productId': productId}, callback=self.parseComment)

    def parseComment(self, response):
        # 得到上一个方法中的数据
        # comments_list = response.meta.get('comments_list')
        productId = response.meta.get('productId')
        # 提取评论信息
        json_data = json.loads(response.text)

        maxPage = json_data.get('maxPage')

        if json_data.get('comments'):
            for dat in json_data['comments']:
                content = dat.get('content')
                #print(content)
                # comments_list.append(content)

                items = {
                    # 'items': comments_list,
                    'content': content,
                    #'maxPage': maxPage,
                    'productId': productId
                }
                print(items)
                yield items

        # 翻页
        if json_data.get('maxPage'):
            maxPage = int(json_data['maxPage'])
            if maxPage>=2:
                for page in range(1, maxPage):
                    maxPageUrl = re.sub('page=\d+', f'page={page}', response.url)
                    print(maxPageUrl)
                    yield scrapy.Request(maxPageUrl, callback=self.parseComment, meta={'productId': productId})

                # items = {
                #     'item': item,
                #     'maxPage': maxPage if maxPage else '',
                #     'comments_list': comments_list,
                #     'length': len(comments_list)
                # }
                # print(items)
                # yield items