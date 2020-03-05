"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: microSpider.py
    @time: 2019/11/30 16:09
    @desc:
"""
import aiohttp
import asyncio

# 初始化网址
start_urls = ['https://github.com/scrapyhub/aioScrapy/blob/master/minScrapy.py']

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
async def download(session, url):
    # 在此处激活配置文件
    async with session.get(url, headers=settings['headers']) as response:
        return await response.text()


# engine引擎 处理相关事务 (下载器、 爬虫文件、管道文件)
async def engine():
    async with aiohttp.ClientSession() as session:
        for url in start_urls:
            response = download(session, url)
            await parse(response)


# 解析数据(spider文件)
async def parse(response):
    print(response)


# 管道文件(item)
async def item():
    pass

def crawl():

    loop = asyncio.get_event_loop()
    loop.run_until_complete(engine())


if __name__ == '__main__':
    crawl()
