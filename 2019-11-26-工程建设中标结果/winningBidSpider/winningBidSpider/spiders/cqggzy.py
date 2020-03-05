# -*- coding: utf-8 -*-
import json, re
import scrapy
from .xpathRule import cqggzyRule


class CqggzySpider(scrapy.Spider):
    name = 'cqggzy'  # 重庆
    allowed_domains = ['cqggzy.com']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        },
        'ITEM_PIPELINES': {
            'winningBidSpider.pipelines.WinningbidspiderPipelinecqggzy': 306,
        },
        'DOWNLOAD_DELAY': .5,
        'JOBDIR': 'cqggzy_request_seen'  # 当前项目下 断点续爬
    }

    def start_requests(self):
        for pageIndex in range(1, 1032 + 1):
            url = f'https://www.cqggzy.com/EpointWebBuilderService/getInfoListAndCategoryList.action?cmd=getInfoList&pageIndex={pageIndex}&pageSize=18&siteguid=d7878853-1c74-4913-ab15-1d72b70ff5e7&categorynum=005002001&title=&infoC=&_=1574938396244'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        jsonData = json.loads(response.text)
        jsonData = json.loads(jsonData['custom'])
        for dat in jsonData:
            infoid = dat.get('infoid')
            categorynum = dat.get('categorynum')
            infodate = dat.get('infodate')
            infodate = re.sub('-', '', infodate)
            detailUrl = f'https://www.cqggzy.com/jyjg/005002/{categorynum}/{infodate}/{infoid}.html'
            yield scrapy.Request(detailUrl, callback=self.parseDetail)

    def parseDetail(self, response):
        return cqggzyRule.ruleDetail(response)
