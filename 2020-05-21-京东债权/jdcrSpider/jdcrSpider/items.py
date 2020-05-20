# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import json
import scrapy
from scrapy.utils.project import get_project_settings
from peewee import *
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Compose, Identity, MapCompose, Join
from .item_tools import *


class JdcrspiderModel(Model):
    # 共39个字段 加上主键 id 共40个
    bid_type = CharField(max_length=4, default="")  # 标的物类型
    bid_province = CharField(max_length=8, default="")  # 标的物所在省
    bid_city = CharField(max_length=8, default="")  # 标的物所在市
    auction_rounds = CharField(max_length=4, default="")  # 拍卖轮次
    bid_location = CharField(max_length=64, default="")  # 标的物所在地
    seller_name = CharField(max_length=10, default="")  # 送拍机构
    starting_price = CharField(max_length=15, default="")  # 起拍价
    transaction_price = CharField(max_length=15, default="")  # 成交价
    fare_increase_rate = CharField(max_length=15, default="")  # 加价幅度
    title = CharField(max_length=128, default="")  # 标题
    delay_period = CharField(max_length=16, default="")  # 延时周期
    preemptive_right_holder = CharField(max_length=8, default="无")  # 优先购买权人
    current_state = CharField(max_length=16, default="")  # 当前状态
    completion_time = CharField(max_length=32, default="")  # 完成时间
    sign_up_number = CharField(max_length=8, default="")  # 报名人数
    watch_number = CharField(max_length=8, default="")  # 围观人数
    bid_name = CharField(max_length=32, default="")  # 标的物名称
    debtor_name = CharField(max_length=8, default="")  # 债务人名称
    debtor_info = CharField(max_length=64, default="")  # 债务人信息
    creditor_name = CharField(max_length=64, default="")  # 债权人名称
    creditor_info = CharField(max_length=256, default="")  # 债权人信息
    creditor_balance = CharField(max_length=32, default='')  # 债权余额
    principal_amount = CharField(max_length=64, default='')  # 本金金额
    interest = CharField(max_length=64, default="")  # 利息及逾期利息
    lawsuit_amount = CharField(max_length=15, default='')  # 诉讼费用金额
    loan_interest_rate = CharField(max_length=10, default="")  # 贷款月利率
    loan_release_date = CharField(max_length=16, default="")  # 贷款发放日
    loan_maturity_date = CharField(max_length=16, default="")  # 贷款到期日
    collateral = CharField(max_length=8, default="")  # 有无抵/质押物/查封资产
    collateral_valuation = CharField(max_length=15, default='')  # 抵/质押物/查封资产总评估价
    collateral_info = CharField(max_length=64, default="")  # 抵/质押物/查封资产信息
    guarantor = CharField(max_length=8, default="")  # 有无担保人　
    guarantor_name = CharField(max_length=16, default="")  # 担保人
    guarantor_info = CharField(max_length=32, default="")  # 担保人信息
    guaranteed_amount = CharField(max_length=64, default='')  # 担保金额
    guaranteed_form = CharField(max_length=16, default="")  # 担保形式
    lawsuit_status = CharField(max_length=16, default="")  # 诉讼状态
    trading_channels = CharField(max_length=4, default="")  # 交易渠道 (淘宝或京东)
    page_url = CharField(max_length=256, default="")  # 页面网址

    class Meta:
        settings = get_project_settings().getdict('MYSQL_SETTINGS')
        datebase = settings['datebase']
        host = settings['host']
        port = settings['port']
        user = settings['user']
        passwd = settings['passwd']

        db = MySQLDatabase(datebase, host=host, port=port, user=user, passwd=passwd, charset='utf8')

        database = db
        table_name = 'jd_creditor_rights'


class JdcrspiderItem(scrapy.Item):
    # define the fields for your item here like: 共 39 个字段
    bid_type = scrapy.Field()  # 标的物类型
    bid_province = scrapy.Field()  # 标的物所在省
    bid_city = scrapy.Field()  # 标的物所在市
    auction_rounds = scrapy.Field()  # 拍卖轮次
    bid_location = scrapy.Field()  # 标的物所在地
    seller_name = scrapy.Field()  # 送拍机构
    starting_price = scrapy.Field()  # 起拍价
    transaction_price = scrapy.Field()  # 成交价
    fare_increase_rate = scrapy.Field()  # 加价幅度
    title = scrapy.Field()  # 标题
    delay_period = scrapy.Field()  # 延时周期
    preemptive_right_holder = scrapy.Field()  # 优先购买权人
    current_state = scrapy.Field()  # 当前状态
    completion_time = scrapy.Field(
        output_processor=Compose(TakeFirst(), timeStampTransform),
    )  # 完成时间
    sign_up_number = scrapy.Field()  # 报名人数
    watch_number = scrapy.Field()  # 围观人数
    bid_name = scrapy.Field()  # 标的物名称
    debtor_name = scrapy.Field()  # 债务人名称
    debtor_info = scrapy.Field()  # 债务人信息
    creditor_name = scrapy.Field()  # 债权人名称
    creditor_info = scrapy.Field()  # 债权人信息
    creditor_balance = scrapy.Field(
        output_processor=Compose(TakeFirst(), wanYuanToyuan)
    )  # 债权余额
    principal_amount = scrapy.Field()  # 本金金额
    interest = scrapy.Field()  # 利息及逾期利息
    lawsuit_amount = scrapy.Field()  # 诉讼费用金额
    loan_interest_rate = scrapy.Field()  # 贷款利率
    loan_release_date = scrapy.Field()  # 贷款发放日
    loan_maturity_date = scrapy.Field()  # 贷款到期日
    collateral = scrapy.Field()  # 有无抵/质押物/查封资产
    collateral_valuation = scrapy.Field()  # 抵/质押物/查封资产总评估价
    collateral_info = scrapy.Field()  # 抵/质押物/查封资产信息
    guarantor = scrapy.Field()  # 有无担保人　
    guarantor_name = scrapy.Field()  # 担保人
    guarantor_info = scrapy.Field()  # 担保人信息
    guaranteed_amount = scrapy.Field()  # 担保金额
    guaranteed_form = scrapy.Field()  # 担保形式
    lawsuit_status = scrapy.Field()  # 诉讼状态
    trading_channels = scrapy.Field()  # 交易渠道
    page_url = scrapy.Field()  # 页面网址


class JdItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    current_state_in = MapCompose(json.loads, paimaiStatus)
    principal_amount_in = Join()
    principal_amount_out = Compose(principalAmount, wanYuanToyuan, cleanNotIncludeYuan)

if __name__ == '__main__':
    JdcrspiderModel.create_table()
