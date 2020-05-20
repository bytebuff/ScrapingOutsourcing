# -*- coding: utf-8 -*-
import json
import scrapy
from ..items import JdcrspiderItem, JdItemLoader
from twisted.internet.defer import inlineCallbacks


class JdcrSpider(scrapy.Spider):
    name = 'jdcr'
    allowed_domains = ['jd.com']
    start_urls = [f'https://auction.jd.com/getAssetsList.html?childrenCateId=12767&limit=40&page={page}' for page in range(1, 30 + 1)]

    def parse(self, response):
        json_response = json.loads(response.text)
        flag = json_response.get('ls')
        if flag:
            for data in flag:
                detail_url = f'https://paimai.jd.com/{data["id"]}'
                yield response.follow(url=detail_url, callback=self.parse_detail, meta={'list_data': data})

    @inlineCallbacks
    def parse_detail(self, response):
        list_data = response.meta['list_data']

        item_loader = JdItemLoader(item=JdcrspiderItem(), response=response)

        # extract the data for your item here : 共 39 个字段
        item_loader.add_value('bid_type', '债权')  # 标的物类型
        item_loader.add_value('bid_province', list_data['province'])  # 标的物所在省
        item_loader.add_value('bid_city', list_data['city'])  # 标的物所在市
        item_loader.add_value('auction_rounds', list_data['title'], re='【(.*?)】|（(.*?次)）')  # 拍卖轮次
        item_loader.add_xpath('bid_location', '//em[@id="paimaiAddress"]/text()')  # 标的物所在地
        item_loader.add_value('seller_name', list_data['shopName'])  # 送拍机构
        item_loader.add_value('starting_price', list_data['startPrice'])  # 起拍价
        item_loader.add_value('transaction_price', list_data['currentPrice'])  # 成交价
        item_loader.add_value('fare_increase_rate', list_data['priceLowerOffset'])  # 加价幅度
        item_loader.add_value('title', list_data['title'])  # 标题
        item_loader.add_xpath('delay_period', '//span[contains(text(),"延时周期")]/following-sibling::span[1]/text()')  # 延时周期
        item_loader.add_xpath('preemptive_right_holder', '//span[@id="priorPurchaserShow"]/text()')  # 优先购买权人

        current_state_url = f'https://paimai.jd.com/json/current/englishquery.html?paimaiId={list_data["id"]}&start=0&end=9'
        current_state_request = scrapy.Request(current_state_url, callback=self.parse_detail)
        current_state_response = yield self.crawler.engine.download(current_state_request, self)
        item_loader.add_value('current_state', current_state_response.text)  # 当前状态 - 拍卖状态-> 0 等待拍卖 1 正在拍卖 2 拍卖结束

        item_loader.add_value('completion_time', list_data['endTime'])  # 完成时间

        # 报名与围观人数
        number_url = f'https://paimai.jd.com/json/ensure/queryAccess?paimaiId={list_data["id"]}'
        number_request = scrapy.Request(number_url, callback=self.parse_detail)
        number_response = yield self.crawler.engine.download(number_request, self)

        item_loader.add_value('sign_up_number', number_response.text, re=r'"accessEnsureNum":(\d+)')  # 报名人数
        item_loader.add_value('watch_number', number_response.text, re=r'"accessNum":(\d+)')  # 围观人数

        item1 = item_loader.load_item()

        bid_detail_url = f'https://paimai.jd.com/json/paimaiProduct/productDesciption?productId={list_data["skuId"]}'
        bid_request = scrapy.Request(bid_detail_url, callback=self.parse_detail)
        bid_response = yield self.crawler.engine.download(bid_request, self)

        # 标的物信息
        bid_item_loader = JdItemLoader(item=JdcrspiderItem(), response=bid_response)

        bid_item_loader.add_xpath('bid_name', '//td[contains(text(),"标的物名称")]/following-sibling::td/text()')  # 标的物名称
        bid_item_loader.add_xpath('debtor_name', '//td[contains(text(),"债务人名称")]/following-sibling::td/text()')  # 债务人名称
        bid_item_loader.add_xpath('debtor_info', '//td[contains(text(),"债务人信息")]/following-sibling::td/text()')  # 债务人信息
        bid_item_loader.add_xpath('creditor_name', '//td[contains(text(),"债权人名称")]/following-sibling::td/text()')  # 债权人名称
        bid_item_loader.add_xpath('creditor_info', '//td[contains(text(),"债权人信息")]/following-sibling::td/text()')  # 债权人信息
        bid_item_loader.add_xpath('creditor_balance', '//td[contains(text(),"债权余额")]/following-sibling::td/text()')  # 债权余额

        bid_item_loader.add_xpath('principal_amount', '//td[contains(text(),"本金金额")]/following-sibling::td/text()')  # 本金金额
        bid_item_loader.add_xpath('principal_amount', '//p//text()')  # 本金金额

        bid_item_loader.add_xpath('interest', '//td[contains(text(),"利息金额")]/following-sibling::td/text()')  # 利息及逾期利息
        bid_item_loader.add_xpath('lawsuit_amount', '//td[contains(text(),"诉讼费用")]/following-sibling::td/text()')  # 诉讼费用金额
        bid_item_loader.add_xpath('loan_interest_rate', '//td[contains(text(),"利率")]/following-sibling::td/text()')  # 贷款利率
        bid_item_loader.add_xpath('loan_release_date', '//td[contains(text(),"贷款发放日")]/following-sibling::td/text()')  # 贷款发放日
        bid_item_loader.add_xpath('loan_maturity_date', '//td[contains(text(),"贷款到期日")]/following-sibling::td/text()')  # 贷款到期日
        bid_item_loader.add_xpath('collateral', '//td[contains(text(),"有无抵")]/following-sibling::td/text()')  # 有无抵/质押物/查封资产
        bid_item_loader.add_xpath('collateral_valuation', '//td[contains(text(),"查封资产总评估价")]/following-sibling::td/text()')  # 抵/质押物/查封资产总评估价
        bid_item_loader.add_xpath('collateral_info', '//td[contains(text(),"查封资产信息")]/following-sibling::td/text()')  # 抵/质押物/查封资产信息
        bid_item_loader.add_xpath('guarantor', '//td[contains(text(),"有无担保人")]/following-sibling::td/text()')  # 有无担保人　
        bid_item_loader.add_xpath('guarantor_name', '//td[contains(text(),"担保人")]/following-sibling::td/text()')  # 担保人
        bid_item_loader.add_xpath('guarantor_info', '//td[contains(text(),"担保人信息")]/following-sibling::td/text()')  # 担保人信息
        bid_item_loader.add_xpath('guaranteed_amount', '//td[contains(text(),"担保金额")]/following-sibling::td/text()')  # 担保金额
        bid_item_loader.add_xpath('guaranteed_form', '//td[contains(text(),"担保形式")]/following-sibling::td/text()')  # 担保形式
        bid_item_loader.add_xpath('lawsuit_status', '//td[contains(text(),"诉讼状态")]/following-sibling::td/text()')  # 诉讼状态
        bid_item_loader.add_value('trading_channels', '京东')  # 交易渠道
        bid_item_loader.add_value('page_url', response.url)  # 页面网址

        item2 = bid_item_loader.load_item()

        items = {
            **item1,
            **item2,
        }

        return items
