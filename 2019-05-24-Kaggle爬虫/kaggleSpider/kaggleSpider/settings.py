# -*- coding: utf-8 -*-

# Scrapy settings for kaggleSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'kaggleSpider'

SPIDER_MODULES = ['kaggleSpider.spiders']
NEWSPIDER_MODULE = 'kaggleSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'kaggleSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {

    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': '_ga=GA1.2.1592250334.1553319415; _fbp=fb.1.1553319418362.776361445; ka_sessionid=880c8bb83abe68ba7ae8dda39cdf1abf812ecd0f; intercom-id-koj6gxx6=f59a8a14-8587-432c-9f0b-b0abd8c17858; CSRF-TOKEN=CfDJ8LdUzqlsSWBPr4Ce3rb9VL9Wj9NIyOfhN4uF7czE4M8XynS5LIfRULEvNsBkiv8uq8l_ViLD2uBlV39DR0QBPQMwmsXdrfoZXep6_zUwaIKvdLpY-6WzxI6QFI3ykMqVKqkpSojVVe6YxlUiMJmrmeo; .ASPXAUTH=3695F91F051C92A351E376BB2FDEC4AFB007FB2F98538E0C033E0345E1E9907DF5940A67F7AD8B6316F97E845582B4CAFD4A097D6317062D2F48B9102A1D7578A8D95C6F3D819937032223FBC95CDA3D49B13CB1; GCLB=CJTrxtyu1qH5BQ; _gid=GA1.2.974908827.1555573397; XSRF-TOKEN=CfDJ8LdUzqlsSWBPr4Ce3rb9VL9OXKSvsR6d1uiqbsOSDJnIs2B8NqHTbUBdFDGGkayefluy59fbwVUHtaxvi7p4iTJKXoVEhHDBe4gfWIpBc89wGW1fbXyiSscaV3E8jkt5RIkX4fDFjQTvqlY9QGDuTKg5Bl6GMOfwMD2mdgyHNPWE8ycI5l674m_hjkDA2apazA; intercom-session-koj6gxx6=K2h3TEpQRUpERHd0dFBCVVpOcWhac3ZBVDJXbXh4dXh3eUNVSFd6bW5Ka1ovYzFTcTVZTzkwV2twaUdRaWJRKy0tTnJ1WGptVmhnbnpRT2w3UFExeUVYQT09--f8591d64532390678167c3eeddd0eae408a605e9',
    'referer': 'https://www.kaggle.com/discussion?sortBy=new&group=all&page=1&pageSize=20&category=all',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'kaggleSpider.middlewares.KagglespiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'kaggleSpider.middlewares.KagglespiderDownloaderMiddleware': 543,
#     #'kaggleSpider.middlewares.IpDownloaderMiddleware': 500
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'kaggleSpider.pipelines.KagglespiderPipeline': 300,
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
