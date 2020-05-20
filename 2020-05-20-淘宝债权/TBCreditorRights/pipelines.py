# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import aiomysql
from .settings import *
from .items import TbcrspiderModel


class TbcreditorrightsPipeline(object):

    def open_spider(self, spider):
        if not TbcrspiderModel.table_exists():
            TbcrspiderModel.create_table()
            print(spider.settings['TABLE_TITLE_NAME_ZH'])
            TbcrspiderModel.create(**spider.settings['TABLE_TITLE_NAME_ZH'])

    async def process_item(self, item, spider):
        try:
            TbcrspiderModel.create(**item)
        except Exception as e:
            print(f"管道错误->{e}")
        return item

    def close_spider(self, spider):
        pass


class AsyncTbcreditorrightsPipeline(object):

    def open_spider(self, spider):
        if not TbcrspiderModel.table_exists():
            TbcrspiderModel.create_table()
            print(spider.settings['TABLE_TITLE_NAME_ZH'])
            TbcrspiderModel.create(**spider.settings['TABLE_TITLE_NAME_ZH'])

    async def process_item(self, item, spider):
        conn = await aiomysql.connect(
            host=MYSQL_SETTINGS['host'],
            port=MYSQL_SETTINGS['port'],
            user=MYSQL_SETTINGS['user'],
            password=MYSQL_SETTINGS['passwd'],
            db=MYSQL_SETTINGS['datebase'],
        )
        async with conn.cursor() as cur:
            sql = """INSERT INTO `tb_creditor_rights_test` (`bid_type`, `bid_province`, `bid_city`, `bid_area`, `bid_start_time`, `bid_end_time`, `auction_rounds`, `title`, `starting_price`, `transaction_price`, `assessment_price`, `current_state`, `completion_time`, `margin`, `price_rate_increase`, `sale_cycle`, `delaytime_cycle`, `preferred_purchase`, `disposal_unit`, `sign_up_number`, `set_reminders`, `onlookers_number`, `guarantee_method`, `principal_creditor_rights`, `no_interest`, `base_date`, `principal_interest_total`, `debtor_name`, `debtor_info`, `creditor_info`, `creditor_name`, `creditor_balance`, `principal_amount`, `interest_amount`, `loans_monthly_interest_rate`, `loans_release_date`, `loan_maturity_date`, `collateral`, `collateral_total_price`, `collateral_info`, `guarantor`, `guarantor_name`, `guarantor_info`, `guarantor_amount`, `guarantor_method`, `litigation_status`, `rrading_channels`, `page_url`)
VALUES
	('[\'债权\']', '[\'浙江省\']', '[\'金华市\']', '[\'浙江省 金华市 永康市\']', '[1577930400000]', '[1578016800000]', '[\'【第一次】【平安银行】郑泰集', '[\'【平安银行】郑泰集团有限公司', '[\'11,220,000 \']', '[\'11,220,000 \']', '', '', '[\'2020/01/03 10:', '[\'1,100,000 \']', '[\'20,000 \']', '[\': 1天\']', '[\': 1天\']', '[\':\\n           ', '[\'平安银行总行\']', '[1]', '[\'10\']', '[4531]', '[\'保证\']', '[\'11218460.42元\']', '', '[\'2019-10-30\']', '[\'20311899.16元\']', '[\'郑泰集团有限公司\']', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '[\'https://zc-ite');
"""
            await cur.execute(sql)
            await conn.commit()
            await conn.close()

        return item

    def close_spider(self, spider):
        pass
