# -*- coding: utf-8 -*-

# Scrapy settings for lagouSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lagouSpider'

SPIDER_MODULES = ['lagouSpider.spiders']
NEWSPIDER_MODULE = 'lagouSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lagouSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    #'Content-Length': '20',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': '_ga=GA1.2.1240643066.1540209044; user_trace_token=20181022195043-b4f35172-d5f0-11e8-977d-525400f775ce; LGUID=20181022195043-b4f35434-d5f0-11e8-977d-525400f775ce; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22166ebeb76562b8-0fce0a466e86c9-36664c08-1049088-166ebeb765710%22%2C%22%24device_id%22%3A%22166ebeb76562b8-0fce0a466e86c9-36664c08-1049088-166ebeb765710%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpt_baidu_pc%22%7D%7D; LG_LOGIN_USER_ID=f04da6b90433eca5941adb239bfb03a477fbef957e473d75; index_location_city=%E5%B9%BF%E5%B7%9E; JSESSIONID=ABAAABAAAIAACBIE6D3339739E4A5161F0E831A106C040F; _gid=GA1.2.355172615.1555913567; LGSID=20190422141247-a625f6e6-64c5-11e9-acd2-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1553829006,1555221774,1555913567; TG-TRACK-CODE=search_code; _gat=1; X_MIDDLE_TOKEN=6c00823a54e2b18b304ba50c653c9a01; SEARCH_ID=c23f7dfcbc124fa29cc10288c9fcb4b0; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1555916990; LGRID=20190422150950-9e9cc0cb-64cd-11e9-acf3-525400f775ce; X_HTTP_TOKEN=010cabdaca147f5d50071955515e2327bd48e181a6',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_?px=new&city=%E8%A5%BF%E5%AE%89',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lagouSpider.middlewares.LagouspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'lagouSpider.middlewares.LagouspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'lagouSpider.pipelines.LagouspiderPipeline': 300,
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
