# -*- coding: utf-8 -*-
import json
import scrapy


class ShanghaiSpider(scrapy.Spider):
    name = 'shanghai'
    allowed_domains = ['222.66.64.149']

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        },
        'ITEM_PIPELINES': {
            'winningBidSpider.pipelines.WinningbidspiderPipelineshanghai': 302,
        },
        'DOWNLOAD_DELAY': .5,
        'JOBDIR': 'shanghai_request_seen'  # 当前项目下 断点续爬
    }

    start_urls = [
        f'http://222.66.64.149/publicity/transaction/page?page={page}&pageSize=10&columnStatus=3&timeZone=6&stageStatus=5'
        for page in range(1, 210 + 1)
    ]

    def parse(self, response):
        jsonData = json.loads(response.text)
        if jsonData.get('result').get('list'):
            for dat in jsonData['result']['list']:
                projectCode = dat.get('projectCode', '')
                print(projectCode)
                detailUrl = f'http://222.66.64.149/publicity/constructionWinner/{projectCode}'
                yield scrapy.Request(detailUrl, callback=self.parseDetail)

    def parseDetail(self, response):
        jsonData = json.loads(response.text)
        if jsonData.get('result'):
            dat = jsonData['result']
            # 招标人
            tenderName = dat.get('tenderName', '')
            # 项目名称
            projectName = dat.get('projectName', '')
            # 建设地点
            address = dat.get('address', '')
            # 中标人
            winBidderName = dat.get('winBidderName', '')
            # 中标金额
            evaluationPrice = dat.get('evaluationPrice', '')
            # 时间
            bidOpenTime = dat.get('bidOpenTime', '')

            items = {
                # 招标人
                'tenderName': tenderName,
                # 项目名称
                'projectName': projectName,
                # 建设地点
                'address': address,
                # 中标人
                'winBidderName': winBidderName,
                # 中标金额
                'evaluationPrice': evaluationPrice,
                # 时间
                'bidOpenTime': bidOpenTime,
            }
            yield items

