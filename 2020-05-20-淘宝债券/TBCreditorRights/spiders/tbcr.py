# -*- coding: utf-8 -*-
import json, re, time, redis
import scrapy
from scrapy import signals
from scrapy.exceptions import DontCloseSpider
from scrapy.http import TextResponse
from ..utils import daybyday
from ..items import TbItemLoader, TbcreditorrightsItem
from twisted.internet.defer import inlineCallbacks
from scrapy.loader.processors import TakeFirst, Compose, Identity, MapCompose, Join


class TbcrSpider(scrapy.Spider):
    name = 'tbcr'
    allowed_domains = ['taobao.com']
    # start_urls = [
    #     f'https://zc-paimai.taobao.com/zc_item_list.htm?auction_source=0&front_category=56956002&st_param=-1&auction_start_seg=0&auction_start_from={day}&auction_start_to={day}'
    #     for day in daybyday('2020-01-01', '2020-01-02')]

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(TbcrSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_idle, signal=signals.spider_idle)
        return spider

    def start_requests(self):
        yield self.next_req()

    def next_req(self):
        redis_cli = redis.StrictRedis(host='127.0.0.1', port=6379, db=0, decode_responses=True)
        url = str(redis_cli.blpop('tbcr')[1])
        print(url)
        return scrapy.Request(url)

    def spider_idle(self, spider):

        request = self.next_req()
        if request:
            self.crawler.engine.schedule(request, self)
        else:
            time.sleep(2)
        raise DontCloseSpider

    def parse(self, response):
        # 提取网页中的JSON信息 在列表页
        json_data_string = response.xpath('//script[@id="sf-item-list-data"]/text()').get()
        json_data_dict = json.loads(json_data_string)
        for list_data in json_data_dict['data']:
            url = 'https:' + list_data['itemUrl']
            yield scrapy.Request(url=url, callback=self.parse_detail, meta={'list_data': list_data})

        # 翻页
        next_url = response.xpath('//a[@class="next"]/@href').get()
        if next_url:
            next_page = 'https:' + next_url.lstrip()
            yield scrapy.Request(url=next_page, callback=self.parse)

    @inlineCallbacks
    def parse_detail(self, response):
        list_data = response.meta['list_data']

        list_item_loader = TbItemLoader(item=TbcreditorrightsItem(), response=response)
        list_item_loader.add_value('bid_type', '债权') # 标的物类型
        list_item_loader.add_value('bid_start_time', list_data.get('start', '')) # 标的物开拍时间的开始时间
        list_item_loader.add_value('bid_end_time', list_data.get('end', '')) # 标的物开拍时间的结束时间
        list_item_loader.add_value('onlookers_number', list_data.get('viewerCount', '')) # 围观人数
        list_item_loader.add_value('sign_up_number', list_data.get('applyCount', '')) # 报名人数
        list_item_loader.add_value('title', list_data.get('title', '')) # 标题
        list_item_loader.add_value('page_url', response.url) # 网页地址

        list_item_loader.add_xpath('auction_rounds', '//h1/text()') # 拍卖轮次
        list_item_loader.add_xpath('starting_price', '//span[contains(text(), "起 始 价")]/following-sibling::span/span/text()') # 起始价
        list_item_loader.add_xpath('margin', '//span[contains(text(), "保 证 金")]/following-sibling::span/span/text()') # 保证金
        list_item_loader.add_xpath('assessment_price', '//span[contains(text(), "评 估 价")]/following-sibling::span/span/text()') # 评估价
        list_item_loader.add_xpath('price_rate_increase', '//span[contains(text(), "加价幅度")]/following-sibling::span/span/text()') # 加价幅度
        list_item_loader.add_xpath('sale_cycle', '//span[contains(text(), "竞价周期")]/following-sibling::span/text()') # 竞价周期
        list_item_loader.add_xpath('delaytime_cycle', '//span[contains(text(), "竞价周期")]/following-sibling::span[1]/text()') # 延时周期
        list_item_loader.add_xpath('preferred_purchase', '//span[contains(text(), "优先购买权人")]/following-sibling::span[1]/text()') # 优先购买权人

        list_item_loader.add_xpath('transaction_price', '//span[contains(text(), "成交价")]/following-sibling::div//span/em/text()') # 成交价
        list_item_loader.add_xpath('completion_time', '//span[contains(@class,"countdown")]/text()') # 完成时间
        list_item_loader.add_xpath('disposal_unit', '//span[contains(text(), "处置单位")]/following-sibling::span/a/text()') # 处置单位

        list_item_loader.add_xpath('bid_province', '//div[@id="itemAddress"]/text()', re='\A(.*?) ') # 标的物所在省
        list_item_loader.add_xpath('bid_city', '//div[@id="itemAddress"]/text()', re=' (.*?) ') # 标的物所在市
        list_item_loader.add_xpath('bid_area', '//div[@id="itemAddress"]/text()') # 标的物所在区

        # 设置提醒人数
        set_reminders_url = f'https://paimai.taobao.com/json/getSubscribersNum?itemIds={list_data.get("id", "")}'
        set_reminders_req = scrapy.Request(url=set_reminders_url, callback=self.parse_detail)
        set_reminders_res = yield self.crawler.engine.download(set_reminders_req, self)
        list_item_loader.add_value('set_reminders', set_reminders_res.text, re='"subscribersNum":(\d+)}')


        # 标的物详情描述
        bid_url = f'https://zc-paimai.taobao.com/json/get_pc_desc.htm?item_id={list_data.get("id", "")}'
        bid_req = scrapy.Request(url=bid_url, callback=self.parse_detail)
        bid_res = yield self.crawler.engine.download(bid_req, self)
        unicode_escape_res = bid_res.text.encode('utf-8').decode('unicode_escape')
        unicode_escape_res_re = re.sub('\s', '', unicode_escape_res)
        # unicode_escape_res = TextResponse(url=bid_res.url, request=bid_req, body=bid_res.text.encode('utf-8').decode('unicode_escape'), encoding='gbk')

        list_item_loader.add_value('guarantee_method', unicode_escape_res_re, TakeFirst(), re='>担保方式：<.*?">(.*?)<') # 担保方式
        list_item_loader.add_value('principal_creditor_rights', unicode_escape_res_re, TakeFirst(), re='>债权本金：<.*?">(.*?)<') # 债权本金
        list_item_loader.add_value('no_interest', unicode_escape_res_re, TakeFirst(), re='>未尝利息：<.*?">(.*?)<') # 未尝利息
        list_item_loader.add_value('base_date', unicode_escape_res_re, TakeFirst(), re='>基准日：<.*?">(.*?)<') # 基准日
        list_item_loader.add_value('principal_interest_total', unicode_escape_res_re, TakeFirst(), re='>本息合计：<.*?">(.*?)<') # 本息合计
        list_item_loader.add_value('debtor_name', unicode_escape_res_re, TakeFirst(), re='>债务人名称：<.*?">(.*?)<') # 债务人名称

        list_item_loader.add_value('debtor_info', unicode_escape_res_re, TakeFirst(), re='>债务人信息：<.*?">(.*?)<') # 债务人信息-
        list_item_loader.add_value('creditor_info', unicode_escape_res_re, TakeFirst(), re='>债权人信息：<.*?">(.*?)<') # 债权人信息-
        list_item_loader.add_value('creditor_name', unicode_escape_res_re, TakeFirst(), re='>债权人名称：<.*?">(.*?)<') # 债权人名称-
        list_item_loader.add_value('creditor_balance', unicode_escape_res_re, TakeFirst(), re='>债权余额：<.*?">(.*?)<') # 债权余额-
        list_item_loader.add_value('principal_amount', unicode_escape_res_re, TakeFirst(), re='>本金金额：<.*?">(.*?)<') # 本金金额-
        list_item_loader.add_value('interest_amount', unicode_escape_res_re, TakeFirst(), re='>利息金额：<.*?">(.*?)<') # 利息金额-
        list_item_loader.add_value('loans_monthly_interest_rate', unicode_escape_res_re, TakeFirst(), re='>贷款月利率：<.*?">(.*?)<') # 贷款月利率-
        list_item_loader.add_value('loans_release_date', unicode_escape_res_re, TakeFirst(), re='>贷款发放日：<.*?">(.*?)<') # 贷款发放日-
        list_item_loader.add_value('loan_maturity_date', unicode_escape_res_re, TakeFirst(), re='>贷款到期日：<.*?">(.*?)<') # 贷款到期日-
        list_item_loader.add_value('collateral', unicode_escape_res_re, TakeFirst(), re='>有无抵押：<.*?">(.*?)<') # 有无抵押-
        list_item_loader.add_value('collateral_total_price', unicode_escape_res_re, TakeFirst(), re='>抵押总评估价：<.*?">(.*?)<') # 抵押总评估价-
        list_item_loader.add_value('collateral_info', unicode_escape_res_re, TakeFirst(), re='>抵押信息：<.*?">(.*?)<') # 抵押信息-
        list_item_loader.add_value('guarantor', unicode_escape_res_re, TakeFirst(), re='>有无担保人：<.*?">(.*?)<') # 有无担保人-
        list_item_loader.add_value('guarantor_name', unicode_escape_res_re, TakeFirst(), re='>担保人：<.*?">(.*?)<') # 担保人-
        list_item_loader.add_value('guarantor_info', unicode_escape_res_re, TakeFirst(), re='>担保人信息：<.*?">(.*?)<') # 担保人信息-
        list_item_loader.add_value('guarantor_amount', unicode_escape_res_re, TakeFirst(), re='>担保金额：<.*?">(.*?)<') # 担保金额-
        list_item_loader.add_value('guarantor_method', unicode_escape_res_re, TakeFirst(), re='>担保形式：<.*?">(.*?)<') # 担保形式-
        list_item_loader.add_value('litigation_status', unicode_escape_res_re, TakeFirst(), re='>诉讼状态：<.*?">(.*?)<') # 诉讼状态-
        list_item_loader.add_value('rrading_channels', unicode_escape_res_re, TakeFirst(), re='>交易渠道：<.*?">(.*?)<') # 交易渠道-

        list_items = list_item_loader.load_item()

        items = {
            **list_items,
        }
        return items