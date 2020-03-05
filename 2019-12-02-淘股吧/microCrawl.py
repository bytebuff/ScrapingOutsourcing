import requests

# 初始化网址
start_urls = []

# 配置文件
settings = {
    'headers': {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    },  # dict 字典格式
    'timeout': 20  # 超时时间
}


# 下载器 用来下载响应
def download(session, url):
    # 在此处激活配置文件
    with session.get(url, headers=settings['headers']) as response:
        return response.text  # 返回文本响应


# engine引擎 处理相关事务 (下载器、 爬虫文件、管道文件)
def engine():
    with requests.Session() as session:
        for url in start_urls:
            response = download(session, url)
            parse(response)


# 解析数据(spider文件)
def parse(response):
    pass


# 管道文件(pipelines管道)
def pipeline(item):
    pass


if __name__ == '__main__':
    engine()
