"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: 红楼.py
    @time: 2019/11/24 11:16
    @desc: 红楼梦数据采集
"""
import re, time
import requests

# 总网页 采集所有页数

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'purepen.com',
    'Pragma': 'no-cache',
    'Referer': 'http://purepen.com/hlm.htm',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
}


def getAllList():
    url = 'http://purepen.com/hlm/index.htm'
    response = requests.get(url, headers=headers, timeout=1200)
    return response.text


def parseAllList(text):
    urlList = re.findall('<TD><A HREF="(.*?)">', text)
    urls = []
    for url in urlList:
        url = f'http://purepen.com/hlm/{url}'
        urls.append(url)
    return urls


def detailRequest(url):
    response = requests.get(url, headers=headers, timeout=1200)
    time.sleep(1)
    response.encoding = 'gb2312'

    return response.text


def parseDetail(text):
    # 文本内容
    content = re.findall(r'size="3">(.*?)</font>', text, flags=re.S)
    if content:
        content = cleanData(content[1])
        saveData(content)
        print(content)


def cleanData(content):
    '''
    清洗数据 把不想关的去掉
    :param content: 导入的参数
    :return: 清洗后的参数
    '''
    # 去掉换行
    # content = re.sub(r'\n', '', content)
    # print(content)
    # 去掉&nbsp
    content = re.sub(r'&nbsp', '', content)
    # 去掉\u3000
    content = re.sub(r'\u3000', '', content)
    # 去掉<b>
    content = re.sub(r'<b>', '', content)

    return content


def saveData(content):
    with open('红楼梦.txt', 'a', encoding='utf-8') as fp:
        fp.write(content + '\n')


def runSpider():
    text = getAllList()
    allUrl = parseAllList(text)
    for url in allUrl:
        print(url)
        text = detailRequest(url)
        parseDetail(text)


if __name__ == '__main__':
    runSpider()
