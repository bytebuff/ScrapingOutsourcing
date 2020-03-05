"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: anjukeDetail.py
    @time: 2019/11/16 14:54
    @desc: 获取数据 也就是访问详情页 然后获取数据
"""
import re, csv, time, os
from selenium import webdriver
from parsel import Selector
from selenium.webdriver.firefox.options import Options


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

    # 数据提取
    # 单价 以及单位
    jiage = selectors.xpath('//span[@class="house_basic_title_money_num"]/text()').get(default='')
    jiagedanwei = selectors.xpath('//span[@class="house_basic_title_money_unit"]/text()').get(default='')
    # 价格和单位拼接
    jiadan = jiage + jiagedanwei
    # 租价和单位
    zujia = selectors.xpath('//span[@class="house_basic_title_money_num_chuzu"]/text()').get(default='').strip()
    zujiadanwei = selectors.xpath('//span[@class="house_basic_title_money_unit_chuzu"]/text()').get(default='').strip()
    # 拼接租价和单位
    zudan = zujia + zujiadanwei
    # 面积
    mianji = selectors.xpath('//p[@class="house_basic_title_info"]/span[1]/text()').get(default='').strip()
    # 类型
    leixing = selectors.xpath('//p[@class="house_basic_title_info"]/span[2]/text()').get(default='').strip()
    # 起租
    qizu = selectors.xpath('//p[@class="house_basic_title_info"]/span[3]/text()').get(default='').strip()
    # 区域
    quyu = selectors.xpath('//span[contains(text(),"域：")]/../text()').getall()
    quyu = ''.join(quyu).strip()
    # 地址
    dizhi = selectors.xpath('//div[@class="house_basic_title_info_2"]//span[@class="address"]/text()').get(
        default='').strip()

    # 概况
    yuezu = selectors.xpath('//span[contains(text(),"月租")]/following-sibling::span/text()').get(default='').strip()
    yafu = selectors.xpath('//span[contains(text(),"押付")]/following-sibling::span/text()').get(default='').strip()
    qizuqi = selectors.xpath('//span[contains(text(),"起租期")]/following-sibling::span/text()').get(default='').strip()
    jianzhumianji = selectors.xpath('//span[contains(text(),"建筑面积")]/following-sibling::span/text()').get(
        default='').strip()
    shangpuxingzhi = selectors.xpath('//span[contains(text(),"商铺性质")]/following-sibling::span/text()').get(
        default='').strip()
    shangpuleixing = selectors.xpath('//span[contains(text(),"商铺类型")]/following-sibling::span/text()').get(
        default='').strip()
    jingyingzhuangtai = selectors.xpath('//span[contains(text(),"经营状态")]/following-sibling::span/text()').get(
        default='').strip()
    jingyingleixing = selectors.xpath('//span[contains(text(),"经营类型")]/following-sibling::span/text()').get(
        default='').strip()
    louceng = selectors.xpath('//span[contains(text(),"楼层")]/following-sibling::span/text()').get(default='').strip()
    guige = selectors.xpath('//span[contains(text(),"规格")]/following-sibling::span/text()').get(default='').strip()
    keliurenqun = selectors.xpath('//span[contains(text(),"客流人群")]/following-sibling::span/text()').get(
        default='').strip()
    xiangguanfeiyong = selectors.xpath('//span[contains(text(),"相关费用")]/following-sibling::span/text()').get(
        default='').strip()

    # 配套设施 列表 x注意选择页面字体比较深的 代表有这个设施
    peitaosheshi = selectors.xpath('//ul[@class="peitao-icon"]/li[@class="peitao-on"]/text()').getall()

    jiaoTong = []
    # 地铁 购物等数据 //ul[@id="mapResultBox"]/li/span/text()
    if 'mapItemBar' in response:
        # 定位滑动到到地图的地方
        elementMap = driver.find_element_by_xpath('//*[@id="mapWrap"]/h3')
        driver.execute_script('arguments[0].scrollIntoView()', elementMap)
        # time.sleep(1.5)
        # 重新载入滑动后的数据
        pageSource = driver.page_source
        selectors = Selector(text=pageSource)
        selectors = selectors.xpath('//ul[@id="mapResultBox"]/li')

        # 交通
        for selector in selectors[0:1]:
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

    # 整理数据
    items = [
        jiadan,
        zudan,
        mianji,
        leixing,
        qizu,
        quyu,
        dizhi,
        yuezu,
        yafu,
        qizuqi,
        jianzhumianji,
        shangpuxingzhi,
        shangpuleixing,
        jingyingzhuangtai,
        jingyingleixing,
        louceng,
        guige,
        keliurenqun,
        xiangguanfeiyong,
        peitaosheshi,
        jiaoTong  # 交通
    ]

    print(items)
    saveDetailView(items)


def saveDetailView(item):
    with open(f'{saveFileName}.csv', 'a', encoding='utf-8', newline='') as fp:
        csvWriter = csv.writer(fp)
        csvWriter.writerow(item)


if __name__ == '__main__':
    # 无头浏览器
    firefox_options = Options()
    # firefox_options.add_argument('--headless')
    # 禁用图片
    firefox_profile = webdriver.FirefoxProfile()
    # firefox_profile.set_preference('permissions.default.image', 2)  # 某些firefox只需要这个
    # 禁用浏览器缓存
    firefox_profile.set_preference("network.http.use-cache", False)
    firefox_profile.set_preference("browser.cache.memory.enable", False)
    firefox_profile.set_preference("browser.cache.disk.enable", False)
    firefox_profile.set_preference("browser.sessionhistory.max_total_viewers", 3)
    firefox_profile.set_preference("network.dns.disableIPv6", True)
    firefox_profile.set_preference("Content.notify.interval", 750000)
    firefox_profile.set_preference("content.notify.backoffcount", 3)
    # 有的网站支持 有的不支持
    firefox_profile.set_preference("network.http.pipelining", True)
    firefox_profile.set_preference("network.http.proxy.pipelining", True)
    firefox_profile.set_preference("network.http.pipelining.maxrequests", 32)

    # driver = webdriver.Firefox(firefox_profile=firefox_profile, options=firefox_options)
    driver = webdriver.Chrome()

    fileNames = [f for f in os.listdir() if '网址' in f]
    for fileName in fileNames:
        saveFileName = '结果详情-' + fileName.split('.')[0]
        # 准备网址
        urls = getFileUrls(fileName)
        # 初始化浏览器
        for url in urls:
            print('当前的网址是>>>  ', url)
            getDetailView(url)
    # tui出
    driver.quit()
