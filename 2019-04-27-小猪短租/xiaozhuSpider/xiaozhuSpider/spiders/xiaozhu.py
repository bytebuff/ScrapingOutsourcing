# -*- coding: utf-8 -*-
import scrapy
import re


def get_citys():

    with open(r'C:\Users\19609\Desktop\SpiderEnv\小猪短租\xiaozhuSpider\xiaozhuSpider\spiders\citys.txt', encoding='utf-8') as fp:
        all_citys = {}
        for line in fp:
            #line = re.findall("new Array('(.*?)','(.*?)',", line)
            if not line == '\n':
                data = line.strip()
                # print(data)
                short, city_name = re.findall("Array\('(.*?)','(.*?)',", data)[0]
                city = [(city_name, short)]
                city = dict(city)
                all_citys.update(city)
    # 返回所有城市的字典 
    return all_citys



class XiaozhuSpider(scrapy.Spider):
    name = 'xiaozhu'
    allowed_domains = ['xiaozhu.com']
    # start_urls = ['http://xiaozhu.com/']

    def start_requests(self):

        with open(r'C:\Users\19609\Desktop\SpiderEnv\小猪短租\xiaozhuSpider\xiaozhuSpider\spiders\urls.txt', 'r') as fp:
            for line in fp:
                url = line.strip()
                yield scrapy.Request(url, callback=self.parse)

    # # 解析详情页
    def parse(self, response):
        #city = response.meta['city']
        # selectors = response.xpath("//ul[@class='pic_list clearfix']/li")
        # for selector in selectors:
        #     # 房子网页
        #     href = selector.xpath("./a/@href").extract_first()
        #     print(href)
        #     # print(href)
        #     # print('*'*80)
        _lodgeId = re.search('fangzi/(\d+)\.html', response.url).group(1)
        #     # print('#'*80)
        #     # print(_lodgeId)
        city = re.findall('://(.*?)\.', response.url)[0]
        if city:
            # 计算评论的id
            href = f'http://{city}.xiaozhu.com/ajaxRequest/Ajax_GetDetailComment?lodgeId={_lodgeId}&cityDomain=undefined&p=1'
            print(href)
            yield scrapy.Request(href, callback=self.parse_content)

        # # 翻页
        # next_page = response.xpath('//a[@class="font_st"]/@href').extract()
        # if len(next_page)==1:
        #     print(next_page[0])
        #     print('*'*80)
        #     yield scrapy.Request(next_page[0], callback=self.parse)
        # if len(next_page)==2:
        #     print(next_page[1])
        #     print('*'*80)
        #     yield scrapy.Request(next_page[1], callback=self.parse)


    # 解析评论
    def parse_content(self, response):

        # http://bj.xiaozhu.com/ajaxRequest/Ajax_GetDetailComment?lodgeId=27001562703&cityDomain=undefined&p=2

        _id = re.findall('lodgeId=(\d+)&cityDomain', response.url)[0]
        
        selectors = response.xpath('//div[@class="dp_con"]')
        for selector in selectors:
            # 入住时间
            _time = selector.xpath('.//if/text()').extract_first()
            # 客户名字
            _name = selector.xpath('.//span[@class="col_pink"]/text()').extract_first()
            # 房东回复
            _reply= selector.xpath('.//p/text()').extract_first()
            if _reply:
                _reply = _reply.strip()
            # 客户评价
            _content = selector.xpath('./text()').extract()
            _content = ''.join([content.strip() for content in _content if content])

            data = f'{_id},{_time},{_name},{_content},{_reply}'

            data = {
                'data': data
            }
            print(data)
            yield data
        
        # 评论内容翻页
        next_num = response.selector.re('pageNo <= (\d+)')
        if next_num and int(next_num[0])>=2:
            for num in range(2, int(next_num[0])+1):
                next_url = re.sub('&p=\d+', f'&p={num}', response.url)
                yield scrapy.Request(next_url, callback=self.parse_content)