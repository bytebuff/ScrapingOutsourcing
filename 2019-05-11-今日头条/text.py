import requests

url = 'https://www.toutiao.com/api/pc/media_hot/?media_id=1571793867579394'

headers = {
    'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    #'cookie': 'UM_distinctid=166fe0ba04617d-038f51e6e279f9-36664c08-100200-166fe0ba047e8; _ga=GA1.2.1898673368.1541860477; uuid="w:a78cfb0a7a1149c387ba9125e80166fd"; tt_webid=6685562750024828429; csrftoken=0f8a82bb7b9ef1d9161a26c8e94407cd; tt_track_id=284dce931a7441a4aa6f1d4d4f0dc2c4; __tasessionId=ossr0308e1557576338151; CNZZDATA1259612802=368030108-1556600305-%7C1557577739',
    #'referer': 'https://www.toutiao.com/c/user/627222585572/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
}

response = requests.get(url, headers=headers)
print(response.text)