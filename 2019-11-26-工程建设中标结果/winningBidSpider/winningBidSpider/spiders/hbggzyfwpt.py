# -*- coding: utf-8 -*-
# 湖北
import json
import scrapy
from .xpathRule import hbggzyfwpt


class HbggzyfwptSpider(scrapy.Spider):
    name = 'hbggzyfwpt'
    allowed_domains = ['hbggzyfwpt.cn']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        },
        'ITEM_PIPELINES': {
            'winningBidSpider.pipelines.WinningbidspiderPipelinehbggzyfwpt': 301,
        },
        'DOWNLOAD_DELAY': .5,
        'JOBDIR': 'hbggzyfwpt_request_seen'  # 当前项目下 断点续爬
    }

    # 列表页的网址
    url = 'https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggs'
    # 详情页的网址
    projectCodeUrl = 'https://www.hbggzyfwpt.cn/jyxxAjax/jsgcZbjgDetail'

    def start_requests(self):
        for currPage in range(1, 1274 + 1):
            formdata = {
                'currentPage': f'{currPage}',
                'area': '000',
                'industriesTypeCode': '0',
                # 'scrollValue': '1217', # 不需要
                'bulletinName': '',
                'publishTimeType': '4',
                'publishTimeStart': '2018-11-01',
                'publishTimeEnd': '2019-11-01'
            }
            yield scrapy.FormRequest(url=self.url, formdata=formdata, callback=self.parse)

    def parse(self, response):
        selectors = response.xpath('//table//tr')
        for selector in selectors:
            detailUrl = selector.xpath('./td[1]/a/@href').get()
            # 平台  用来匹配不同平台的数据
            platform = selector.xpath('./td[2]/a/font/text()').get()
            platform = {
                'platform': platform,
                'detailUrl': 'https://www.hbggzyfwpt.cn' + detailUrl
            }
            yield response.follow(detailUrl, callback=self.getProjectCode, meta=platform)

    def getProjectCode(self, response):
        projectCode = response.xpath('//input[@name="projectCode"]/@value').get()
        if projectCode:
            formdata = {
                'projectCode': projectCode
            }
            yield scrapy.FormRequest(self.projectCodeUrl,
                                     formdata=formdata,
                                     callback=self.parseDetail,
                                     meta=response.meta)

    def parseDetail(self, response):
        platform = response.meta['platform']
        detailUrl = response.meta['detailUrl']
        # json数据解析
        jsonData = json.loads(response.text)

        if '武汉市' in platform:
            return hbggzyfwpt.ruleDetailWuHanShi(jsonData, detailUrl)
        if '湖北省' in platform:
            return hbggzyfwpt.ruleDetailShengJi(jsonData, detailUrl)
        if '黄石市' in platform:
            return hbggzyfwpt.ruleDetailHuangShiShi(jsonData, detailUrl)
        if '十堰市' in platform:
            return hbggzyfwpt.ruleDetailShiYanShi(jsonData, detailUrl)
        if '荆州市' in platform:
            return hbggzyfwpt.ruleDetailJinZhouShi(jsonData, detailUrl)
        if '宜昌市' in platform:
            return hbggzyfwpt.ruleDetailYiChangShi(jsonData, detailUrl)
        if '襄阳市' in platform:
            return hbggzyfwpt.ruleDetailXiangYangShi(jsonData, detailUrl)
        if '鄂州市' in platform:
            return hbggzyfwpt.ruleDetailXiangYangShi(jsonData, detailUrl)
        if '荆门市' in platform:
            return hbggzyfwpt.ruleDetailJinMenShi(jsonData, detailUrl)
        if '黄冈市' in platform:
            return hbggzyfwpt.ruleDetailHuangGangShi(jsonData, detailUrl)
        if '孝感市' in platform:
            return hbggzyfwpt.ruleDetailXiaoGanShi(jsonData, detailUrl)
        if '咸宁市' in platform:
            return hbggzyfwpt.ruleDetailXianNingShi(jsonData, detailUrl)
        if '随州市' in platform:
            return hbggzyfwpt.ruleDetailSuiZhouShi(jsonData, detailUrl)
        if '恩施市' in platform:
            return hbggzyfwpt.ruleDetailEnShiShi(jsonData, detailUrl)
        if '仙桃市' in platform:
            return hbggzyfwpt.ruleDetailXianTaoShi(jsonData, detailUrl)
        if '天门市' in platform:
            return hbggzyfwpt.ruleDetailTianMenShi(jsonData, detailUrl)
        if '潜江市' in platform:
            return hbggzyfwpt.ruleDetailQianJiangShi(jsonData, detailUrl)
        if '神农架' in platform:
            return hbggzyfwpt.ruleDetailShenNongJia(jsonData, detailUrl)