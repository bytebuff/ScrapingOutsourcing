# -*- coding: utf-8 -*-

# Scrapy settings for TBCreditorRights project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'TBCreditorRights'

SPIDER_MODULES = ['TBCreditorRights.spiders']
NEWSPIDER_MODULE = 'TBCreditorRights.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'TBCreditorRights (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'TBCreditorRights.middlewares.TbcreditorrightsSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'TBCreditorRights.middlewares.TbcreditorrightsDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
   # 'scrapy.extensions.telnet.TelnetConsole': None,
    'TBCreditorRights.extensions.SpiderRedisExensions': 500

}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'TBCreditorRights.pipelines.TbcreditorrightsPipeline': 300,
   # 'TBCreditorRights.pipelines.AsyncTbcreditorrightsPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
HTTPCACHE_GZIP = False  # 压缩格式

# MySQL Settings
MYSQL_SETTINGS = {
    'datebase': 'creditor_rights',
    'host': '172.17.0.104',
    'port': 3307,
    'user': 'root',
    'passwd': 'lhjkv587',
}
# 表格中文标题
TABLE_TITLE_NAME_ZH = {
    'bid_type': '标的物类型',
    'bid_province': '标的物所在省',
    'bid_city': '标的物所在市',
    'bid_area': '标的物所在区',
    'bid_start_time': '标的物开拍时间的开始时间',
    'bid_end_time': '标的物开拍时间的结束时间',
    'auction_rounds': '拍卖轮次',
    'title': '标题',
    'starting_price': '起拍价',
    'transaction_price': '成交价',
    'assessment_price': '评估价',
    'current_state': '当前状态',
    'completion_time': '完成时间',
    'margin': '保证金',
    'price_rate_increase': '加价幅度',
    'sale_cycle': '变卖周期',
    'delaytime_cycle': '延时周期',
    'preferred_purchase': '优先购买',
    'disposal_unit': '处置单位',
    'sign_up_number': '报名人数',
    'set_reminders': '设置提醒',
    'onlookers_number': '围观人数',
    'guarantee_method': '担保方式',
    'principal_creditor_rights': '债权本金',
    'no_interest': '未尝利息',
    'base_date': '基准日',
    'principal_interest_total': '本息合计',
    'debtor_name': '债务人名称',
    'debtor_info': '债务人信息',
    'creditor_info': '债权人信息',
    'creditor_name': '债权人名称',
    'creditor_balance': '债权余额',
    'principal_amount': '本金金额',
    'interest_amount': '利息金额',
    'loans_monthly_interest_rate': '贷款月利率',
    'loans_release_date': '贷款发放日',
    'loan_maturity_date': '贷款到期日',
    'collateral': '有无抵押',
    'collateral_total_price': '抵押总评估价',
    'collateral_info': '抵押信息',
    'guarantor': '有无担保人',
    'guarantor_name': '担保人',
    'guarantor_info': '担保人信息',
    'guarantor_amount': '担保金额',
    'guarantor_method': '担保形式',
    'litigation_status': '诉讼状态',
    'rrading_channels': '交易渠道',
    'page_url': '页面网址',
}

TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'