"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: 获取详细信息.py
    @time: 2019/12/2 18:29
    @desc: 获取详细信息
"""
import csv, re, time
import requests
from parsel import Selector

def readViewDetail():
    with open('viewDetail.txt') as fp:
        for word in fp:
            yield word.strip()

# 初始化网址
start_urls = ['http://cmispub.cicpa.org.cn/cicpa2_web/07/806E389E384F09EB8569317E991AC586.shtml' for i in range(1,10)]

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
        time.sleep(0.5)
        response.encoding = 'gbk'
        return response.text  # 返回文本响应


# engine引擎 处理相关事务 (下载器、 爬虫文件、管道文件)
def engine():
    with requests.Session() as session:
        for url in start_urls:
            print(url)
            response = download(session, url)
            parse(response)


# 解析数据(spider文件)
def parse(response):
    # 生日
    shengri = re.search('出生日期.*?</td>.*?<td class="data_tb_content".*?>(.*?)</td>', response, flags=re.S)
    if shengri:
        shengri = shengri.group(1)
    else:
        shengri = ''
    response = Selector(text=response)
    # 姓名
    xingming = response.xpath('//td[contains(text(),"姓名")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    xingbie = response.xpath('//td[contains(text(),"性别")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    zhiwu = response.xpath('//td[contains(text(),"所内职务")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    dangyuan = response.xpath('//td[contains(text(),"是否党员")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    xueli = response.xpath('//td[contains(text(),"学历")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    xuewei = response.xpath('//td[contains(text(),"学位")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    zhuanye = response.xpath('//td[contains(text(),"所学专业")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    xuexiao = response.xpath('//td[contains(text(),"毕业学校")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    kaohe = response.xpath('//td[contains(text(),"资格取得方式（考试/考核）")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    shuhao = response.xpath('//td[contains(text(),"全科合格证书号")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    nianfen = response.xpath('//td[contains(text(),"全科合格年份")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    bianhao = response.xpath('//td[contains(text(),"注册会计师证书编号")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    gudong = response.xpath('//td[contains(text(),"是否合伙人（股东）")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    jianhao = response.xpath('//td[contains(text(),"批准注册文件号")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    shijian = response.xpath('//td[contains(text(),"批准注册时间")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    wusuo = response.xpath('//td[contains(text(),"所在事务所")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    xueshi = response.xpath('//td[contains(text(),"本年度应完成学时")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    yixueshi = response.xpath('//td[contains(text(),"本年度已完成学时")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    xinxi = response.xpath('//td[contains(text(),"处罚/惩戒信息")]/following-sibling::td[1]/text()').get(default='')
    # 姓名
    huodong = response.xpath('//td[contains(text(),"参加公益活动")]/following-sibling::td[1]/text()').get(default='')
    # 生日
    items = {
        'xingming': xingming.strip(),
        'xingbie': xingbie.strip(),
        'zhiwu': zhiwu.strip(),
        'dangyuan': dangyuan.strip(),
        'xueli': xueli.strip(),
        'xuewei': xuewei.strip(),
        'zhuanye': zhuanye.strip(),
        'xuexiao': xuexiao.strip(),
        'kaohe': kaohe.strip(),
        'shuhao': shuhao.strip(),
        'nianfen': nianfen.strip(),
        'bianhao': bianhao.strip(),
        'gudong': gudong.strip(),
        'jianhao': jianhao.strip(),
        'shijian': shijian.strip(),
        'wusuo': wusuo.strip(),
        'xueshi': xueshi.strip(),
        'yixueshi': yixueshi.strip(),
        'xinxi': xinxi.strip(),
        'huodong': huodong.strip(),
        'shengri': shengri.strip(),
    }
    print(items)
    pipeline(items)



# 管道文件(pipelines管道)
def pipeline(item):
    with open('cicpa334.csv', 'a', encoding='utf-8', newline='') as fp:
        csvWriter = csv.writer(fp)
        data = [
            *item.values()
        ]
        csvWriter.writerow(data)


if __name__ == '__main__':
    engine()
