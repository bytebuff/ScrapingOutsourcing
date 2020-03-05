"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: 北大末名bbs.py
    @time: 2019/12/1 10:51
    @desc:
"""
"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: 红楼.py
    @time: 2019/11/24 11:16
    @desc: 红楼梦数据采集
"""
import time, re
import requests
from bs4 import BeautifulSoup

# 总网页 采集所有页数

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
}


def getAllList():
    url = 'https://bbs.pku.edu.cn/v2/home.php'
    response = requests.get(url, headers=headers)
    return response.text


def parseAllList(text):
    soup = BeautifulSoup(text, 'html.parser')
    section = soup.findAll('section', attrs={'class': 'topic-block'})[1]
    urlList = section.findAll('a', attrs={'class': 'post-link'})
    urls = []
    for url in urlList:
        url = 'https://bbs.pku.edu.cn/v2/' + url['href']
        urls.append(url)
    return urls


def detailRequest(url):
    response = requests.get(url, headers=headers, timeout=1200)
    time.sleep(0.5)
    return response.text


def parseDetail(text):
    # 文本内容
    soup = BeautifulSoup(text, 'html.parser')
    div = soup.findAll('div', attrs={'class': 'content'})[0]
    p = div.findAll('p')

    for p in p:
        saveData(p.text)


def saveData(content):
    with open('bbs.txt', 'a', encoding='utf-8') as fp:
        fp.write(content + '\n')


def runSpider():
    text = getAllList()
    allUrl = parseAllList(text)
    for detailUrl in allUrl:
        text = detailRequest(detailUrl)
        parseDetail(text)


if __name__ == '__main__':
    runSpider()
