import re, os
import requests
from parsel import Selector
from tmoockey import download_key, download_ts, aes_key_and_ts, save_mp4


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'eBoxOpenCGB_A_V02=true; isCenterCookie=no; cloudAuthorityCookie=0; versionListCookie=CGB_A_V02; defaultVersionCookie=CGB_A_V02; versionAndNamesListCookie=CGB_A_V02N22NCGB_A_V02; courseCookie=CGB; stuClaIdCookie=685942; tedu.local.language=zh-CN; TMOOC-SESSION=751AC251068147C2A1CA7BC452B25CB2; Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1565856075,1566398396,1566399968; Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1566399968; sessionid=751AC251068147C2A1CA7BC452B25CB2|E_bfumcl2; Hm_lvt_e997f0189b675e95bb22e0f8e2b5fa74=1566399068,1566399225,1566400002,1566400008; JSESSIONID=D8FD17F42300AE9B6613862ACF394CFC; Hm_lpvt_e997f0189b675e95bb22e0f8e2b5fa74=1566400018',
    'Host': 'tts.tmooc.cn',
    'Referer': 'https://tts.tmooc.cn/studentCenter/toMyttsPage?versionCode=CGB_A_V02',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}

headers2 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'eBoxOpenCGB_A_V02=true; isCenterCookie=no; cloudAuthorityCookie=0; versionListCookie=CGB_A_V02; defaultVersionCookie=CGB_A_V02; versionAndNamesListCookie=CGB_A_V02N22NCGB_A_V02; courseCookie=CGB; stuClaIdCookie=685942; tedu.local.language=zh-CN; TMOOC-SESSION=751AC251068147C2A1CA7BC452B25CB2; Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1565856075,1566398396,1566399968; Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1566399968; sessionid=751AC251068147C2A1CA7BC452B25CB2|E_bfumcl2; Hm_lvt_e997f0189b675e95bb22e0f8e2b5fa74=1566399068,1566399225,1566400002,1566400008; JSESSIONID=D8FD17F42300AE9B6613862ACF394CFC; Hm_lpvt_e997f0189b675e95bb22e0f8e2b5fa74=1566400018',
    'Host': 'tts.tmooc.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}

headers3 = {
    'Origin': 'https://tts.tmooc.cn',
    'Referer': 'https://tts.tmooc.cn/video/showVideo?menuId=582783&version=CGB_A_V02',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}

def get_menuId(url):
    response = requests.get(url, headers=headers)
    selectors = Selector(text=response.text).xpath('//div[@class="course-menu"]/ul/li[@class="opened"]')
    for selector in selectors:
        video_name = selector.xpath('./p/text()').get().strip()
        video_href = selector.xpath('./ul/li[@class="sp"]/a/@href').get()
        video_name = ''.join(video_name.split())
        video_href = video_href
        print(video_name, '-->', video_href)
        yield video_name, video_href


def get_m3u8(video_name, video_href):
    response = requests.get(video_href, headers=headers2)
    # print(response.text)
    # all_video = re.findall(r"""onclick="changeVideo('(.*?)',this)" title="(.*?)">""", response.text, flags=re.S)
    all_video = re.findall(r"""onclick="changeVideo\('(.*?)\.m3u8',this\)" title="(.*?)">""", response.text, flags=re.S)
    # print(all_video)
    for video in all_video:
        title_name = video[1] # 每个视频的名字
        m3u8_url = f'https://c.it211.com.cn/{video[0]}/{video[0]}.m3u8'
        response_m3u8 = requests.get(m3u8_url, headers=headers3, verify=False)
        # 提取key的url  http://tts.tmooc.cn/video/saveVideoStatsLog?menuId=582796
        url_key = re.search('URI="(.*?)"', response_m3u8.text).group(1)
        #'http://c.it211.com.cn/cgb19020226pm/static.key'
        key = download_key(url_key)
        # 提取ts的所有网址
        url_ts = re.findall('https://c\.it211\.com\.cn/.*?\.ts', response_m3u8.text)
        for ts_url in url_ts:
            ts = download_ts(ts_url)
            data = aes_key_and_ts(key, ts)
            video_path = f'./{video_name}/'
            makedir_video(video_path)
            print(title_name)
            save_mp4(video_path+title_name, data)


def makedir_video(video_path):

    os.makedirs(video_path, exist_ok=True)



if __name__ == '__main__':

    url = 'https://tts.tmooc.cn/studentCenter/toMyttsPage'
    video_menuId = get_menuId(url)
    for video_name, video_href in video_menuId:
        # 保存视频
        get_m3u8(video_name, video_href)