"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: anjuke.py
    @time: 2019/11/16 14:40
    @desc: https://sh.sydc.anjuke.com/sp-shou/xuhuiqu/ 列表页
            获取全部详情页的网址 保存到文件中去
"""

'''
上海: 浦东(70) https://sh.58.com/pudongxinqu/shangpucz/pn70 
上海: 闵行(70) https://sh.58.com/minxing/shangpucz/pn2/
上海: 松江(48) https://sh.58.com/songjiang/shangpucz/pn48/
上海: 宝山(57) https://sh.58.com/baoshan/shangpucz/pn57
上海: 嘉定(50) https://sh.58.com/jiading/shangpucz/pn50/
上海: 徐汇(54) https://sh.58.com/xuhui/shangpucz/pn54/
上海: 青浦(20) https://sh.58.com/qingpu/shangpucz/pn20
上海: 静安(70) https://sh.58.com/jingan/shangpucz/pn70
上海: 普陀(55) https://sh.58.com/putuo/shangpucz/pn55
上海: 杨浦(54) https://sh.58.com/yangpu/shangpucz/pn54/
上海: 黄浦(13) https://sh.58.com/fengxiansh/shangpucz/pn13/
上海: 虹口(59) https://sh.58.com/huangpu/shangpucz/pn59/
上海: 长宁(40) https://sh.58.com/changning/shangpucz/pn40/
上海: 金山(10) https://sh.58.com/jinshan/shangpucz/pn10/
上海: 上海周边(4) https://sh.58.com/shanghaizhoubian/shangpucz/pn4/
'''

import re
from selenium import webdriver
from parsel import Selector


def getListView(url):
    driver.get(url)
    pageSource = driver.page_source
    # 如果出现验证码 就人工等待一下 验证 判断页面元素 验证码字符串是否在页面里面
    # 如果有验证码 那么就验证 验证以后需要重新加载页面

    # 本次访问做以下验证码校验
    if '验证码' in pageSource:
        print('你需要验证验证码，然后输入 ok 继续')
        word = input('请输入ok：')
        if word == 'ok':
            getListView(url)
    else:
        # 选择元素
        parseListView(pageSource)


def parseListView(response):
    '''
    解析详情页
    :param response:
    :return:
    '''
    selectors = Selector(text=response)
    selectors = selectors.xpath('//ul[@id="house-list-wrap"]/li')
    for selector in selectors:
        detailUrl = selector.xpath('./h2/a/@href').get()
        print(detailUrl)
        if 'target' not in detailUrl:
            saveDetailUrl(detailUrl)


def saveDetailUrl(url):
    '''
    保存详情页的网址
    :param url: 网址传递过来
    :return: None
    '''
    with open(f'{city}-网址.txt', 'a', encoding='utf-8') as fp:
        fp.write(url + '\n')


def readUrls():
    with open('urls') as fp:
        for url in fp:
            url = url.strip()
            maxPage = re.search('https://sh.58.com/.*?/shangpucz/pn(\d+)', url).group(1)
            city = re.search('https://sh.58.com/(.*?)/shangpucz/pn\d+', url).group(1)
            urlFormat = re.sub('shangpucz/pn(\d+)', 'shangpucz/pn{}', url)
            yield city, maxPage, urlFormat,


if __name__ == '__main__':

    driver = webdriver.Firefox()

    maxPageAndurlFormat = readUrls()

    for city, maxPage, urlFormat in maxPageAndurlFormat:
        for p in range(0, int(maxPage) + 1):
            url = urlFormat.format(p)
            getListView(url)

    driver.quit()  # 退出
