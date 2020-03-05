import requests,re
from parsel import Selector
from lxml import etree
from bs4 import BeautifulSoup

url = 'https://www.yescoin.top/auction-admin/wapi/pc/content/8a8080af6a205bda016a20b41d1e1f66'

headers = {
'accept': 'application/json',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
#'content-length': '52',
'content-type': 'application/json',
'cookie': '_ga=GA1.2.2073613626.1555377379; _gid=GA1.2.2010780058.1555377379',
'i18n': 'hk',
'origin': 'https://www.yescoin.top',
'referer': 'https://www.yescoin.top/',
'token': '',
'tokenauth': 'front',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}

cookie = {
    'Cookie': ''
}

form = {"code":"sys_message",
        "currentPage":1,
        "pageSize":15}

response = requests.post(url, headers=headers).json()
json_data = response['contents'][0]['content']
selector = Selector(text=json_data)
data = selector.xpath('//p[@class="MsoNormal"]//font/text()').getall()
print(''.join(data))