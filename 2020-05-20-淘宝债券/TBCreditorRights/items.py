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
from .items_tools import *


class TbcrspiderModel(Model):
    # 共48个字段 加上主键 id 共49个
    bid_type = CharField(max_length=16, default="")  # 标的物类型
    bid_province = CharField(max_length=16, default="")  # 标的物所在省
    bid_city = CharField(max_length=16, default="")  # 标的物所在市
    bid_area = CharField(max_length=16, default="")  # 标的物所在区
    bid_start_time = CharField(max_length=16, default="") # 标的物开拍时间的开始时间
    bid_end_time = CharField(max_length=16, default="") # 标的物开拍时间的结束时间
    auction_rounds = CharField(max_length=16, default="")  # 拍卖轮次
    title = CharField(max_length=16, default="")  # 标题
    starting_price = CharField(max_length=16, default="")  # 起拍价
    transaction_price = CharField(max_length=16, default="")  # 成交价
    assessment_price = CharField(max_length=16, default="") # 评估价
    current_state = CharField(max_length=16, default="")  # 当前状态
    completion_time = CharField(max_length=16, default="")  # 完成时间
    margin = CharField(max_length=16, default="") # 保证金
    price_rate_increase = CharField(max_length=16, default="") # 加价幅度
    sale_cycle = CharField(max_length=16, default="") # 竞价周期
    delaytime_cycle = CharField(max_length=16, default="") # 延时周期
    preferred_purchase = CharField(max_length=16, default="") # 优先购买权人
    disposal_unit = CharField(max_length=16, default="") # 处置单位
    sign_up_number = CharField(max_length=16, default="") # 报名人数
    set_reminders = CharField(max_length=16, default="") # 设置提醒
    onlookers_number = CharField(max_length=16, default="") # 围观人数
    guarantee_method = CharField(max_length=16, default="") # 担保方式
    principal_creditor_rights = CharField(max_length=16, default="") # 债权本金
    no_interest = CharField(max_length=16, default="") # 未尝利息
    base_date = CharField(max_length=16, default="") # 基准日
    principal_interest_total = CharField(max_length=16, default="") # 本息合计
    debtor_name = CharField(max_length=16, default="") # 债务人名称
    debtor_info = CharField(max_length=16, default="") # 债务人信息
    creditor_info = CharField(max_length=16, default="") # 债权人信息
    creditor_name = CharField(max_length=16, default="") # 债权人名称
    creditor_balance = CharField(max_length=16, default="") # 债权余额
    principal_amount = CharField(max_length=16, default="") # 本金金额
    interest_amount = CharField(max_length=16, default="") # 利息金额
    loans_monthly_interest_rate = CharField(max_length=16, default="") # 贷款月利率
    loans_release_date = CharField(max_length=16, default="") # 贷款发放日
    loan_maturity_date = CharField(max_length=16, default="") # 贷款到期日
    collateral = CharField(max_length=16, default="") # 有无抵押
    collateral_total_price = CharField(max_length=16, default="") # 抵押总评估价
    collateral_info = CharField(max_length=16, default="") # 抵押信息
    guarantor = CharField(max_length=16, default="") # 有无担保人
    guarantor_name = CharField(max_length=16, default="") # 担保人
    guarantor_info = CharField(max_length=16, default="") # 担保人信息
    guarantor_amount = CharField(max_length=16, default="") # 担保金额
    guarantor_method = CharField(max_length=16, default="") # 担保形式
    litigation_status = CharField(max_length=16, default="") # 诉讼状态
    rrading_channels = CharField(max_length=16, default="") # 交易渠道
    page_url = CharField(max_length=16, default="") # 页面网址

    class Meta:
        settings = get_project_settings().getdict('MYSQL_SETTINGS')
        datebase = settings['datebase']
        host = settings['host']
        port = settings['port']
        user = settings['user']
        passwd = settings['passwd']

        db = MySQLDatabase(datebase, host=host, port=port, user=user, passwd=passwd, charset='utf8')

        database = db
        table_name = 'tb_creditor_rights_test'


class TbcreditorrightsItem(scrapy.Item):
    # define the fields for your item here like: 共 48 个字段
    bid_type = scrapy.Field()  # 标的物类型
    bid_province = scrapy.Field()  # 标的物所在省
    bid_city = scrapy.Field()  # 标的物所在市
    bid_area = scrapy.Field()  # 标的物所在区
    bid_start_time = scrapy.Field() # 标的物开拍时间的开始时间
    bid_end_time = scrapy.Field() # 标的物开拍时间的结束时间
    auction_rounds = scrapy.Field()  # 拍卖轮次
    title = scrapy.Field()  # 标题
    starting_price = scrapy.Field()  # 起拍价
    transaction_price = scrapy.Field()  # 成交价
    assessment_price = scrapy.Field() # 评估价
    current_state = scrapy.Field()  # 当前状态
    completion_time = scrapy.Field()  # 完成时间
    margin = scrapy.Field() # 保证金
    price_rate_increase = scrapy.Field() # 加价幅度
    sale_cycle = scrapy.Field() # 变卖周期
    delaytime_cycle = scrapy.Field() # 延时周期
    preferred_purchase = scrapy.Field() # 优先购买
    disposal_unit = scrapy.Field() # 处置单位
    sign_up_number = scrapy.Field() # 报名人数
    set_reminders = scrapy.Field() # 设置提醒
    onlookers_number = scrapy.Field() # 围观人数
    guarantee_method = scrapy.Field() # 担保方式
    principal_creditor_rights = scrapy.Field() # 债权本金
    no_interest = scrapy.Field() # 未尝利息
    base_date = scrapy.Field() # 基准日
    principal_interest_total = scrapy.Field() # 本息合计
    debtor_name = scrapy.Field() # 债务人名称
    debtor_info = scrapy.Field() # 债务人信息
    creditor_info = scrapy.Field() # 债权人信息
    creditor_name = scrapy.Field() # 债权人名称
    creditor_balance = scrapy.Field() # 债权余额
    principal_amount = scrapy.Field() # 本金金额
    interest_amount = scrapy.Field() # 利息金额
    loans_monthly_interest_rate = scrapy.Field() # 贷款月利率
    loans_release_date = scrapy.Field() # 贷款发放日
    loan_maturity_date = scrapy.Field() # 贷款到期日
    collateral = scrapy.Field() # 有无抵押
    collateral_total_price = scrapy.Field() # 抵押总评估价
    collateral_info = scrapy.Field() # 抵押信息
    guarantor = scrapy.Field() # 有无担保人
    guarantor_name = scrapy.Field() # 担保人
    guarantor_info = scrapy.Field() # 担保人信息
    guarantor_amount = scrapy.Field() # 担保金额
    guarantor_method = scrapy.Field() # 担保形式
    litigation_status = scrapy.Field() # 诉讼状态
    rrading_channels = scrapy.Field() # 交易渠道
    page_url = scrapy.Field() # 页面网址

class TbItemLoader(ItemLoader):
    # guarantee_method_in = Compose(TakeFirst(), unicode_item)
    pass

if __name__ == '__main__':
    # TbcrspiderModel.create_table()
    items = TbcreditorrightsItem()
    print(items.fields)
