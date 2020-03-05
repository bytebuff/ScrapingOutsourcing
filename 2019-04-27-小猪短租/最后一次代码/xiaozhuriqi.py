import re
import requests

url = 'http://sh.xiaozhu.com/ajaxRequest/AJAX_GetLodgeUnitCalendar'

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'gr_user_id=4844e1fa-126f-43d0-909f-5af5f96866e6; 59a81cc7d8c04307ba183d331c373ef6_gr_last_sent_cs1=N%2FA; grwng_uid=a409c431-1140-4e26-95e7-2e69a55e5a31; xz_guid_4se=03459fce-2235-4d5b-9e84-a36ee4184660; _uab_collina=155358561150539202408096; abtest_ABTest4SearchDate=b; 59a81cc7d8c04307ba183d331c373ef6_gr_session_id=9172aaf1-1df1-4252-b981-f0ca033f08da; SPIDER_AVOID_TOKEN_calendar=b2e0c792ad68362d6dd72f0dc9a7be61; 59a81cc7d8c04307ba183d331c373ef6_gr_last_sent_sid_with_cs1=9172aaf1-1df1-4252-b981-f0ca033f08da; 59a81cc7d8c04307ba183d331c373ef6_gr_session_id_9172aaf1-1df1-4252-b981-f0ca033f08da=true; xzuuid=d9bb88ce; TY_SESSION_ID=fab65245-7fff-4181-93b1-e0361e8fb396; rule_math=ca5t4kewww',
    'Host': 'sh.xiaozhu.com',
    'Referer': 'http://sh.xiaozhu.com/fangzi/99382335701.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Tingyun-Id': 'uxh10gyAidI;r=753569265',
    'xSRF-Token': '6796b23645814829dc53104a9e33aaa7',
}

with open('urls.txt','r') as fp:
    for line in fp:
        url = line.strip()
        print(url)
        url_id = re.search('fangzi/(\d+)\.html', url).group(1)
        print(url_id)
        for date in range(4, 10):
            params = {
                'lodgeunitid': f'{url_id}',
                'startdate': f'2019-0{date}-01',
                'enddate': f'2019-0{date+1}-01', # 修改日期  想要获取每个月所有的 改成月初  例如五月数据 2019-07-01
                'editable': 'true',
                'calendarCode': 'true',
                'rand': '0.013787678797468228',
                'spiderAvoidToken': 'b2e0c792ad68362d6dd72f0dc9a7be61'
            }

            response = requests.post(url, headers=headers, params=params)

            for data in response.json():
                if data.get('state') == 'unavailable':
                    with open('state.csv', 'a') as fp:
                        fp.write(str(data)+'\n')