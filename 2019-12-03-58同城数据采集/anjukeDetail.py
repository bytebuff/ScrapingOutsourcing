"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: anjukeDetail.py
    @time: 2019/11/16 14:54
    @desc: 获取数据 也就是访问详情页 然后获取数据
"""
import re, csv, time
from selenium import webdriver
from parsel import Selector


def getFileUrls(filePath):
    '''
    从文件中中获取网址 这个函数使用rabbitmq可能会更合适
    :return:
    '''
    urls = []
    with open(filePath, 'r', encoding='utf-8') as fp:
        for url in fp:
            urls.append(url.strip())
    return urls  # 返回网址列表


def getDetailView(url):
    driver.get(url)
    # 需要向下滑动一下 滑动到地址的位置
    pageSource = driver.page_source
    # 判断是否出现了验证吗 入股哦出现 了 就先暂停程序 等待认为点击 验证(安居客规定需要在五分钟只能验证号)
    if '验证码' in pageSource:
        print('你需要验证验证码，然后输入 ok 继续')
        word = input('请输入ok：')
        if word == 'ok':
            getDetailView(url)
            # 解析数据
    else:
        # 直接解析数据
        parseDetailView(pageSource)


def parseDetailView(response):
    selectors = Selector(text=response)
    # 变量的命名是最后两个字的全拼
    zongJia = selectors.xpath("//span[text()='总价']/following-sibling::span/text()").get()
    mianJi = selectors.xpath("//span[text()='建筑面积']/following-sibling::span/text()").get()
    danJia = selectors.xpath("//span[text()='单价']/following-sibling::span/text()").get()
    xingZhi = selectors.xpath("//span[text()='商铺性质']/following-sibling::span/text()").get()
    leiXing = selectors.xpath("//span[text()='商铺类型']/following-sibling::span/text()").get()
    louCeng = selectors.xpath("//span[text()='楼层']/following-sibling::span/text()").get()
    zhuangTai = selectors.xpath("//span[text()='经营状态']/following-sibling::span/text()").get()
    guiGe = selectors.xpath("//span[text()='规格']/following-sibling::span/text()").get()
    jyLeiXing = selectors.xpath("//span[text()='经营类型']/following-sibling::span/text()").get()
    wuYe = selectors.xpath("//span[text()='物业']/following-sibling::span/text()").get()
    renQun = selectors.xpath("//span[text()='客流人群']/following-sibling::span/text()").get()
    diZhi = selectors.xpath("//span[text()='地址']/following-sibling::span/text()").get()



    # 配套设施 列表
    peiTaoSheShi = selectors.xpath('//div[@class="supports-wrapper"]//ul/li[@class!="gray"]/p/text()').getall()

    jiaoTong = []
    gouWu = []

    # 地铁 购物等数据 //ul[@id="mapResultBox"]/li/span/text()
    if 'mapItemBar' in response:
        # 定位滑动到到地图的地方
        elementMap = driver.find_element_by_xpath('//*[@id="map"]/h3')
        driver.execute_script('arguments[0].scrollIntoView()', elementMap)
        time.sleep(5)
        # 重新载入滑动后的数据
        pageSource = driver.page_source
        selectors = Selector(text=pageSource)
        selectors = selectors.xpath('//ul[@id="mapResultBox"]/li')
        # 交通
        for selector in selectors[0:2]:
            # 交通
            diTie = selector.xpath('./span/text()').get()
            # 下面这两个是一起的
            letter = selector.xpath('./div[@class="pst"]/span[@class="letter"]/text()').get()
            ellip = selector.xpath('./div[@class="pst"]/span[@class="title txt-ellip"]/text()').get()
            dis = selector.xpath('./div[@class="pst"]/span[@class="dis"]/text()').get()

            jT = [
                diTie,
                letter,
                ellip,
                dis,
            ]

            jiaoTong.append(jT)

        # 购物
        # 购物似乎需要 点击 才可以出现数据
        pageSource = clickGouWu(driver)
        # 选择出购物数据 和 交通一样
        selectors = Selector(text=pageSource)
        selectors = selectors.xpath('//ul[@id="mapResultBox"]/li')
        # 购物
        for selector in selectors[0:2]:
            # 交通
            diTie = selector.xpath('./span/text()').get()
            # 下面这两个是一起的
            letter = selector.xpath('./div[@class="pst"]/span[@class="letter"]/text()').get()
            ellip = selector.xpath('./div[@class="pst"]/span[@class="title txt-ellip"]/text()').get()
            dis = selector.xpath('./div[@class="pst"]/span[@class="dis"]/text()').get()

            gW = [
                diTie,
                letter,
                ellip,
                dis,
            ]

            gouWu.append(gW)


    # 整理数据
    items = [
        zongJia,
        mianJi,
        danJia,
        xingZhi,
        leiXing,
        louCeng,
        zhuangTai,
        guiGe,
        jyLeiXing,
        wuYe,
        renQun,
        diZhi,

        peiTaoSheShi,

        jiaoTong,  # 交通数据

        gouWu # 购物

    ]

    print(items)
    saveDetailView(items)


def clickGouWu(driver):
    '''
    点击购物
    :param driver:
    :return:
    '''
    try:
        driver.find_element_by_xpath('//*[@id="mapItemBar"]/li[2]').click()
        time.sleep(2)
    except:
        print('购物不能点击>>>', driver.current_url)
    pageSource = driver.page_source

    return pageSource


def saveDetailView(item):
    with open('测试数据.csv', 'a', encoding='utf-8', newline='') as fp:
        csvWriter = csv.writer(fp)
        csvWriter.writerow(item)


if __name__ == '__main__':

    fileName = '静安网址'

    # 准备网址
    urls = getFileUrls(f'{fileName}.txt')
    # 初始化浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()

    for url in urls:
        print('当前的网址是>>>  ', url)
        getDetailView(url)

    # tui出
    driver.close()
