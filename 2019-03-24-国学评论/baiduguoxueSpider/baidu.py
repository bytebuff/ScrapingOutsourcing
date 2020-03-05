import requests
import re

url = 'https://www.baidu.com/s?wd=%E5%9B%BD%E5%AD%A6%E5%9F%B9%E8%AE%AD&pn=30'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
}
response = requests.get(url, headers=headers)

title = re.findall('data-tools=\'{"title":"(.*?)","url":', response.text)
content = re.findall('class="c-abstract">(.*?)target="_blank"', response.text)
print(title)
print(content)
print(len(title))
print(len(content))