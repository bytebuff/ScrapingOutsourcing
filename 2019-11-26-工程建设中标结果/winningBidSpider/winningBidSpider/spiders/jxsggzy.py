# -*- coding: utf-8 -*-
import json, re
import scrapy


class JxsggzySpider(scrapy.Spider):
    name = 'jxsggzy'  # 广西
    allowed_domains = ['jxsggzy.cn']

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        },
        'ITEM_PIPELINES': {
            'winningBidSpider.pipelines.WinningbidspiderPipelinejxsggzy': 304,
        },
        'DOWNLOAD_DELAY': .5,
        'JOBDIR': 'jxsggzy_request_seen'  # 当前项目下 断点续爬
    }

    # 列表页的网址

    def start_requests(self):
        for pageIndex in range(1, 143 + 1):
            # url = f'http://jxsggzy.cn/web/jyxx/002001/002001004/{pageIndex}.html'
            url2 = f'http://jxsggzy.cn/web/jyxx/002002/002002005/{pageIndex}.html'
            yield scrapy.Request(url=url2, callback=self.parse)

    def parse(self, response):
        # jsonData = json.loads(response.text)
        # jsonData = json.loads(jsonData['return'])
        # for dat in jsonData['Table']:
        #     print('*' * 80)
        #     print(dat)
        #     # 新的网址
        #     # categorynum
        #     categorynum = dat.get('categorynum')
        #     infoid = dat.get('infoid')
        #     postdate = dat.get('postdate')
        #     postdate = re.sub('-', '',postdate)
        #     detailUrl = f'http://jxsggzy.cn/web/jyxx/002001/{categorynum}/{postdate}/{infoid}.html'
        #     yield scrapy.Request(detailUrl, callback=self.parseDetail)

        # 重新写 上面的没有选择中标公示
        selectors = response.xpath('//div[@class="ewb-infolist"]/ul/li')
        for selector in selectors:
            detailUrl = selector.xpath('./a/@href').get()
            print(detailUrl)
            yield response.follow(detailUrl, callback=self.parseDetail)


    def parseDetail(self, response):
        # 招标单位名称
        jianSheDanWei = response.xpath('//span[contains(text(),"建设单位")]/../following-sibling::td/span/text()').get(default='')
        # 招标单位名称
        gongChengMingCheng = response.xpath('//span[contains(text(),"工程名称")]/../following-sibling::td/span/text()').get(default='')
        # 招标单位名称
        gongChengDiZhi = response.xpath('//span[contains(text(),"工程地址")]/../following-sibling::td/span/text()').get(default='')
        # 招标单位名称
        kaiBiaoShiJian = response.xpath('//span[contains(text(),"开标时间")]/../following-sibling::td/span/text()').get(default='')
        # 招标单位名称
        danWeiMingCheng = response.xpath('//span[contains(text(),"第一中标排序单位名称")]/../following-sibling::td/span/text()').get(default='')
        # 招标单位名称
        touBiaoZiZhi = response.xpath('//span[contains(text(),"投标资质")]/../following-sibling::td/span/text()').get(default='')
        # 招标单位名称
        touBiaoBaoJia = response.xpath('//span[contains(text(),"投标报价")]/../following-sibling::td/span/text()').get(default='')

        items = {
            'jianSheDanWei': jianSheDanWei,
            'gongChengMingCheng': gongChengMingCheng,
            'gongChengDiZhi': gongChengDiZhi,
            'kaiBiaoShiJian': kaiBiaoShiJian,
            'danWeiMingCheng': danWeiMingCheng,
            'touBiaoZiZhi': touBiaoZiZhi,
            'touBiaoBaoJia': touBiaoBaoJia,
        }
        yield items



