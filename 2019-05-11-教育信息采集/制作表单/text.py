import requests

url = 'https://yz.chsi.com.cn/zsml/queryAction.do'

data = {'ssdm': '11',
        'dwmc': '',
        'mldm': '13',
        'mlmc': '',
        'yjxkdm': '1305',
        'zymc': '信息艺术设计',
        'xxfs': ''}

response = requests.post(url, data=data)

with open('test.html', 'w', encoding='utf-8') as fp:
    fp.write(response.text)

