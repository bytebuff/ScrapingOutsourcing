# -*- coding: utf-8 -*-
import json
import scrapy
from parsel import Selector


class GgzyjySpider(scrapy.Spider):
    name = 'ggzyjy'  # 四川
    allowed_domains = ['ggzyjy.sc.gov.cn']
    url = 'http://ggzyjy.sc.gov.cn/inteligentsearch/rest/inteligentSearch/getFullTextData'
    COOKIES_ENABLED = False
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            # 'Accept-Encoding': 'gzip, deflate',
            # 'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            # 'Connection': 'keep-alive',
            # 'Content-Length': '532',
            # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'JSESSIONID=C54C4C3FA646D1A0FF671B3D208F79BA; UM_distinctid=16e9b0cf3b615d-004b806e08fc9f-7711b3e-100200-16e9b0cf3b7245; CNZZDATA1276636503=794109402-1574554252-%7C1574554252; userGuid=-31722750',
            'Host': 'ggzyjy.sc.gov.cn',
            'Origin': 'http://ggzyjy.sc.gov.cn',
            'Pragma': 'no-cache',
            'Referer': 'http://ggzyjy.sc.gov.cn/jyxx/transactionInfo.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            # 'X-Requested-With': 'XMLHttpRequest',
        },
        'ITEM_PIPELINES': {
            'winningBidSpider.pipelines.WinningbidspiderPipelineggzyjy': 303,
        },
        'DOWNLOAD_DELAY': .5,
        'JOBDIR': 'ggzyjy_request_seen'  # 当前项目下 断点续爬
    }

    def start_requests(self):
        for currPage in range(1, 61 + 1):
            formdata = {"token": "", "pn": f"{(currPage - 1) * 12}", "rn": "12", "sdt": "", "edt": "", "wd": "",
                        "inc_wd": "",
                        "exc_wd": "", "fields": "title", "cnum": "", "sort": "{'webdate':'0'}", "ssort": "title",
                        "cl": "500", "terminal": "",
                        "condition": '[{"fieldName":"categorynum","equal":"002001006","notEqual":null,"equalList":null,"notEqualList":null,"isLike":true,"likeType":2}]',
                        "time": '[{"fieldName":"webdate","startTime":"2018-11-1 00:00:00","endTime":"2019-11-1 23:59:59"}]',
                        "highlights": "", "statistics": "null", "unionCondition": "null", "accuracy": "",
                        "noParticiple": "0", "searchRange": "null", "isBusiness": "1"}
            # 这个请求需要JSON格式提交 必须JSON格式提交 明明是表单 开发人员闹着玩？？YouCantFuckMe
            yield scrapy.Request(url=self.url, method="POST", body=json.dumps(formdata), callback=self.parse)

    def parse(self, response):
        # print(response.text)
        jsonData = json.loads(response.text)
        if jsonData.get('result', '').get('records', ''):
            for dat in jsonData['result']['records']:
                linkurl = dat.get('linkurl')
                yield response.follow(linkurl, callback=self.parseDetail)

    def parseDetail(self, response):
        dataValue = response.xpath('//span[@id="relateinfoid"]/@data-value').get()
        dataTarget = response.xpath('//li/a[contains(text(),"评标结果")]/@data-value').get()
        url = f'http://ggzyjy.sc.gov.cn/staticJson/{dataValue}/{dataTarget}.json'
        yield scrapy.Request(url, callback=self.parseJson)

    def parseJson(self, response):

        jsonData = json.loads(response.text)

        for dat in jsonData['data']:
            infoContent = dat.get('infoContent')

            zhuanzai = dat.get('zhuanzai')

            selectors = Selector(text=infoContent)
            # 项目及标段名称
            title = selectors.xpath('//td[contains(text(),"项目及标段名称")]/following-sibling::td/text()').get(default='')
            # 招标人
            zhaoBiaoRen = selectors.xpath('//td[text()="招标人"]/following-sibling::td[1]/text()').get(default='')
            # 开标时间
            shiJian = selectors.xpath('//td[text()="开标时间"]/following-sibling::td/text()').get(default='')
            # 第一名
            diYiMing = selectors.xpath(
                '//th[contains(text(),"第一")]/following-sibling::th[@name="CandidateName"]/text()').get(default='')
            if not diYiMing:
                diYiMing = selectors.xpath(
                    '//th[contains(text(),"第一")]/following-sibling::td[@name="CandidateName"]/text()').get(default='')
            # 竞标价
            jingBiaoJia = selectors.xpath(
                '//th[contains(text(),"第一")]/following-sibling::th[@name="OfferFile"]/text()').get(default='')
            if not jingBiaoJia:
                jingBiaoJia = selectors.xpath(
                    '//th[contains(text(),"第一")]/following-sibling::td[@name="OfferFile"]/text()').get(default='')

            # 职称
            zhiCheng = selectors.xpath('//td[text()="项目技术负责人"]/following-sibling::td[4]/text()').get(default='')

            items = {
                'title': title,
                'zhaoBiaoRen': zhaoBiaoRen,
                'shiJian': shiJian,
                'diYiMing': diYiMing,
                'jingBiaoJia': jingBiaoJia,
                'zhiCheng': zhiCheng,
                'zhuanzai': zhuanzai,
            }
            yield items


