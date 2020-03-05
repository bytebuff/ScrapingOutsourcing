"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: test.py
    @time: 2019/11/30 17:07
    @desc:
"""
import base64
import requests

url = 'http://127.0.0.1:8001/geckocr'

with open('code.php.png', 'rb') as fp:
    img = base64.b64encode(fp.read())
    data = {
        'img': str(img)[1:]
    }
    result = requests.post(url, data=data)
    print(result)
