# -*- coding: utf-8 -*-
import scrapy
import json


class GaokaowSpider(scrapy.Spider):
    name = 'youzy'
    allowed_domains = ['youzy.cn']
    start_urls = [f'https://www.youzy.cn/tzy/search/colleges/collegeList?page={page}' for page in range(1, 2)]

    def parse(self, response):
        print('提取数据')
        # 提取数据
        selectors = response.xpath('//ul[@class="uzy-college-list "]/li')
        print(selectors)
        for selector in selectors:
            # url = selector.xpath('.//a[@class="name"]/@href').get()
            college_id = selector.xpath('.//button[@type="button"]/@data-collegeid').get()
            # 获取高考分数的值 先要传送这个网址  859是不变的 只有后面的collegeId是改变的
            url = f'https://www.youzy.cn/Data/ScoreLines/UCodes/QueryList?provinceId=859&collegeId={college_id}'

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
                # provinceName = data.get('provinceName')
                uCodeNum = data.get('uCodeNum')
                collegeName = data.get('collegeName')
                admissCode = data.get('admissCode')
                # collegeId = data.get('collegeId')
                # 获取高考分数
                # url = f'http://jdzzy.gaokaow.cc/Data/ScoreLines/Fractions/Professions/Query'
                # url = f'https://www.youzy.cn/Data/ScoreLines/Fractions/Colleges/Query'
                url = f'https://www.youzy.cn/Data/ScoreLines/Fractions/Professions/Query'

                item.update(
                    {
                        # 'provinceName': provinceName,
                        # 'uCodeNum': uCodeNum,
                        'collegeName': collegeName,
                        'admissCode': admissCode,
                        # 'collegeId': collegeId,
                    }
                )

                for year in range(2016, 2019): # 控制年份
                    for courseType in range(0, 2):
                        form_data = {
                            'batch': '0',
                            'courseType': f'{courseType}',
                            'uCode': f"{uCodeNum}",
                            'yearFrom': f'{year}',
                            'yearTo': f'{year}',
                        }
                        yield scrapy.FormRequest(url, method='POST', formdata=form_data, callback=self.parse_detail, meta=item)


    def parse_detail(self, response):

        item = response.meta

        json_data = json.loads(response.text)
        if json_data.get('result'):
            for data in json_data['result']:
                maxScore = data.get('maxScore') # 最高分
                minScore = data.get('minScore') # 最低分
                avgScore = data.get('avgScore') # 平均分
                lowSort = data.get('lowSort') # 最低位次
                enterNum = data.get('enterNum') # 录取数
                year = data.get('year') # 年份
                courseType = data.get('courseType') # 0 --> 理科  1 --> 文科
                professionCode = data.get('professionCode') # 专业代码
                professionName = data.get('professionName') # 专业名称
                remarks = data.get('remarks') # 专业名称
                professionName = professionName + remarks
                batchName = data.get('batchName') # 招生批次

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

                all_data = [item.get("collegeName"),item.get("li_shu"),item.get("xing_zhi"),item.get("pai_ming"),year,professionCode,professionName,courseType,batchName,maxScore,avgScore,minScore,lowSort,enterNum]

                items = {
                    'all_data': all_data
                }
                yield items