class GgzyjySpider61(scrapy.Spider):
    name = 'ggzyjy61'  # 四川
    allowed_domains = ['ggzyjy.sc.gov.cn']
    url = 'http://ggzyjy.sc.gov.cn/inteligentsearch/rest/inteligentSearch/getFullTextData'
    url61 = 'http://ggzyjy.sc.gov.cn/WebBuilder/rest/searchindb/get'
    COOKIES_ENABLED = False
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            # 'Accept-Encoding': 'gzip, deflate',
            # 'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            # 'Connection': 'keep-alive',
            # 'Content-Length': '532',
            # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'JSESSIONID=C54C4C3FA646D1A0FF671B3D208F79BA; UM_distinctid=16e9b0cf3b615d-004b806e08fc9f-7711b3e-100200-16e9b0cf3b7245; CNZZDATA1276636503=794109402-1574554252-%7C1574554252; userGuid=-31722750',
            'Host': 'ggzyjy.sc.gov.cn',
            'Origin': 'http://ggzyjy.sc.gov.cn',
            'Pragma': 'no-cache',
            'Referer': 'http://ggzyjy.sc.gov.cn/jyxx/transactionInfo.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            # 'X-Requested-With': 'XMLHttpRequest',
        },
        'ITEM_PIPELINES': {
            'winningBidSpider.pipelines.WinningbidspiderPipelineggzyjy': 303,
        },
        'DOWNLOAD_DELAY': .5,
        'JOBDIR': 'ggzyjy61_request_seen'  # 当前项目下 断点续爬
    }

    def start_requests(self):
        for currPage in range(60, 1319 + 1):
            formdata = {
                'fuTitle': '',
                'pageIndex': f'{currPage - 1}',
                'strDate': '2018-11-1+00%3A00%3A00',
                'endDate': '2019-11-1+23%3A59%3A59',
                'categorynum': '002001006',
                'jyResource': '000',
                'tradeType': 'no',
            }
            # 这个请求需要JSON格式提交 必须JSON格式提交 明明是表单 开发人员闹着玩？？YouCantFuckMe
            yield scrapy.FormRequest(url=self.url61, method="POST", formdata=formdata, callback=self.parse)

    def parse(self, response):
        # print(response.text)
        jsonData = json.loads(response.text)
        if jsonData.get('infodata', ''):
            for dat in jsonData['infodata']:
                linkurl = dat.get('visiturl')
                zhuanzai = dat.get('zhuanzai')
                zhuanzai = {
                    'zhuanzai': zhuanzai
                }
                yield response.follow(linkurl, callback=self.parseDetail, meta=zhuanzai)

    def parseDetail(self, response):
        selectors = Selector(text=response.text)
        # 项目及标段名称
        title = selectors.xpath('//td[contains(text(),"项目及标段名称")]/following-sibling::td/text()').get(default='')
        # 招标人
        zhaoBiaoRen = selectors.xpath('//td[text()="招标人"]/following-sibling::td[1]/text()').get(default='')
        # 开标时间
        shiJian = selectors.xpath('//td[text()="开标时间"]/following-sibling::td/text()').get(default='')
        # 第一名
        diYiMing = selectors.xpath(
            '//th[contains(text(),"第一")]/following-sibling::th[@name="CandidateName"]/text()').get(default='')
        if not diYiMing:
            diYiMing = selectors.xpath(
                '//th[contains(text(),"第一")]/following-sibling::td[@name="CandidateName"]/text()').get(default='')
        # 竞标价
        jingBiaoJia = selectors.xpath(
            '//th[contains(text(),"第一")]/following-sibling::th[@name="OfferFile"]/text()').get(default='')
        if not jingBiaoJia:
            jingBiaoJia = selectors.xpath(
                '//th[contains(text(),"第一")]/following-sibling::td[@name="OfferFile"]/text()').get(default='')

        # 职称
        zhiCheng = selectors.xpath('//td[text()="项目技术负责人"]/following-sibling::td[4]/text()').get(default='')

        items = {
            'title': title,
            'zhaoBiaoRen': zhaoBiaoRen,
            'shiJian': shiJian,
            'diYiMing': diYiMing,
            'jingBiaoJia': jingBiaoJia,
            'zhiCheng': zhiCheng,
            **response.meta
        }
        yield items
