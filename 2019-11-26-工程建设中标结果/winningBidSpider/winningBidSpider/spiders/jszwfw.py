# -*- coding: utf-8 -*-
import json
import scrapy
from .xpathRule import jszwfwRule


class JszwfwSpider(scrapy.Spider):
    name = 'jszwfw' # 江苏
    allowed_domains = ['jszwfw.gov.cn']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        },
        'ITEM_PIPELINES': {
            'winningBidSpider.pipelines.WinningbidspiderPipelinejszwfw': 305,
        },
        'DOWNLOAD_DELAY': .5,
        'JOBDIR': 'jszwfw_request_seen'  # 当前项目下 断点续爬
    }

    # 列表页的网址
    def start_requests(self):
        for pageIndex in range(1, 50 + 1):
            url = 'http://jsggzy.jszwfw.gov.cn/inteligentsearch/rest/inteligentSearch/getFullTextData'
            formdata = {"token":"","pn":f"{(pageIndex-1)*20}","rn":"20","sdt":"","edt":"","wd":"null","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"infodatepx\":\"0\"}","ssort":"title","cl":"200","terminal":"","condition":[{"fieldName":"categorynum","isLike":"true","likeType":"2","equal":"003001008"}],"time":[{"fieldName":"infodatepx","startTime":"2019-08-26 00:00:00","endTime":"2019-11-26 23:59:59"}],"highlights":"title","statistics":"null","unionCondition":"null","accuracy":"","noParticiple":"1","searchRange":"null","isBusiness":"1"}
            yield scrapy.Request(url=url, method='POST', body=json.dumps(formdata), callback=self.parse)

    def parse(self, response):
        jsonData = json.loads(response.text)
        for dat in jsonData['result']['records']:
            linkurl = dat.get('linkurl')
            fieldvalue = {
                'fieldvalue': dat.get('fieldvalue')
            }
            yield response.follow(linkurl, callback=self.parseDetail, meta=fieldvalue)

    def parseDetail(self, response):

        fieldvalue = response.meta['fieldvalue']

        if fieldvalue in '南京市':
            return jszwfwRule.ruleDetailNanJingShi(response, fieldvalue)
        if fieldvalue in '无锡市':
            return jszwfwRule.ruleDetailWuXi(response, fieldvalue)
        if fieldvalue in '徐州市':
            return jszwfwRule.ruleDetailXuZhouShi(response, fieldvalue)
        if fieldvalue in '常州市':
            return jszwfwRule.ruleDetailChangZhouShi(response, fieldvalue)
        if fieldvalue in '苏州市':
            return jszwfwRule.ruleDetailSuZhouShi(response, fieldvalue)
        if fieldvalue in '南通市':
            return jszwfwRule.ruleDetailNanTongShi(response, fieldvalue)
        if fieldvalue in '连云港市':
            return jszwfwRule.ruleDetailLianYunGangShi(response, fieldvalue)
        if fieldvalue in '淮安市':
            return jszwfwRule.ruleDetailHuaiAnShi(response, fieldvalue)
        if fieldvalue in '盐城市':
            return jszwfwRule.ruleDetailYanChengShi(response, fieldvalue)
        if fieldvalue in '扬州市':
            return jszwfwRule.ruleDetailYangZhouShi(response, fieldvalue)
        if fieldvalue in '泰州市':
            return jszwfwRule.ruleDetailTaiZhouShi(response, fieldvalue)
        if fieldvalue in '宿迁市':
            return jszwfwRule.ruleDetailSuQianShi(response, fieldvalue)



