import requests
import json

url = 'http://jdzzy.gaokaow.cc/Data/ScoreLines/UCodes/QueryList?provinceId=855&collegeId=4193'

data = {
    "provinceId": 855,
    "collegeId": 4193
}

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Cookie': 'Youzy2BCurrentProvince=%7B%22provinceName%22%3A%22%E5%9B%9B%E5%B7%9D%22%2C%22provinceId%22%3A%22855%22%7D; connect.sid=s%3AsmT9tY6QHV-yNT5g0pDeA_lueqzgD1pa.tHPxoaTLmTrv0GsPG7ProNaMuS%2FIElG6EOchkMjkCuE; Youzy2BStore=%7B%22id%22%3A%225c6be8819e742b010419123a%22%2C%22numId%22%3A4210%2C%22name%22%3A%22%E9%87%91%E7%82%B9%E5%AD%90%E5%BF%97%E6%84%BF%22%2C%22storeLogoUrl%22%3A%22http%3A%2F%2Fimg3.youzy.cn%2Fcontent%2Fmedia%2Fthumbs%2Fp00039732.png%22%2C%22provinceName%22%3A%22%E5%9B%9B%E5%B7%9D%22%2C%22openProvinces%22%3A%22%E5%9B%9B%E5%B7%9D%22%2C%22provinceNumId%22%3A%22855%22%2C%22openProvinceIds%22%3A%22855%22%2C%22h5Address%22%3A%22http%3A%2F%2Fjdzzym.gaokaow.cc%22%2C%22isOpened%22%3Afalse%2C%22theme%22%3A%7B%22theme%22%3A0%2C%22themeNavi%22%3A1%2C%22themePageOfHome%22%3A1%7D%7D',
    'Host': 'jdzzy.gaokaow.cc',
    'Origin': 'http://jdzzy.gaokaow.cc',
    'Referer': 'http://jdzzy.gaokaow.cc/tzySearch/colleges/homepage?cid=896',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

response = requests.post(url, headers=headers)

# print(response.json())
print(response.text)