# -*- coding: utf-8 -*-

# Scrapy settings for baiduguoxueSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'baiduguoxueSpider'

SPIDER_MODULES = ['baiduguoxueSpider.spiders']
NEWSPIDER_MODULE = 'baiduguoxueSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'baiduguoxueSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Host': 'www.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    #'Referer': 'https://www.baidu.com/s?wd=%E5%9B%BD%E5%AD%A6%E5%9F%B9%E8%AE%AD&pn=140&oq=%E5%9B%BD%E5%AD%A6%E5%9F%B9%E8%AE%AD&ie=utf-8&rsv_pq=b36afa7b00027031&rsv_t=ee0ajUiWOdvR4LC9z%2BpemV39e8Jw1LrM%2FaVbII0%2FWzQR3RJy7NS0QT236kg',
    #'is_referer': 'https://www.baidu.com/s?wd=%E5%9B%BD%E5%AD%A6%E5%9F%B9%E8%AE%AD&pn=130&oq=%E5%9B%BD%E5%AD%A6%E5%9F%B9%E8%AE%AD&ie=utf-8&rsv_pq=c9ec36f0000082c9&rsv_t=40d3%2BxSTAnv15khIcHZL7yr7MoHSRPE6T8s3bFjoPY6EWhavAJs3BOgL9s4&bs=%E5%9B%BD%E5%AD%A6%E5%9F%B9%E8%AE%AD',
    #'is_xhr': '1',
    #'is_pbs': '%E5%9B%BD%E5%AD%A6%E5%9F%B9%E8%AE%AD',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    #'Cookie': 'BD_UPN=13314752; BAIDUID=CC5420478CEB9216950D0BA7291BC541:FG=1; BIDUPSID=F43D7964202B14A8F9960CF3B7CF620F; PSTM=1544785391; MCITY=-340%3A75%3A; BDUSS=zZpcWU2aFAwS3ZxbW0zdEJpbk85bXZiWXFQaXh4THIxaEtGTFlZWk5KSWljckZjQVFBQUFBJCQAAAAAAAAAAAEAAABSO6NAyrfC87jqZmx5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACLliVwi5YlcQ; H_PS_PSSID=1443_21113_20697_28722_28557_28697_28584_28603_28626_20719; delPer=0; BD_CK_SAM=1; PSINO=3; BDRCVFR[gltLrB7qNCt]=mk3SLVN4HKm; H_PS_645EC=ee0ajUiWOdvR4LC9z%2BpemV39e8Jw1LrM%2FaVbII0%2FWzQR3RJy7NS0QT236kg; sug=3; sugstore=0; ORIGIN=2; bdime=0; BDSVRTM=100',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'baiduguoxueSpider.middlewares.BaiduguoxuespiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'baiduguoxueSpider.middlewares.BaiduguoxuespiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'baiduguoxueSpider.pipelines.BaiduguoxuespiderPipeline': 300,
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
