# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.commands import ScrapyCommand
from scrapy import cmdline

class GaokaowSpider(scrapy.Spider):
    name = 'gaokaow'
    allowed_domains = ['gaokaow.cc']
    start_urls = ['http://jdzzy.gaokaow.cc/tzySearch/colleges/search?page=3']

    def parse(self, response):
        # 提取数据
        selectors = response.xpath('//ul[@class="uzy-college-list"]/li')
        for selector in selectors:
            # url = selector.xpath('.//a[@class="name"]/@href').get()
            college_id = selector.xpath('.//button[@type="button"]/@data-collegeid').get()
            # 获取高考分数的值 先要传送这个网址  855是不变的 只有后面的collegeId是改变的
            url = f'http://jdzzy.gaokaow.cc/Data/ScoreLines/UCodes/QueryList?provinceId=855&collegeId={college_id}'

            # 表单构造不成功  没有comment-type ??

            # formdata = {
            #     'provinceId': '855',
            #     'collegeId': f'{college_id}'
            # }
            # print(formdata)

            school_name = selector.xpath('.//a[@class="name"]/text()').get()
            school_name = school_name.strip() if school_name else ''

            li_shu = selector.xpath('.//ul/li[@class="quarter_1"]/text()').get()
            li_shu = ''.join([li.strip() for li in list(li_shu)])

            xing_zhi = selector.xpath('.//ul/li[@class="quarter_2"]/text()').get()
            xing_zhi = ''.join([xing.strip() for xing in list(xing_zhi)])

            pai_ming = selector.xpath('.//div[@class="rank"]//span/text()').get()
            pai_ming = pai_ming.strip() if pai_ming else ''

            item = {
                'school_name': school_name,
                'li_shu': li_shu,
                'xing_zhi': xing_zhi,
                'pai_ming': pai_ming,
            }

            yield scrapy.FormRequest(url, method='POST', callback=self.parse_extract, meta=item)

    # 提取 uCodeNum
    def parse_extract(self, response):

        item = response.meta

        # school_name = response.meta.get('school_name')
        # li_shu = response.meta.get('li_shu')
        # xing_zhi = response.meta.get('xing_zhi')
        # pai_ming = response.meta.get('pai_ming')

        json_data = json.loads(response.text)
        if json_data.get('result'):
            for data in json_data['result']:
                provinceName = data.get('provinceName')
                uCodeNum = data.get('uCodeNum')
                collegeName = data.get('collegeName')
                collegeId = data.get('collegeId')
                # 获取高考分数
                url = f'http://jdzzy.gaokaow.cc/Data/ScoreLines/Fractions/Colleges/Query?provinceNumId=855&ucode={uCodeNum}'



                item.update(
                    {
                        'provinceName': provinceName,
                        'uCodeNum': uCodeNum,
                        'collegeName': collegeName,
                        'collegeId': collegeId,
                    }
                )

                yield scrapy.FormRequest(url, method='POST', callback=self.parse_detail, meta=item)

    def parse_detail(self, response):

        item = response.meta

        json_data = json.loads(response.text)
        if json_data.get('result'):
            for data in json_data['result']:
                maxScore = data.get('maxScore')
                minScore = data.get('minScore')
                enterNum = data.get('enterNum')
                batchName = data.get('batchName')
                year = data.get('year')
                course = data.get('course') # 0 --> 理科  1 --> 文科

                # item.update(
                #     {
                #         'maxScore':maxScore,
                #         'minScore':minScore,
                #         'enterNum':enterNum,
                #         'batchName':batchName,
                #         'year':year,
                #         'course':course,
                #     }
                # )

                all_data = [item.get("school_name"),item.get("li_shu"),item.get("xing_zhi"),item.get("pai_ming"),item.get("collegeName"),maxScore,minScore,enterNum,batchName,year,course]

                items = {
                    'all_data': all_data
                }
                yield items