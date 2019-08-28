import requests
from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r'C:\Users\19609\Desktop\SpiderEnv\抖音加密破解\signture.html')

desc = driver.find_element_by_xpath('//body').text
print(desc)
url = f'https://www.iesdouyin.com/aweme/v1/aweme/post/?user_id=111131234898&count=21&max_cursor=0&aid=1128&_signature={desc}&dytk=de5486e77c8a63e6660b78edc4e59020'
print(url)
headers = {
    'Host': 'www.iesdouyin.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.iesdouyin.com/share/user/111131234898?u_code=16l7ecm65&timestamp=1553152590',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Cookie': 'tt_webid=6663253908318815751; _ba=BA0.2-20190301-5199e-6YMUtKVQH3EJFK22eEtm',
}

response = requests.get(url,headers=headers)
print(response.json())