#coding:utf-8
'''爬取大学排名'''

import requests
from bs4 import BeautifulSoup

allUniv = [] #大学列表

def getHtml(url):
    '''得到网页内容'''
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""

def getUniversities(soup):
    '''打到我们要的数据'''
    rows = soup.find_all('tr') #所有的表格行
    for tr in rows:
        cells = tr.find_all('td')  #所有的单元格
        if len(cells)==0:
            continue
        
        singleUniv = [] #用来存放各项数据
        for td in cells:
            singleUniv.append(td.text)
        allUniv.append(singleUniv) #加入到总列表中

def printUniversitiesTop(num):
    print("排名","学校名称","省市","总分","培养规模")
    for i in range(num):
        u=allUniv[i]
        print(u[0],u[1],u[2],u[3],u[6])

def main():
    #获得网页内容
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHtml(url)
    #解析得到数据
    soup = BeautifulSoup(html, "html.parser")
    getUniversities(soup)
    #显示前10名
    printUniversitiesTop(10)

main()
