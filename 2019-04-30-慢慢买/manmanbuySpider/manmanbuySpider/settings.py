# -*- coding: utf-8 -*-

# Scrapy settings for manmanbuySpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'manmanbuySpider'

SPIDER_MODULES = ['manmanbuySpider.spiders']
NEWSPIDER_MODULE = 'manmanbuySpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'manmanbuySpider (+http://www.yourdomain.com)'

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
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_85f48cee3e51cd48eaba80781b243db3=1556601529; ASP.NET_SessionId=tz3vaam1qk14y11aa4b0qye1; usersearcherid=644f79879a784a5592210c833ba015e0; MMBUserAreaN=%7B%22Area%22%3A%22510104%22%2C%22Zone%22%3A5%2C%22PerName%22%3A%22%25u56DB%25u5DDD%22%2C%22CityName%22%3A%22%25u6210%25u90FD%25u5E02%22%2C%22CountyName%22%3A%22%25u9526%25u6C5F%25u533A%22%2C%22User%22%3A%224f83b9ec-29a7-2741-31c2-6f5cb0f86742%22%2C%22IsUsed%22%3A1%7D; COMPARE_COOKIE=%7B%22c%22%3A0%2C%22s%22%3A0%2C%22l%22%3A%5B%5D%7D; Hm_lvt_30453b7c2dfa67a6c69b52556ce8eaef=1556601705; Hm_lpvt_30453b7c2dfa67a6c69b52556ce8eaef=1556601705; Hm_lvt_313c599bcf6e44393cebef6a2629f81e=1556601569,1556601727; uibdfq=15; Hm_lpvt_85f48cee3e51cd48eaba80781b243db3=1556602095; Hm_lpvt_313c599bcf6e44393cebef6a2629f81e=1556602095',
    'Host': 's.manmanbuy.com',
    #'Referer': 'http://s.manmanbuy.com/Default.aspx?PageID=3&key=%b0%d7%b2%cb',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'manmanbuySpider.middlewares.ManmanbuyspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'manmanbuySpider.middlewares.ManmanbuyspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'manmanbuySpider.pipelines.ManmanbuyspiderPipeline': 300,
   #'manmanbuySpider.pipelines.ManmanbuyspiderImagePipeline': 301,
   'manmanbuySpider.pipelines.ManmanbuyspiderMySQLPipeline': 302
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
