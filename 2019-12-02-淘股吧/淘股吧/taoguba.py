"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: taoguba.py
    @time: 2019/11/30 15:00
    @desc:
"""
import csv, time, re
import requests
import pandas as pd


def getOnePage(searchWord):
    url = f'https://www.taoguba.com.cn/getSearchTopicResult?pageNo=1&searchDate=6&subject={searchWord}&type=3'
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'notActiveUserIDPC=105368870; UM_distinctid=16ebac350a021d-09833131d58627-7711b3e-100200-16ebac350a135c; Hm_lvt_cc6a63a887a7d811c92b7cc41c441837=1575091394; JSESSIONID=2816dd11-8e0d-4edc-819f-c26b4e61ada8; tgbuser=3655717; tgbpwd=23224C7C586jt2ft0pwynvx8zt; onedayyszc=1575129600000; CNZZDATA1574657=cnzz_eid%3D1166600985-1575087774-%26ntime%3D1575093174; Hm_lpvt_cc6a63a887a7d811c92b7cc41c441837=1575097341',
        'pragma': 'no-cache',
        'referer': 'https://www.taoguba.com.cn/search?searchContent=%E6%96%B0%E5%BC%80%E6%BA%90&type=0',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    response = requests.get(url, headers=headers)
    return response.json()


def parseOnePage(jsonData, code, word):
    if jsonData.get('dto'):
        for dat in jsonData['dto']['topicAttr']:
            body = dat.get('body')
            body = cleanData(body)
            subject = dat.get('subject')
            postDate = dat.get('postDate')
            postDate = timeStamp(postDate)
            items = [
                code,
                word,
                postDate,
                subject,
                body,
            ]
            print(items)
            saveFile(items)


def timeStamp(timeStamp):
    timaArry = time.localtime(timeStamp / 1000)
    dt = time.strftime('%Y-%m-%d %H:%M:%S', timaArry)
    return dt


def cleanData(text):
    text = re.findall('[\u4e00-\u9fa5]', text)
    return ''.join(text)


def saveFile(item):
    with open('taoguba' + '.csv', 'a', encoding='utf-8', newline='') as fp:
        csvWriter = csv.writer(fp)
        csvWriter.writerow(item)
        fp.flush()


def getSearchWord():
    df = pd.read_excel('全部A股代码及名称.xlsx')
    zhengQuanCode = df['证券代码']
    zhengQuanName = df['证券名称']
    codeWords = []
    for code, word in zip(zhengQuanCode, zhengQuanName):
        codeWords.append((code, word))
    return codeWords

if __name__ == '__main__':
    codeWords = getSearchWord()
    # print(codeWords)
    for code, word in codeWords[1:3]:
        jsonData = getOnePage(word)
        parseOnePage(jsonData, code, word)
