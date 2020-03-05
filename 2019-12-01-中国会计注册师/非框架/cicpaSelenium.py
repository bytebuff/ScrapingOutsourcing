"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: cicpaSelenium.py
    @time: 2019/12/1 22:36
    @desc:
"""
import re
from selenium import webdriver


def sendKey(word):
    inputWord = driver.find_element_by_xpath('//input[@name="perName"]')
    inputWord.clear()
    inputWord.send_keys(word)

    clickWord = driver.find_element_by_xpath('//img[@align="absmiddle"]')
    clickWord.click()

    # 提取 ViewDetail
    pageSource = driver.page_source
    getViewDetail(pageSource, word)
    # 查看有多少页
    try:
        pages = re.search('条记录 / 共 (\d+) 页 / 当前第', pageSource).group(1)
        if int(pages) > 1:
            for page in range(int(pages) - 1):
                # 点击下一页
                driver.find_element_by_partial_link_text('下一页').click()
                pageSource = driver.page_source
                getViewDetail(pageSource, word)

    except:
        print('这个人可能有问题', word)
        with open('第三次采集目标错误名单.txt', 'a', encoding='utf-8') as fp:
            fp.write(word+"\n")


def getViewDetail(pageSource, word):
    viewDetail = re.findall(f"javascript:viewDetail\('(.*?)','{word}'\)", pageSource)
    print(viewDetail)
    for view in viewDetail:
        saveViewDetail(view)


def saveViewDetail(view):
    with open('第三次采集目标名单.txt', 'a', encoding='utf-8') as fp:
        fp.write(view + '\n')


def getSearchWord():
    with open('第三次采集.txt', encoding='utf-8') as fp:
        for word in fp:
            word = word.strip()
            yield word


if __name__ == '__main__':
    driver = webdriver.Ie()
    driver.get('http://cmispub.cicpa.org.cn/cicpa2_web/public/query0/2/00.shtml')
    driver.switch_to.frame(0)
    words = getSearchWord()
    for word in words:
        sendKey(word)
