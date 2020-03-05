"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: gdggzyRule.py
    @time: 2019/11/15 17:01
    @desc:
"""
import re


# 广州
def ruleDetailGuangZhou(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人 广州的没有 招标人
    zhaobiaoRen = response.xpath("//td[text()='招标人：']/following-sibling::td[1]/span/text()").get(default='')
    # 招标方式 广州的没有 招标方式
    zhaobiaoFangShi = response.xpath("//td[text()='招标方式：']/following-sibling::td[1]/span/text()").get(default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 深圳
def ruleDetailShenZhen(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath("//td[text()='招标人：']/following-sibling::td[1]/span/text()").get(default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath("//td[text()='招标方式：']/following-sibling::td[1]/span/text()").get(default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 佛山
def ruleDetailFoShan(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath("//td[text()='招标人：']/following-sibling::td[1]/span/text()").get(default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath("//td[text()='招标方式：']/following-sibling::td[1]/span/text()").get(default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 东莞
def ruleDetailDongGuan(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = re.search('<br>( 招标单位：.*?  )<br>', response.text).group(1) if re.search('<br>( 招标单位：.*?  )<br>',
                                                                                          response.text) else ''
    # 招标方式
    zhaobiaoFangShi = re.search('<br>( 招标方式: .*?  )<br>', response.text).group(1) if re.search('<br>( 招标方式: .*?  )<br>',
                                                                                               response.text) else ''

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 汕头
def ruleDetailShanTou(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath('//div[contains(text(),"招标人：")]/../following-sibling::td/div/text()').get(default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath("//td[text()='招标方式：']/following-sibling::td[1]/span/text()").get(default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 惠州
def ruleDetailHuiZhou(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath('//span[contains(text(),"人：")]/text()').get(default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath("//td[text()='招标方式：']/following-sibling::td[1]/span/text()").get(default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 清远
def ruleDetailQingYuan(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = re.search('>招标人：<u>(.*?)<', response.text).group(1) if re.search('>招标人：<u>(.*?)<',
                                                                                   response.text) else ''
    zhaobiaoFangShi = re.search('招标方式:(.*?)&nbsp;', response.text).group(1) if re.search('招标方式:(.*?)&nbsp;',
                                                                                         response.text) else ''

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 珠海
def ruleDetailZhuHai(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath('//span[contains(text(),"人：")]/text()').get(default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath("//td[text()='招标方式：']/following-sibling::td[1]/span/text()").get(default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 茂名
def ruleDetailMaoMing(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath("//td[text()='招标单位']/following-sibling::td[1]/text()").get(default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath("//td[text()='招标方式']/following-sibling::td[1]/text()").get(default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 中山
def ruleDetailZhongShan(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath("//th[contains(text(),'建设单位')]/following-sibling::td[1]/text()").get(default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath("//td[text()='招标方式']/following-sibling::td[1]/text()").get(default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 潮州
def ruleDetailChaoZhou(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath("//th[contains(text(),'建设单位')]/following-sibling::td[1]/text()").get(default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath("//td[text()='招标方式']/following-sibling::td[1]/text()").get(default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 韶关
def ruleDetailShaoGuan(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath("//span[contains(text(),'招 标 人')]/../../following-sibling::td[1]/p/span/text()").get(
        default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath(
        "//span[contains(text(),'招标方式')]/../../following-sibling::td[1]/p/span/text()").get(default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 河源
def ruleDetailHeYuan(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath("//span[contains(text(),'建设单位')]/../../following-sibling::td[1]/p/span/text()").get(
        default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath(
        "//span[contains(text(),'招标方式')]/../../following-sibling::td[1]/p/span/text()").get(default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 汕尾
def ruleDetailShanWei(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath("//span[contains(text(),'建设单位')]/../../following-sibling::td[1]/p/span/text()").get(
        default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath(
        "//span[contains(text(),'招标方式')]/../../following-sibling::td[1]/p/span/text()").get(default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 江门
def ruleDetailJiangMen(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath('//td[contains(text(),"招标人：")]/span/text()').get(default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath(
        "//span[contains(text(),'招标方式')]/../../following-sibling::td[1]/p/span/text()").get(default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 阳江
def ruleDetailYangJiang(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath('//th[contains(text(),"招标人")]/following-sibling::td/text()').get(default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath(
        "//span[contains(text(),'招标方式')]/../../following-sibling::td[1]/p/span/text()").get(default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 揭阳
def ruleDetailJieYang(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath('//p[contains(text(),"招标人：")]/../following-sibling::td/p/text()').get(default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath('//p[contains(text(),"招标方式：")]/../following-sibling::td/p/text()').get(default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 梅州
def ruleDetailMeiZhou(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath('//span[contains(text(),"招标单位")]/../../following-sibling::td//text()').get(default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath('//p[contains(text(),"招标方式：")]/../following-sibling::td/p/text()').get(default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 肇庆
def ruleDetailZhaoQing(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath('//div[contains(text(),"招标人：")]/../following-sibling::td/div/text()').get(default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath('//div[contains(text(),"招标方式：")]/../following-sibling::td/div/text()').get(
        default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 湛江
def ruleDetailZhanJiang(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath('//div[contains(text(),"招标人：")]/../following-sibling::td/div/text()').get(default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath('//div[contains(text(),"招标方式：")]/../following-sibling::td/div/text()').get(
        default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items


# 云浮
def ruleDetailYunFu(response):
    # 中标投标人名称
    name = response.xpath("//th[text()='中标投标人名称']/following-sibling::td[1]/text()").get(default='')
    # 中标金额
    amountMoney = response.xpath("//th[text()='中标金额']/following-sibling::td[1]/text()").get(default='')
    # 公告发布时间
    time = response.xpath("//th[text()='公告发布时间']/following-sibling::td[1]/text()").get(default='')
    # 公告发布媒体
    meiti = response.xpath("//th[text()='公告发布媒体']/following-sibling::td[1]/text()").get(default='')
    # 招标项目名称 标题
    xiangmuName = response.xpath("//th[text()='公告标题']/following-sibling::td[1]/text()").get(default='')
    # 招标人
    zhaobiaoRen = response.xpath('//span[contains(text(),"招标人：")]/following-sibling::span//text()').get(default='')
    # 招标方式
    zhaobiaoFangShi = response.xpath('//div[contains(text(),"招标方式：")]/../following-sibling::td/div/text()').get(
        default='')

    items = {
        'name': name,
        'amountMoney': amountMoney,
        'time': time,
        'meiti': meiti,
        'xiangmuName': xiangmuName,
        'zhaobiaoRen': zhaobiaoRen,
        'zhaobiaoFangShi': zhaobiaoFangShi,
        'city': response.meta['city'],
        'detailUrl': response.url
    }

    return items
