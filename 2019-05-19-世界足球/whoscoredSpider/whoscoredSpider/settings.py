# -*- coding: utf-8 -*-

# Scrapy settings for whoscoredSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'whoscoredSpider'

SPIDER_MODULES = ['whoscoredSpider.spiders']
NEWSPIDER_MODULE = 'whoscoredSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'whoscoredSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': 'visid_incap_774904=fU6xUqILRe2ljOs7rHNT4xz/r1wAAAAAQUIPAAAAAADTr/hLFJfTan7WTjhCIOny; _ga=GA1.2.901709446.1555037986; _ym_uid=155503799141660844; _ym_d=1555037991; incap_ses_426_774904=fmUpf09CzSwHtkKsuXXpBUZX3lwAAAAAT7lUtw8MjkE/7opUXGXJOQ==; __gads=ID=b2a8b0b1bc122bd3:T=1558075282:S=ALNI_Maq9qSHDg_d5-WBptKKueK8X7a1aQ; incap_ses_894_774904=8eq8KU+69jFwLLBa6DFoDBPa4FwAAAAArlmBosumt5XzhmXID98zYQ==; _gid=GA1.2.1248564269.1558239789; _ym_visorc_52685938=w; _ym_isad=2; _gat=1; _gat_subdomainTracker=1',
    'model-last-mode': 'Ykn7uqiYu7Qz/2U308TI/w0hCXKto7tyLNTXDg6faK4=', # 这个必须有
    'referer': 'https://www.whoscored.com/Matches/1316821/LiveStatistics/', # 这个必须有
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'whoscoredSpider.middlewares.WhoscoredspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'whoscoredSpider.middlewares.WhoscoredspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'whoscoredSpider.pipelines.WhoscoredspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#REDIRECT_ENABLED = False