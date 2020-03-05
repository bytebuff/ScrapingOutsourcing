# -*- coding: utf-8 -*-

# Scrapy settings for jdSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jdSpider'

SPIDER_MODULES = ['jdSpider.spiders']
NEWSPIDER_MODULE = 'jdSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jdSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': '__jdu=726152571; shshshfpa=f7900398-ba69-2898-4ad7-44301cf00d00-1541647899; TrackID=1x525e1odixDaxBf_LmaKaWE_AEp_wDzvhv99cH_42TVHxOOJi7U7YVd_sRgTl8VGpjDoJ0Vyu5TYsWL7re6zef4sTzojwBYrP7-VN53bQRU; pinId=9YbyTrGAADwYzeLRj_kMfrV9-x-f3wj7; qrsc=3; shshshfpb=04ded5392b7ea37c44060f3316258493282b7f8adc93fd2785be3ae1d8; areaId=22; PCSYCityID=1930; xtest=5015.cf6b6759; ipLoc-djd=1-72-2799-0; _gcl_au=1.1.1332904140.1555388005; unpl=V2_ZzNtbRJWQxMlDURQek0OV2JTEF0SAEMUIQsVVC4aWwU3VkENclRCFX0UR1FnGVoUZwMZWERcQhZFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZH0aWwVjABZbQmdzEkU4dlFzGFwMbjMTbUNnAUEpC09Qch9USGEAFV1GVEcTdThHZHg%3d; CCC_SE=ADC_pc54VZKPzRzryKqZfH%2fgi1pBp4j5eaFTUCbvmjqS3DpzC48MQDYP3LpBWwb3ijyqnMvVdgTn2N1EZcDsql565WTdwFJAz%2ban%2fkBiwDQiEYaL%2f6%2be4zeA%2bclO0Hl3MZMDCenWiFdHFGummYRwD%2bQOcft1OnrlcCr97FzeWENSHhO92IWfS%2bVnaIbr%2bRNCpptjkZOX5UwxneDOwJiDGyZZjdCCFWaKwo2EGmlRXK8VmTX4I3PQAS%2bCt4OGSDB0eHvEd98StLHr7FYFdAIuG9QHoP0DpsFDWGKpWQeBIiJlq6SchsqVPYSJIjmENUGhq%2bzJ%2blfVn7LDFq79X4s%2fm14TP2mZi3%2fqRMdKv%2f6njnwLKAYkwEa5xGmB8MZ8MfZCWITtq%2fofukxYJVBDJrgH7S7wsQRDaMv3Wt%2bR1Blg98reh4Bg0ouxGVFW02Qu2HueypEBQouZDzEr3VVtWw%2boDgL3y1vDf1j%2fZokt5UWfbQlvkJOydiZuXayIyelmw5Y%2fLD%2fi8SNP5I0DmSVv1tLusfxLj3mq8gu%2bJmOd0KNAVb%2fjEowvq6%2bymfDIbOBQnIC0LsW8; __jda=122270672.726152571.1540385961.1555387892.1555472830.12; __jdc=122270672; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_a017a4350ecc4a31af10e2b1d261adba|1555472830378; shshshfp=e3c1a47bbf88c5b956a8fdb80bca2731; rkv=V0600; 3AB9D23F7A4B3C9B=Z3PK5KKCADWGKK5A64IU3MOJHJ557VE6S7YAG3HW7T2YMK4LDICOVYFT5BKCUVP54B2FPENCNP6RMHPV75F7H7GYGI',
    'referer': 'https://search.jd.com/Search?keyword=%E5%86%9C%E4%BA%A7%E5%93%81&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%86%9C%E4%BA%A7%E5%93%81&stock=1&page=1&s=1&click=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jdSpider.middlewares.JdspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jdSpider.middlewares.JdspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'jdSpider.pipelines.JdspiderPipeline': 300,
    #'jdSpider.pipelines.JdspiderMySQLPipeline': 301
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
