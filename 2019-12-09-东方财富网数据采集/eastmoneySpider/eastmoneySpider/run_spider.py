"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: run_spider.py
    @time: 2019/12/9 11:24
    @desc:
"""
from scrapy import cmdline

cmdline.execute('scrapy crawl eastmoney'.split())
