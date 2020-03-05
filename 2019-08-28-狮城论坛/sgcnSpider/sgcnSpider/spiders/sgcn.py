# -*- coding: utf-8 -*-
import scrapy
from .baidu_aip import basicGeneralUrl


class SgcnSpider(scrapy.Spider):
    name = 'sgcn'
    allowed_domains = ['sgcn.com']

    def start_requests(self):
        # 设置版块  空运海运
        block = getattr(self, 'block', False)

        if block == '空运海运':
            url = 'https://bbs.sgcn.com/forum-220-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '票券转让':
            url = 'https://bbs.sgcn.com/forum-1265-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '美食街':
            url = 'https://bbs.sgcn.com/forum-212-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '机票旅游':
            url = 'https://bbs.sgcn.com/forum-215-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '房屋买卖':
            url = 'https://bbs.sgcn.com/forum-1253-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '整套出租':
            url = 'https://bbs.sgcn.com/forum-234-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '商业地产':
            url = 'https://bbs.sgcn.com/forum-1254-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '主人房出租':
            url = 'https://bbs.sgcn.com/forum-1231-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '普通房出租':
            url = 'https://bbs.sgcn.com/forum-138-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '隔间/佣人房':
            url = 'https://bbs.sgcn.com/forum-1235-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '床位搭房':
            url = 'https://bbs.sgcn.com/forum-1251-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '短期日租':
            url = 'https://bbs.sgcn.com/forum-235-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '宿舍与寄宿':
            url = 'https://bbs.sgcn.com/forum-1233-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '母婴市场':
            url = 'https://bbs.sgcn.com/forum-1209-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '爱心宠物':
            url = 'https://bbs.sgcn.com/forum-140-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '服装配饰':
            url = 'https://bbs.sgcn.com/forum-161-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '鞋帽箱包':
            url = 'https://bbs.sgcn.com/forum-1245-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '美容美发':
            url = 'https://bbs.sgcn.com/forum-1205-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '健康产品':
            url = 'https://bbs.sgcn.com/forum-1246-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '来新劳务':
            url = 'https://bbs.sgcn.com/forum-177-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '求职招聘':
            url = 'https://bbs.sgcn.com/forum-1255-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '家政服务':
            url = 'https://bbs.sgcn.com/forum-218-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '家具家俬':
            url = 'https://bbs.sgcn.com/forum-10-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '家用电器':
            url = 'https://bbs.sgcn.com/forum-1248-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '居家日用':
            url = 'https://bbs.sgcn.com/forum-162-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '摄影器材':
            url = 'https://bbs.sgcn.com/forum-243-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '电脑电子':
            url = 'https://bbs.sgcn.com/forum-197-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '手机与平板':
            url = 'https://bbs.sgcn.com/forum-160-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '体育世界':
            url = 'https://bbs.sgcn.com/forum-15-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '设计与印刷':
            url = 'https://bbs.sgcn.com/forum-1250-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '车辆交易':
            url = 'https://bbs.sgcn.com/forum-1221-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '留学广告':
            url = 'https://bbs.sgcn.com/forum-253-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '书籍与教材':
            url = 'https://bbs.sgcn.com/forum-1223-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '家教补习':
            url = 'https://bbs.sgcn.com/forum-1206-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '音乐与舞蹈':
            url = 'https://bbs.sgcn.com/forum-65-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '移民经商':
            url = 'https://bbs.sgcn.com/forum-157-1.html'
            yield scrapy.Request(url, callback=self.parse)
        if block == '谈婚论嫁':
            url = 'https://bbs.sgcn.com/forum-1259-1.html'
            yield scrapy.Request(url, callback=self.parse)
       
    # 处理列表页
    def parse(self, response):

        # 提取详情页的网址
        urls = response.xpath('//td[@class="icn"]/a/@href').extract()
        for url in urls:
            # 发出请求 处理详情页
            yield scrapy.Request(url, callback=self.parse_detail)

        # # 翻页
        next_url = response.xpath('//a[@class="nxt"]/@href').extract_first()
        if next_url:
            # 回调自己
            yield scrapy.Request(next_url, callback=self.parse)

	# 处理详情页
    def parse_detail(self, response):

        # 提取时间
        _time = response.xpath('//div[@class="authi"]//span/@title').extract_first()
        if not _time:
            _time = response.xpath('//div[@class="authi"]/em/text()').extract_first()
        print(_time)
        # 提取电话de网址 因为电话是图片
        _phoneUrl = response.xpath('//th[text()="电话:"]/following-sibling::td/img/@src').extract_first()
        _phone = ''
        if _phoneUrl:
            _phoneUrl = response.urljoin(_phoneUrl)
			# 直接识别网络图片中的字体
            text = basicGeneralUrl(_phoneUrl)
            if text.get('words_result', False):
                if text['words_result'][0:]:
                    _phone = text['words_result'][0].get('words', None)

        # 提取邮箱
        _email = response.xpath('//th[text()="邮箱:"]/following-sibling::td/text()').extract_first()
        # 提取QQ号码
        # _QQ = response.xpath('').extract_first()
        # 提取微信
        _wechat = response.xpath('//th[text()="微信:"]/following-sibling::td/text()').extract_first()

        # data = {
        #     '发布时间': _time,
        #     '电话号码': _phone,
        #     '邮箱号码': _email,
        #     '微信号码': _wechat
        # }

        data = f'{_time},{_phone},{_email},{_wechat},{response.url}'

        data = {
            'data': data
        }

        yield data