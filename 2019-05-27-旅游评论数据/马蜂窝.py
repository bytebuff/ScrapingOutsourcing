import requests
import re

url = 'https://m.mafengwo.cn/poi/poi/comment_page'

for page in range(1, 30):

    data = {
        'page': page,
        'poiid': '1392109'
    }

    headers = {
        'Host': 'm.mafengwo.cn',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://m.mafengwo.cn/poi/comment_1392109.html',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '20',
        'Cookie': 'wakeApp_unshow_baidu=1; mfw_uuid=5c08d207-46e8-ade4-3071-d34e880ad423; _r=baidu; _rp=a%3A2%3A%7Bs%3A1%3A%22p%22%3Bs%3A18%3A%22www.baidu.com%2Flink%22%3Bs%3A1%3A%22t%22%3Bi%3A1544081927%3B%7D; __mfwlv=1552633646; __mfwvn=4; __mfwlt=1552638001; PHPSESSID=m4s83s9r6sevdhua812p14qe66; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222019-03-15+11%3A17%3A18%22%3B%7D; isDownClick_adis_baidu=1; ad_show=0',
        'Connection': 'keep-alive'
    }

    response = requests.post(url, data=data, headers=headers)
    print(response)
    print(type(response.json()['html']))
    data = re.findall('<div class="context line5">(.*?)</div>', response.json()['html'], flags=re.S)
    for dat in data:
        with open('马蜂窝数据.csv', 'a', encoding='utf-8') as fp:
            fp.write(dat.strip()+'\n')