import time
import requests

url = 'https://sh.xiaozhu.com/ajaxRequest/Ajax_GetDetailComment?lodgeId=34233760203&cityDomain=undefined&p=2'

headers={
    'Host': 'sh.xiaozhu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    #'Referer': 'http://sh.xiaozhu.com/fangzi/38803159503.html',
    'xSRF-Token': 'b8f6355ee91c08a80988a8770177bfef',
    'X-Requested-With': 'XMLHttpRequest',
    #'X-Tingyun-Id': 'uxh10gyAidI;r=587459799',
    'Connection': 'keep-alive',
    #'Cookie': 'abtest_ABTest4SearchDate=b; rule_math=zmmeavqj2qq',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

params = {
    'lodgeId': '34233760203',
    'cityDomain': 'undefined',
    'p': '2'
}

response = requests.get(url, headers=headers)

print(response.text)