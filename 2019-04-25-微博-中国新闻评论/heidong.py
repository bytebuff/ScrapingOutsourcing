import requests
import json,time
from parsel import Selector

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': '_T_WM=83f78aea5a22b368ba2db51c618414e5; SUB=_2A25xqpTBDeRhGeNO6VMY9SvEyTuIHXVTVDyJrDV6PUJbkdAKLRD5kW1NTwRvuZs_aq-VSJR8Urd-KOvLcFb6NCvc; SUHB=079ja78HU6Rh2_; SCF=Aogx8LXbX0KaWx3L0LzCLKrxoTzI9iu1fXkvbOfScH2lt8KCbebPTZzKhmcKBumALFBZEwK102hpo1rlL5CNaFM.; SSOLoginState=1554965649; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4359636583226362%26luicode%3D10000011%26lfid%3D1005051784473157; WEIBOCN_FROM=1110106030',
    'referer': 'https://weibo.cn/comment/Hp1q2dxk6?rl=1&page=3',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}


def save2File(data):
    with open(r'C:\Users\19609\Desktop\SpiderEnv\微博-中国新闻评论\xian.txt','a',encoding='utf-8') as fp:
        fp.write(data+'\n')

try:

    for page in range(2215, 2503):
        url = f'https://weibo.cn/comment/HpBbTqPVW?uid=6105713761&rl=1&page={page}'
        print(url)
        response = requests.get(url, headers=headers)
        #time.sleep(1)
        response.encoding='utf-8'
        selector = Selector(text=response.text)
        # 选择评论
        content = selector.xpath('//span[@class="ctt"]/text()').getall()
        for con in content:
            if con != '回复':
                print(con)
                save2File(con)
except:
    print(f'出错啦++{url}')