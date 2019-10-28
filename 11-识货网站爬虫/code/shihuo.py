import requests
from lxml import etree
import math
import re
from parseD import parseD

url = 'http://www.shihuo.cn/basketball/list?scene=%E7%AF%AE%E7%90%83%E9%9E%8B#qk=catalog'

res = requests.get(url)

html = etree.HTML(res.text)

# 第一级目录 选择所有的品牌
dat = html.xpath('//li[@class="clearfix brands"]//span[@class="t2"]/a/@href')

print(f'总共{len(dat)}也')

count = 0

# 循环进入第二级
for dat_url in dat[1:]:
    count += 1
    # 第一级网址
    print(f'正在爬第{count}也')
    d_urk = f'http:{dat_url}'
    print(f'网址是{d_urk}')
    # 进入第二级网址
    response2 = requests.get(d_urk)
    html2 = etree.HTML(response2.text)
    # 找出多少个商品
    numbers = int(html2.xpath('//div[@class="filter-activity"]/span/text()')[0])
    page_number = math.ceil(numbers/60)
    # 翻页
    for num in range(1, page_number+1):
        ul = re.sub('#qk=shaixuan', f'&page={num}', d_urk)
        # print(ul)
        response3 = requests.get(ul).text
        html3 = etree.HTML(response3)
        # 提取所有商品
        urls = html3.xpath('//ul[@id="js_hover"]/li/div[@class="title"]/a/@href')
        for ull in urls:
            ull = f'http:{ull}'
            print(ull)
            try:
                parseD(ull)
            except:
                pass

            # response4 = requests.get(ull).text
            # html4 = etree.HTML(response4)
            # # 提取信息
            # title = html4.xpath('//div[@class="scroll-wrap"]/h2/text()')
            # # 尺码信息
            # chima = html4.xpath('//div[@class="total-size"]//li/a/text()')
            # # 商品信息
            # shangpin = html4.xpath('//div[@class="pro-desc-content"]/text()')
            # # 图片网址
            # pictures = html4.xpath('//div[@class="pic-list-wrap"]//img/@src')
            #
            # picture_data = {
            #     'title': title,
            #     'chima': chima,
            #     'shangpin': shangpin,
            #     'pictures': pictures
            # }
            #
            # print(picture_data)