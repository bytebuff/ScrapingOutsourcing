"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: test.py
    @time: 2019/12/6 11:53
    @desc:
"""
from scrapely import Scraper
import requests


scraper = Scraper()

url = 'https://www.ituring.com.cn/article'
data = {'name': 'duxingzhe', 'title': '这两天的面试经验总结'}
# response = requests.get(url).text
scraper.train(url, data)
result = scraper.scrape(url, encoding='utf-8')
print(result)