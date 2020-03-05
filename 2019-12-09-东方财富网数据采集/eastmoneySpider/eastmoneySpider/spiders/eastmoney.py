# -*- coding: utf-8 -*-
import json, re
import scrapy


class EastmoneySpider(scrapy.Spider):
    name = 'eastmoney'
    allowed_domains = ['eastmoney.com']
    start_urls = [
        f'http://86.push2.eastmoney.com/api/qt/clist/get?pn={pn}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=b:BK0164&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1575965946731'
        for pn in range(1, 11 + 1)]

    def parse(self, response):
        jsonData = json.loads(response.text)
        for dat in jsonData['data']['diff']:
            code = dat['f12']
            num = dat['f13']
            companyName = dat['f14']

            numCode = str(num) + '.' + code
            url = f'http://quote.eastmoney.com/unify/r/{numCode}'
            companyName = {
                'companyName': companyName
            }
            yield scrapy.Request(url, callback=self.parseDetail, meta=companyName)

    def parseDetail(self, response):
        print("当前网址是->>", response.url)
        code = re.search('com/(.*?).html', response.url).group(1)
        detailUrl = f'http://f10.eastmoney.com/NewFinanceAnalysis/DubangAnalysisAjax?code={code}'
        yield scrapy.Request(detailUrl, callback=self.parseJson, meta=response.meta)

    def parseJson(self, response):
        companyName = response.meta['companyName']  # 公司名字
        jsonData = json.loads(response.text)
        # 选择出数据
        for dat in jsonData['nd'][:3]:
            date = dat['date']  # 时间

            qjfy = dat['qjfy']  # 期间费用
            cwfy = dat['cwfy']  # 财务费用
            xsfy = dat['xsfy']  # 销售费用
            glfy = dat['glfy']  # 管理费用
            yysr = dat['yysr']  # 营业收入


            items = {
                'companyName': companyName,
                'date': date,
                'qjfy': qjfy,
                'cwfy': cwfy,
                'xsfy': xsfy,
                'glfy': glfy,
                'yysr': yysr
            }
            yield items
