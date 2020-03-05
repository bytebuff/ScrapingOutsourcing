#coding:utf-8

import requests
from bs4 import BeautifulSoup
import re
import time

def getHtml(url):
    '''得到网页内容，使用requests'''
    r = requests.get(url)
    r.encoding = "gb18030"  #这个网站采用的不是utf-8，而是gb18030，它比gbk更广
    return r.text

def getLinks(html):
    '''得到页面中的链接，使用soup'''
    soup = BeautifulSoup(html, 'html.parser')  #得到soup对象
    div = soup.find('table', attrs={'cellpadding':"3"})  #找到特定的一个table
    links = div.find_all('a') #找到所有的链接
    
    #或者用下面的找到满足一定条件的链接
    links = div.find_all('a', attrs={'href': re.compile(r'\d{3}\.htm')})  #找到特定的链接
    print(links) 
    return links


url = "http://www.purepen.com/hlm/"
# 得到目录页
html = getHtml(url)
# 从目录页中找到子页的链接
links = getLinks(html)
# 显示所有的链接的地址及文本
for link in links:
    #每个link是一个链接对象（而不是一个字符串）
    print(link['href'])  #取得它的链接地址
    print(link.text.replace('\u3000', ' ') )  #取得文本，那里有个特殊的字符要处理一下

