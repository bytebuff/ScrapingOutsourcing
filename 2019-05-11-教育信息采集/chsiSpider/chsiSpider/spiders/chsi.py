# -*- coding: utf-8 -*-
import scrapy


class ChsiSpider(scrapy.Spider):
    name = 'chsi'
    allowed_domains = ['chsi.com.cn']
    start_urls = [f'https://yz.chsi.com.cn/sch/?start={page}' for page in range(1,880, 20)]

    def parse(self, response):
        selectors = response.xpath('//table//tr')
        for selector in selectors:
            # 院校名称
            school_xxmc = selector.xpath('./td[1]/a/text()').get()
            school_xxmc = school_xxmc.strip() if school_xxmc else ''
            # 所在地
            school_szd = selector.xpath('./td[2]/text()').get()
            school_szd = school_szd.strip() if school_szd else ''


            school_yxls = selector.xpath('./td[3]/text()').get()
            school_yxls = school_yxls.strip() if school_yxls else ''

            school_texing = selector.xpath('./td[4]/span/text()').getall()
            if len(school_texing)==2:
                school_texing = ','.join(school_texing)
            elif len(school_texing)==1:
                school_texing = ','.join(school_texing)
                if '985' in school_texing:
                    school_texing = school_texing + ','
                if '211' in school_texing:
                    school_texing = ',' + school_texing
            else:
                school_texing = ','

            school_texing = school_texing.strip() if school_texing else ''


            school_yjsy = selector.xpath('./td[5]/i/text()').get()
            school_yjsy = 1 if school_yjsy== '\ue664' else 0

            school_zhxyx = selector.xpath('./td[6]/i/text()').get()
            school_zhxyx = 1 if school_zhxyx== '\ue664' else 0



            # items = {
            #     '院校名称': school_xxmc,
            #     '所在地': school_szd,
            #     '院校隶属': school_yxls,
            #     '院校特性': school_texing,
            #     '研究生院': school_yjsy,
            #     '自划线院校': school_zhxyx,
            # }

            data = f'{school_xxmc},{school_szd},{school_yxls},{school_texing},{school_yjsy},{school_zhxyx}'

            items = {
                'data': data
            }

            yield items