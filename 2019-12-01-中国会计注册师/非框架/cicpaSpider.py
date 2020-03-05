"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: cicpaSpider.py
    @time: 2019/12/1 22:18
    @desc:
"""
import requests

urlPost = 'http://cmispub.cicpa.org.cn/cicpa2_web/PersonIndexAction.do'
headers = {
    'Accept': 'image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*',
    'Referer': 'http://cmispub.cicpa.org.cn/cicpa2_web/PersonIndexAction.do',
    'Accept-Language': 'zh-CN',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Length': '113',
    'Host': 'cmispub.cicpa.org.cn',
    'Connection': 'Keep-Alive',
    'Pragma': 'no-cache',
    'Cookie': 'JSESSIONID=E1F413262CE28895AE01DEEABF4525CA; cookiee=20111116',

}
data = {
    'method': 'indexQuery',
    'queryType': '2',
    'isStock': '00',
    'pageSize': '',
    'pageNum': '',
    'ascGuid': '',
    'offName': '',
    'perCode': '',
    'perName': '包西成'
}
response = requests.get(urlPost, params=data, headers=headers)

with open('baoxicheng.html', 'wb') as fp:
    fp.write(response.content)
