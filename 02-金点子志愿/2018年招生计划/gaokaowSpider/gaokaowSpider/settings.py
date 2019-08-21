# -*- coding: utf-8 -*-

# Scrapy settings for gaokaowSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'gaokaowSpider'

SPIDER_MODULES = ['gaokaowSpider.spiders']
NEWSPIDER_MODULE = 'gaokaowSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gaokaowSpider (+http://www.yourdomain.com)'

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
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '0',
    # 'Cookie': 'Youzy2BCurrentProvince=%7B%22provinceName%22%3A%22%E5%9B%9B%E5%B7%9D%22%2C%22provinceId%22%3A%22855%22%7D; Youzy2BStore=%7B%22id%22%3A%225c6be8819e742b010419123a%22%2C%22numId%22%3A4210%2C%22name%22%3A%22%E9%87%91%E7%82%B9%E5%AD%90%E5%BF%97%E6%84%BF%22%2C%22storeLogoUrl%22%3A%22http%3A%2F%2Fimg3.youzy.cn%2Fcontent%2Fmedia%2Fthumbs%2Fp00039732.png%22%2C%22provinceName%22%3A%22%E5%9B%9B%E5%B7%9D%22%2C%22openProvinces%22%3A%22%E5%9B%9B%E5%B7%9D%22%2C%22provinceNumId%22%3A%22855%22%2C%22openProvinceIds%22%3A%22855%22%2C%22h5Address%22%3A%22http%3A%2F%2Fjdzzym.gaokaow.cc%22%2C%22isOpened%22%3Afalse%2C%22theme%22%3A%7B%22theme%22%3A0%2C%22themeNavi%22%3A1%2C%22themePageOfHome%22%3A1%7D%7D; connect.sid=s%3Aheqba3-6Iavh2pBI2Jc1vivNA7mTicPa.5a7fs3DrMuLZDqAdOsRvr0Tv2JGVRxUlzYVUQ9Oy%2FJ4; Youzy2BStudent=%7B%22courseType%22%3A%22%E7%90%86%E7%A7%91%22%2C%22courseTypeEnum%22%3A0%2C%22gaoKaoYear%22%3A2021%2C%22gkaProvince%22%3A%22%E5%9B%9B%E5%B7%9D%22%2C%22gkaProvinceNumId%22%3A855%2C%22id%22%3A%225c6be98fcf8772157c0259ce%22%2C%22isBManager%22%3Atrue%2C%22isImported%22%3A0%2C%22isMember%22%3Afalse%2C%22isSxkUser%22%3Atrue%2C%22isTy%22%3Afalse%2C%22isTyNeedUpgradeTip%22%3Afalse%2C%22isVip%22%3Atrue%2C%22isZZUser%22%3Afalse%2C%22mobile%22%3A%2213118157880%22%2C%22numId%22%3A174282%2C%22realName%22%3A%22%E9%BB%91%E5%AF%A1%E5%A6%87%22%2C%22sex%22%3A1%2C%22storeId%22%3A4210%2C%22username%22%3A%2213118157880%22%2C%22vipPermission%22%3Atrue%7D; Youzy2BCurrentScore=%7B%22numId%22%3A497469%2C%22storeNumId%22%3A4210%2C%22provinceNumId%22%3A855%2C%22studentNumId%22%3A174282%2C%22total%22%3A500%2C%22courseTypeId%22%3A0%2C%22rank%22%3A0%2C%22batch%22%3A0%2C%22poorLineScore%22%3A0%2C%22chooseLevelOrSubjects%22%3A%22%22%2C%22isResetCount%22%3Afalse%2C%22creationTime%22%3A%222019-04-02T15%3A23%3A21.812%2B08%3A00%22%2C%22chooseLevelFormat%22%3A%5B%5D%2C%22chooseSubjectsFormat%22%3A%5B%5D%2C%22id%22%3A%225ca30de9ff3dd936a6e65546%22%7D',
    # 'Host': 'jdzzy.gaokaow.cc',
    # 'Origin': 'http://jdzzy.gaokaow.cc',
    # 'Referer': 'http://jdzzy.gaokaow.cc/tzySearch/colleges/homepage?cid=896',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    # 'X-Requested-With': 'XMLHttpRequest',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'gaokaowSpider.middlewares.GaokaowspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'gaokaowSpider.middlewares.GaokaowspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'gaokaowSpider.pipelines.GaokaowspiderPipeline': 300,
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


# COMMANDS_MODULE =BOT_NAME+ '.commands'