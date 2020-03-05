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
上海: 徐汇区 总共18页 https://sh.sydc.anjuke.com/sp-shou/xuhuiqu-p2
上海: 长宁区 总共7页 https://sh.sydc.anjuke.com/sp-shou/changningqu-p2/
上海: 杨浦区 总共8页 https://sh.sydc.anjuke.com/sp-shou/yangpuqu-p2/
上海: 静安区 总共23页 https://sh.sydc.anjuke.com/sp-shou/jinganqu-p2/
上海: 普陀区 总共8页 https://sh.sydc.anjuke.com/sp-shou/putuoqu-p2/
'''

from selenium import webdriver
from parsel import Selector


def getListView(p):
    url = f'https://sh.sydc.anjuke.com/sp-shou/putuoqu-p{p}/'
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
    selectors = selectors.xpath("//a[@class='list-item']")
    for selector in selectors:
        detailUrl = selector.xpath('./@href').get()
        print(detailUrl)
        saveDetailUrl(detailUrl)


def saveDetailUrl(url):
    '''
    保存详情页的网址
    :param url: 网址传递过来
    :return: None
    '''
    with open('普陀网址.txt', 'a', encoding='utf-8') as fp:
        fp.write(url + '\n')


if __name__ == '__main__':

    driver = webdriver.Chrome()

    for p in range(1, 8+1):
        getListView(p)

    driver.quit()  # 退出
