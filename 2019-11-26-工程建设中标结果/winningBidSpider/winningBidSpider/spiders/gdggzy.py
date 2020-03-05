# -*- coding: utf-8 -*-
import re
import scrapy
from .xpathRule import gdggzyRule


class GdggzySpider(scrapy.Spider):
    name = 'gdggzy'
    allowed_domains = ['dsg.gdggzy.org.cn']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        },
        'ITEM_PIPELINES': {
            'winningBidSpider.pipelines.WinningbidspiderPipelinegdggzy': 300,
        },
        'DOWNLOAD_DELAY': 1.,
        'JOBDIR': 'gdggzy_request_seen'  # 当前项目下 断点续爬
    }

    # start_urls = ['http://gdggzy.com/']

    def start_requests(self):
        url = 'http://dsg.gdggzy.org.cn:8080/Bigdata/InformationPublic/viewList.do?random=0.9781705019872275'
        for currPage in range(1, 923 + 1):
            formdata = {
                'pageSize': '20',
                'currPage': f'{currPage}',
                'noHeadAndFoot': '',
                'businessType': 'Construction',
                'releaseTime': '2018-11-14 00:00:00',
                'cityCode': '',
                'informationPublicType': 'CBResultAnnouncement',
                'title': ''
            }
            yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.parse)

    def parse(self, response):

        selectors = response.xpath('//tbody/tr')
        for selector in selectors:
            detailUrl = selector.xpath('./td[@class="txt-lf"]/a/@href').get()
            city = selector.xpath('./td[1]/em/text()').get()
            city = {
                'city': city
            }
            print(detailUrl)
            yield response.follow(detailUrl, callback=self.parseDetail, meta=city)

    # 处理详情页
    def parseDetail(self, response):

        city = response.meta['city']

        if '广州' in city:
            return gdggzyRule.ruleDetailZhongShan(response)
        if '深圳' in city:
            return gdggzyRule.ruleDetailShenZhen(response)
        if '佛山' in city:
            return gdggzyRule.ruleDetailFoShan(response)
        if '东莞' in city:
            return gdggzyRule.ruleDetailDongGuan(response)
        if '汕头' in city:
            return gdggzyRule.ruleDetailShanTou(response)
        if '惠州' in city:
            return gdggzyRule.ruleDetailHuiZhou(response)
        if '清远' in city:
            return gdggzyRule.ruleDetailQingYuan(response)
        if '珠海' in city:
            return gdggzyRule.ruleDetailZhuHai(response)
        if '茂名' in city:
            return gdggzyRule.ruleDetailMaoMing(response)
        if '潮州' in city:
            return gdggzyRule.ruleDetailChaoZhou(response)
        if '韶关' in city:
            return gdggzyRule.ruleDetailShaoGuan(response)
        if '河源' in city:
            return gdggzyRule.ruleDetailHeYuan(response)
        if '汕尾' in city:
            return gdggzyRule.ruleDetailShanWei(response)
        if '江门' in city:
            return gdggzyRule.ruleDetailJiangMen(response)
        if '阳江' in city:
            return gdggzyRule.ruleDetailYangJiang(response)
        if '揭阳' in city:
            return gdggzyRule.ruleDetailJieYang(response)
        if '梅州' in city:
            return gdggzyRule.ruleDetailMeiZhou(response)
        if '肇庆' in city:
            return gdggzyRule.ruleDetailZhaoQing(response)
        if '湛江' in city:
            return gdggzyRule.ruleDetailZhanJiang(response)
        if '云浮' in city:
            return gdggzyRule.ruleDetailYunFu(response)

