import requests

url = 'http://sh.xiaozhu.com/ajaxRequest/AJAX_GetLodgeUnitCalendar?lodgeunitid=99382335701&startdate=2019-08-01&enddate=2019-09-01&editable=true&calendarCode=true&rand=0.5980195335942269&spiderAvoidToken=b2e0c792ad68362d6dd72f0dc9a7be61&_=0.3072013775391138'

headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_uab_collina=155350740949073319393702; gr_user_id=4844e1fa-126f-43d0-909f-5af5f96866e6; 59a81cc7d8c04307ba183d331c373ef6_gr_last_sent_cs1=N%2FA; grwng_uid=a409c431-1140-4e26-95e7-2e69a55e5a31; xz_guid_4se=03459fce-2235-4d5b-9e84-a36ee4184660; _uab_collina=155358561150539202408096; abtest_ABTest4SearchDate=b; 59a81cc7d8c04307ba183d331c373ef6_gr_session_id=9be3fa82-3c61-425d-9c1a-e156d4ed47e4; 59a81cc7d8c04307ba183d331c373ef6_gr_session_id_9be3fa82-3c61-425d-9c1a-e156d4ed47e4=true; TY_SESSION_ID=78d7cca8-a26c-42a8-8ea3-a74c4d20d992; SPIDER_AVOID_TOKEN_calendar=25315d7e8e32b1441d08e0663d3e3187',
        'Host': 'sh.xiaozhu.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        }

response = requests.get(url, headers=headers)

print(response.json())