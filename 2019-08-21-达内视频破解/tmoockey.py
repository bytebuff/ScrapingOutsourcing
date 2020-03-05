import requests
# pip install pycryptodome
from Crypto.Cipher import AES # AES 对称加密


HEADERS = {
    'Origin': 'http://tts.tmooc.cn',
    'Referer': 'http://tts.tmooc.cn/video/showVideo?menuId=582783&version=CGB_A_V02',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}


def download_key(url_key):
    '''

    :param url_key: m3u8文件中对应的key的url
    :return: 返回该url对应的响应数据，也就是key值(该值需要解密)
    '''
    response_key = requests.get(url_key, headers=HEADERS).content  # 下载key
    return response_key


def download_ts(url_ts):
    '''
    :param url_ts: ts文件的url
    :return: 返回该网址对应的数据
    '''
    response_ts = requests.get(url_ts, headers=HEADERS).content  # 下载key
    return response_ts

def aes_key_and_ts(key, ts):
    '''

    :param key: 钥匙
    :param ts: ts文件
    :return: 解密后的数据
    '''
    data = AES.new(key, AES.MODE_CBC, ts[0:16]).decrypt(ts[16:])
    return data

def save_mp4(file_name, data):
    """
    :param file_name: 存储的位置
    :param data: 存储的数据
    :return: None
    """
    with open(file_name+'.mp4', 'ab') as fp:
        fp.write(data)

if __name__ == '__main__':
    url_key = 'http://c.it211.com.cn/cgb19020226pm/static.key'
    key = download_key(url_key)
    for page in range(0, 199):
        url_ts = f'http://c.it211.com.cn/cgb19020226pm/cgb19020226pm-{page}.ts'
        ts = download_ts(url_ts)
        data = aes_key_and_ts(key, ts)
        save_mp4('666', data)