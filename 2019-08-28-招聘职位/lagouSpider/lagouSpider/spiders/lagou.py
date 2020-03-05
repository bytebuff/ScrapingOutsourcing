# -*- coding: utf-8 -*-
import scrapy
import json


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    def start_requests(self):

        city = getattr(self, 'city', False)
        if city == '北京':
            url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
        elif city == '西安':
            url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E8%A5%BF%E5%AE%89&needAddtionalResult=false'
        for page in range(1, 31):
            formdata = {
                'first': 'false',
                'pn': f'{page}',
                'kd': ''
            }
            yield scrapy.FormRequest(url, formdata=formdata, meta={'city': city})

    def parse(self, response):
        city = response.meta['city']
        json_data = json.loads(response.text)
        print(json_data)
        # positionName
        if json_data.get('content'):
            if json_data['content'].get('positionResult'):
                if json_data['content']['positionResult']:
                    if json_data['content']['positionResult'].get('result'):
                        for data in json_data['content']['positionResult']['result']:
                            positionName = data.get('positionName')
                            companyFullName = data.get('companyFullName')
                            companySize = data.get('companySize')
                            education = data.get('education')
                            salary = data.get('salary')
                            positionAdvantage = data.get('positionAdvantage')
                            item = {
                                'positionName': positionName,
                                'city': city,
                                'companyFullName': companyFullName,
                                'companySize': companySize,
                                'education': education,
                                'salary': salary,
                                'positionAdvantage': positionAdvantage

                            }
                            yield item