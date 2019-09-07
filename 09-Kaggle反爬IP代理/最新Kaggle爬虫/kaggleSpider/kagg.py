import requests
import random

url = 'http://webapi.http.zhimacangku.com/getip?num=15&type=1&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=4&sb=0&pb=4&mr=1&regions='
#
proxies = {
    'https':'110.188.2.32:443',
    'http':'110.188.2.32:443'
}

response = requests.get(url).text

print(response.split('\n'))

