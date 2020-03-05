# -*- coding: utf-8 -*-

# Scrapy settings for xiaozhuSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xiaozhuSpider'

SPIDER_MODULES = ['xiaozhuSpider.spiders']
NEWSPIDER_MODULE = 'xiaozhuSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xiaozhuSpider (+http://www.yourdomain.com)'

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
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'gr_user_id=4844e1fa-126f-43d0-909f-5af5f96866e6; 59a81cc7d8c04307ba183d331c373ef6_gr_last_sent_cs1=N%2FA; grwng_uid=a409c431-1140-4e26-95e7-2e69a55e5a31; xz_guid_4se=03459fce-2235-4d5b-9e84-a36ee4184660; _uab_collina=155358561150539202408096; abtest_ABTest4SearchDate=b; 59a81cc7d8c04307ba183d331c373ef6_gr_session_id=015b34bb-9b95-4924-90e8-2d9652b021e2; 59a81cc7d8c04307ba183d331c373ef6_gr_last_sent_sid_with_cs1=015b34bb-9b95-4924-90e8-2d9652b021e2; 59a81cc7d8c04307ba183d331c373ef6_gr_session_id_015b34bb-9b95-4924-90e8-2d9652b021e2=true; TY_SESSION_ID=87b96734-42c6-4691-b14e-837c6c13c00e; rule_math=ca5t4kewww',
    'Host': 'sh.xiaozhu.com',
    'Referer': 'http://sh.xiaozhu.com/fangzi/44319306303.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Tingyun-Id': 'uxh10gyAidI;r=368205570',
    'xSRF-Token': 'cc008ff63ff0a79d6e6d6a8b064e5599',

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xiaozhuSpider.middlewares.XiaozhuspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'xiaozhuSpider.middlewares.XiaozhuspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'xiaozhuSpider.pipelines.XiaozhuspiderPipeline': 300,
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