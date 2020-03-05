# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from extractor import Extractor

# 获取联系方式
extractor = Extractor()

class FobshanghaiSpider(scrapy.Spider):
    name = 'fobshanghai'
    allowed_domains = ['fobshanghai.com']
    start_urls = ['https://bbs.fobshanghai.com/index.php?gid=1']

    def parse(self, response):

        selectors = response.xpath('//tr[@class="row"]')
        for selector in selectors:
            category_url = selector.xpath('./td[@align="left"]/a[1]/@href').get() # 获取网址
            category_url = response.urljoin(category_url)
            print('分类页网址-->', category_url)
            # 采集分类名称
            # category_name = selector.xpath('./td[@align="left"]/a[1]/span/text()').get()
            yield scrapy.Request(category_url, callback=self.parse_list)


    def parse_list(self, response):

        # 提取详情页网址
        detailLinkExtractor = LinkExtractor(allow='thread-\d+-\d+-\d+\.html')
        urls = detailLinkExtractor.extract_links(response)
        for url in urls:
            print('详情页网址-->', url.url)
            yield scrapy.Request(url.url, callback=self.parse_detail)


        # 提取翻页网址
        # pageLinkExtractor = LinkExtractor(allow='forum-\d+-\d+\.html')
        # pageUrls = pageLinkExtractor.extract_links(response)
        # for pageUrl in pageUrls:
        #     print('详情页列表网址-->', pageUrl.url)
        #     yield scrapy.Request(pageUrl.url, callback=self.parse_list)
        #

    def parse_detail(self, response):

        # 提取数据
        selectors = response.xpath('//table[@class="t_msg"]') # 不要加tbody  没有这个东西 源码中
        for selector in selectors:
            msgComments = selector.xpath('.//div[@class="t_msgfont"]//text()').getall() # 获取网址
            msgTime = selector.xpath(".//div[contains(@style,'float:left')]/text()").get() # 获取网址

            msgComments = ''.join(msgComments)
            msgTime = msgTime.strip() if msgTime else ''

            # print(msgComments)
            # print(msgTime)


            emails = extractor.extract_emails(msgComments)
            wechats = extractor.extract_wechats(msgComments)
            qqs = extractor.extract_qqs(msgComments)
            cellphones = extractor.extract_cellphones(msgComments)
            if emails or wechats or qqs: # 只要有一个有值就保存
                print('邮箱-->', emails)
                print('微信-->', wechats)
                print('QQ-->', qqs)
                print('手机号', cellphones)

                # 处理成csv数据格式
                # csv_emails = ' '.join(emails)
                # csv_wechats = ' '.join(wechats)
                # csv_qqs = ' '.join(qqs)
                # csv_cellphones = ' '.join(cellphones)

                # csv_data = f'{csv_emails},{csv_wechats},{csv_qqs},{cellphones}'
                csv_list_data = [emails, wechats, qqs, cellphones]

                items = {
                    'items': csv_list_data
                }

                yield items

        # 提取翻页数据
        # pageLinkExtractor = LinkExtractor(allow='tid=\d+&extra=&page=\d+')
        # pageUrls = pageLinkExtractor.extract_links(response)
        # for pageUrl in pageUrls:
        #     print('详情页翻页网址-->', pageUrl.url)
        #     yield scrapy.Request(pageUrl.url, callback=self.parse_list)
