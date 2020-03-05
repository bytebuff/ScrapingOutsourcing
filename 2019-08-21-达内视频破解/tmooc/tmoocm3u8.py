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
    'Cookie': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'Host': 'tts.tmooc.cn',
    'Referer': 'http://tts.tmooc.cn/studentCenter/toMyttsPage?versionCode=CGB_A_V02',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}

headers2 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'isCenterCookie=no; eBoxOpenCGB_A_V02=true; Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1555683308; TMOOC-SESSION=68F8C30ADE2C4DD5BAFF1C30BB5D886E; Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1555683388; sessionid=68F8C30ADE2C4DD5BAFF1C30BB5D886E|E_bfumcl2; cloudAuthorityCookie=0; versionListCookie="CGB_A_V02,,JSD_N_V09"; defaultVersionCookie=CGB_A_V02; versionAndNamesListCookie=CGB_A_V02N22NCGB_A_V02M11MJSD_N_V09N22NJSD_N_V09; courseCookie=CGB; stuClaIdCookie=685942; tedu.local.language=zh-CN; Hm_lvt_e997f0189b675e95bb22e0f8e2b5fa74=1555686031; JSESSIONID=FD678D3E10A346FEEE6358BB98EC1A5C; Hm_lpvt_e997f0189b675e95bb22e0f8e2b5fa74=1555762950',
    'Host': 'tts.tmooc.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',

}

headers3 = {
    'Origin': 'http://tts.tmooc.cn',
    'Referer': 'http://tts.tmooc.cn/video/showVideo?menuId=582783&version=CGB_A_V02',
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
        yield video_name, video_href


def get_m3u8(video_name, video_href):
    response = requests.get(video_href, headers=headers2)
    all_video = re.findall("""onclick="changeVideo\('(.*?)\.m3u8',this\)" title="(.*?)">""", response.text, flags=re.S)
    for video in all_video:
        title_name = video[1]
        m3u8_url = f'http://c.it211.com.cn/{video[0]}/{video[0]}.m3u8'
        response_m3u8 = requests.get(m3u8_url, headers=headers3)
        # 提取key的url
        url_key = re.search('URI="(.*?)"', response_m3u8.text).group(1)
        #'http://c.it211.com.cn/cgb19020226pm/static.key'
        key = download_key(url_key)
        url_ts = re.findall('http://c\.it211\.com\.cn/.*?\.ts', response_m3u8.text)
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

    url_l = 'http://tts.tmooc.cn/studentCenter/toMyttsPage?versionCode=CGB_A_V02'
    url_2 = 'http://tts.tmooc.cn/studentCenter/toMyttsPage?versionCode=JSD_N_V09'
    switch_url = input('请选择下载第一个(输入:1)还是第二个视频(输入:2)：')
    if switch_url=='1':
        print(url_l)
        video_menuId = get_menuId(url_l)
        for video_name, video_href in video_menuId:
            get_m3u8(video_name, video_href)
    elif switch_url=='2':
        print(url_2)
        video_menuId = get_menuId(url_l)
        for video_name, video_href in video_menuId:
            get_m3u8(video_name, video_href)
