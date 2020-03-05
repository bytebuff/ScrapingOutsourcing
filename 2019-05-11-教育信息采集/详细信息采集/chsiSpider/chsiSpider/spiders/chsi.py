# -*- coding: utf-8 -*-
import re, json
import scrapy
from scrapy.linkextractors import LinkExtractor

def get_post_data():
    with open('post_data.txt', encoding='utf-8') as fp:
        for line in fp:
            line = line.strip()
            yield line

# # 读取 post_data
# for data in get_post_data():
#     data = re.sub('\'', '\"', data)
#     data = json.loads(data)
#     print(data)


class ChsiSpider(scrapy.Spider):
    name = 'chsi'
    allowed_domains = ['chsi.com.cn']
    # start_urls = ['http://chsi.com.cn/']

    city_data = [{"mc": "北京市", "dm": "11"},
                 {"mc": "天津市", "dm": "12"},
                 {"mc": "河北省", "dm": "13"},
                 {"mc": "山西省", "dm": "14"},
                 {"mc": "内蒙古自治区", "dm": "15"},
                 {"mc": "辽宁省", "dm": "21"},
                 {"mc": "吉林省", "dm": "22"},
                 {"mc": "黑龙江省", "dm": "23"},
                 {"mc": "上海市", "dm": "31"},
                 {"mc": "江苏省", "dm": "32"},
                 {"mc": "浙江省", "dm": "33"},
                 {"mc": "安徽省", "dm": "34"},
                 {"mc": "福建省", "dm": "35"},
                 {"mc": "江西省", "dm": "36"},
                 {"mc": "山东省", "dm": "37"},
                 {"mc": "河南省", "dm": "41"},
                 {"mc": "湖北省", "dm": "42"},
                 {"mc": "湖南省", "dm": "43"},
                 {"mc": "广东省", "dm": "44"},
                 {"mc": "广西壮族自治区", "dm": "45"},
                 {"mc": "海南省", "dm": "46"},
                 {"mc": "重庆市", "dm": "50"},
                 {"mc": "四川省", "dm": "51"},
                 {"mc": "贵州省", "dm": "52"},
                 {"mc": "云南省", "dm": "53"},
                 {"mc": "西藏自治区", "dm": "54"},
                 {"mc": "陕西省", "dm": "61"},
                 {"mc": "甘肃省", "dm": "62"},
                 {"mc": "青海省", "dm": "63"},
                 {"mc": "宁夏回族自治区", "dm": "64"},
                 {"mc": "新疆维吾尔自治区", "dm": "65"},
                 {"mc": "台湾省", "dm": "71"},
                 {"mc": "香港特别行政区", "dm": "81"},
                 {"mc": "澳门特别行政区", "dm": "82"}]

    post_url = 'https://yz.chsi.com.cn/zsml/queryAction.do'
    def start_requests(self):
        post_data = get_post_data()
        for data in post_data:
            data = re.sub('\'', '\"', data)
            data = json.loads(data)
            print(data)
            # data = {
            #     'ssdm': '31', # 城市
            #     'dwmc': '',
            #     'mldm': '08', # 门类
            #     'mlmc':'',
            #     'yjxkdm': '0809', # 学科类别
            #     'zymc': '电子科学与技术', # 专业
            #     'xxfs':''}
            yield scrapy.FormRequest(self.post_url, formdata=data, callback=self.parse)

    # 专业目录查询 第一个页面 有城市代码 学校代码
    def parse(self, response):
        # with open('zhanye.html', 'w', encoding='utf-') as fp:
        #     fp.write(response.text)

        selectors = response.xpath('//tbody/tr')
        for selector in selectors:
            # 选择网址
            url = selector.xpath('.//form/a/@href').get()
            url = response.urljoin(url)
            # 选择学校 代码
            school_code = selector.xpath('.//form/a/text()').get()
            # 城市代码
            city_code = selector.xpath('.//td[2]/text()').get()

            yield scrapy.Request(url, callback=self.parse_next, meta={'school_code': school_code, 'city_code': city_code})

        # linkextractor = LinkExtractor(allow='querySchAction')
        # urls = linkextractor.extract_links(response)
        # for url in urls:
        #     # print('专业网址', url.url)
        #     yield scrapy.Request(url.url, callback=self.parse_next, meta={'data': data})

    # 考试范围
    def parse_next(self, response):

        school_code = response.meta.get('school_code')
        city_code = response.meta.get('city_code')

        selectors = response.xpath('//tbody/tr')
        for selector in selectors:
            # 选择网址
            url = selector.xpath('.//td[8]/a/@href').get()
            url = response.urljoin(url)
            # 院系所
            yuan_xi = selector.xpath('.//td[2]/text()').get()
            # 专业
            zhuan_ye = selector.xpath('.//td[3]/text()').get()
            # 研究方向
            yan_jiu = selector.xpath('.//td[4]/text()').get()

            yield scrapy.Request(url, callback=self.parse_detail, meta={'school_code': school_code, 'city_code': city_code, 'yuan_xi': yuan_xi, 'zhuan_ye': zhuan_ye, 'yan_jiu': yan_jiu})


        # linkextractor = LinkExtractor(allow='/zsml/kskm')
        # urls = linkextractor.extract_links(response)
        # for url in urls:
        #     # print('大学网址：', url.url)
        #     yield scrapy.Request(url.url, callback=self.parse_detail, meta={'data': data})

    def parse_detail(self, response):
        school_code = response.meta.get('school_code')
        city_code = response.meta.get('city_code')
        yuan_xi = response.meta.get('yuan_xi')
        zhuan_ye = response.meta.get('zhuan_ye')
        yan_jiu = response.meta.get('yan_jiu')

        school_code_num, school_code_string = self.extract_num_code(school_code)
        city_code_num, city_code_string = self.extract_num_code(city_code)
        yuan_xi_num, yuan_xi_string = self.extract_num_code(yuan_xi)
        zhuan_ye_num, zhuan_ye_string = self.extract_num_code(zhuan_ye)
        yan_jiu_num, yan_jiu_string = self.extract_num_code(yan_jiu)

        # 提取数据
        # with open('detail.html', 'w', encoding='utf-8') as fp:
        #     fp.write(response.text)

        # 招生单位
        zhao_sheng = response.xpath('//td[text()="招生单位："]/./following-sibling::td[1]/text()').get()
        # 院系所
        yuan_xi = response.xpath('//td[text()="院系所："]/./following-sibling::td[1]/text()').get()
        # 专业代码
        zhuan_ye = response.xpath('//td[text()="专业代码："]/./following-sibling::td[1]/text()').get()
        # 研究方向
        yan_jiu = response.xpath('//td[text()="研究方向："]/./following-sibling::td[1]/text()').get()
        # 拟招人数
        ni_zhao = response.xpath('//td[text()="拟招人数："]/./following-sibling::td[1]/text()').get()
        # 考试方式
        kao_shi = response.xpath('//td[text()="考试方式："]/./following-sibling::td[1]/text()').get()
        # 跨专业
        kua_zhuan = response.xpath('//td[text()="跨专业："]/./following-sibling::td[1]/text()').get()
        # 学习方式
        xue_xi = response.xpath('//td[text()="学习方式："]/./following-sibling::td[1]/text()').get()
        # 指导老师
        zhi_dao = response.xpath('//td[text()="指导老师："]/./following-sibling::td[1]/text()').get()
        # 备注
        bei_zhu = response.xpath('//span[text()="备注："]/../following-sibling::td[1]/span/text()').get()

        # data_up = f'{school_code_num},{school_code_string},{city_code_num},{city_code_string},{yuan_xi_num},{yuan_xi_string},{zhuan_ye_num},{zhuan_ye_string},{yan_jiu_num},{yan_jiu_string},{zhao_sheng},{yuan_xi},{zhuan_ye},{yan_jiu},{ni_zhao},{kao_shi},{kua_zhuan},{xue_xi},{zhi_dao},{bei_zhu},'
        data_up = [school_code_num,school_code_string,city_code_num,city_code_string,yuan_xi_num,yuan_xi_string,zhuan_ye_num,zhuan_ye_string,yan_jiu_num,yan_jiu_string,zhao_sheng,yuan_xi,zhuan_ye,yan_jiu,ni_zhao,kao_shi,kua_zhuan,xue_xi,zhi_dao,bei_zhu]

        # 考试科目提取
        selectors = response.xpath('//table/tbody[@class="zsml-res-items"]')
        for selector in selectors:
            class_1 = selector.xpath('.//td[1]/text()').get().strip()
            class_2 = selector.xpath('.//td[2]/text()').get().strip()
            class_3 = selector.xpath('.//td[3]/text()').get().strip()
            class_4 = selector.xpath('.//td[4]/text()').get().strip()

            class_1_num, class_1_string = self.extract_num_code(class_1)
            class_2_num, class_2_string = self.extract_num_code(class_2)
            class_3_num, class_3_string = self.extract_num_code(class_3)
            class_4_num, class_4_string = self.extract_num_code(class_4)

            # data_dn = f'{class_1},{class_2},{class_3},{class_4}'
            data_dn = [class_1_num,class_1_string,class_2_num,class_2_string,class_3_num,class_3_string,class_4_num,class_4_string]
            data = data_up + data_dn

            items = {
                'data': data
            }
            yield items

    def extract_num_code(self, strings):
        try:
            num = re.search('\((.*?)\)(.*?)$', strings).group(1)
            string = re.search('\((.*?)\)(.*?)$', strings).group(2)
            return num, string
        except:
            return '',''