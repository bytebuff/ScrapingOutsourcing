import requests
import json
import random
import time

url = 'https://sec-m.ctrip.com/restapi/soa2/12530/json/viewCommentList?_fxpcqlniredt=09031143210783581354'

for page in range(48,263): # 480 366
    print('正在采集第【', page, '】页')
    data = {"pageid":10650000804,"viewid":20449,"tagid":0,"pagenum":259,"pagesize":10,"contentType":"json","head":{"appid":"100013776","cid":"09031143210783581354","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":"","extension":[]},"ver":"7.10.3.0319180000"}

    headers = {
        'Host': 'sec-m.ctrip.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://piao.ctrip.com/ticket/dest/t20449.html',
        'content-type': 'application/json',
        'cookieorigin': 'https://piao.ctrip.com',
        'origin': 'https://piao.ctrip.com',
        'Content-Length': '268',
        'Cookie': '_abtest_userid=bd32d639-7281-441e-b72e-90d1b8120eab; _bfa=1.1545476740516.2yjm6o.1.1552619952224.1552633556383.8.22.0; _RF1=110.184.224.240; _RSG=gG4Ki912qCFm5cfpE4yIBA; _RDG=289c74bdc798952e0f32ae10f4aa41af57; _RGUID=f3340812-6c50-442a-a2d2-f043b3a66170; Mkt_UnionRecord=%5B%7B%22aid%22%3A%22106174%22%2C%22timestamp%22%3A1549803515226%7D%2C%7B%22aid%22%3A%2266672%22%2C%22timestamp%22%3A1551851392633%7D%5D; _jzqco=%7C%7C%7C%7C%7C1.1579471169.1548334906201.1552619955284.1552633559234.1552619955284.1552633559234.0.0.0.9.9; __zpspc=9.5.1552633559.1552633559.1%231%7C%7C%7C%7C%7C%23; _fpacid=09031143210783581354; GUID=09031143210783581354; MKT_Pagesource=PC; appFloatCnt=1; manualclose=1; gad_city=be2e953e1ae09d16d9cc90a550611388',
        'Connection': 'keep-alive',
    }

    # proxies = {
    #     'https': ,
    #     'https':
    # }
    time.sleep(random.randint(1, 5))

    response = requests.post(url, json=data, headers=headers)
    u = 'https://sec-m.ctrip.com/restapi/soa2/12530/json/viewCommentList?_fxpcqlniredt=09031143210783581354'
    requests.options(u)
    # print(response.json())
    if response.json()['data']:

        for data in response.json()['data']['comments']:
            d = data['content']
            print(d)
            with open('旅游评论数据/携程.csv', 'a', encoding='utf-8') as fp:
                fp.write(d + '\n')