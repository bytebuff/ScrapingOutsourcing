# -*- coding: utf-8 -*-
from requests.utils import quote
import scrapy

quote('白菜', encoding='gb2312')


class ManmanbuySpider(scrapy.Spider):
    name = 'manmanbuy'
    allowed_domains = ['manmanbuy.com']
    # http://s.manmanbuy.com/Default.aspx?PageID=2&key=%b0%d7%b2%cb
    start_urls = ['http://s.manmanbuy.com/Default.aspx?PageID=3&key=%b0%d7%b2%cb']

    def start_requests(self):

        key = getattr(self, 'key', '白菜')
        page = getattr(self, 'page', 1)
        if key:
            key = quote(key, encoding='gb2312')
            for page in range(1, int(page)+1):
                url = f'http://s.manmanbuy.com/Default.aspx?PageID={page}&key={key}'
                yield scrapy.Request(url)

    def parse(self, response):
        # 提取数据
        selectors = response.xpath('//div[@class="div1100"]/div')
        for selector in selectors:
            # 跳转链接
            href = selector.xpath('.//div[@class="proPickuanBig"]/a/@href').get()
            href = href if href else ''
            # 获取图片网址
            picture_url = selector.xpath('.//div[@class="proPickuanBig"]//img/@src').get()
            picture_url = picture_url if picture_url else ''
            # 标题
            title = selector.xpath('.//div[@class="divtitleBigNew"]//a/@title').get()
            title = title if title else ''
            # 价格
            price = selector.xpath('.//span[@class="listpricespan"]//text()').get()
            price = price if price else ''
            # 来自哪个网址
            from_url = selector.xpath('.//div[@class="divpriceBigzydq"]//span/text()').get()
            from_url = from_url if from_url else ''
            # 评论数
            comment_num = selector.xpath('.//div[@class="divlogoBigNew"]/a/text()').get()
            comment_num = comment_num if comment_num else ''
            # 自营还是其他
            ziying = selector.xpath('.//div[@class="divcommentBigNew AreaZY"]/text()').get()
            ziying = ziying if ziying else ''
            # 去掉全部是空的元素
            if href and picture_url and title and price and from_url and comment_num and ziying:
                item = {
                    'href': href.strip(),
                    'picture_url': picture_url.strip(),
                    'title': title.strip(),
                    'price': price.strip(),
                    'from_url': from_url.strip(),
                    'comment_num': comment_num.strip(),
                    'ziying': ziying.strip(),
                }
                print(item)
                yield item