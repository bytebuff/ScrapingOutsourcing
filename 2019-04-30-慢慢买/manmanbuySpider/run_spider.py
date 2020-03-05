'''
运行爬虫
'''
from scrapy import cmdline

cmdline.execute('scrapy crawl manmanbuy -a key=短袖男 -a page=2'.split())