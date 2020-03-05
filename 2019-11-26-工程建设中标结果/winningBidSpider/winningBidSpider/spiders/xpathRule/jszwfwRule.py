"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: jszwfwRule.py
    @time: 2019/11/27 14:27
    @desc:
"""
import re
from parsel import Selector


# 南京市
def ruleDetailNanJingShi(response, fieldvalue):
    selectors = Selector(text=response.text)
    # 标题
    biaoTi = selectors.xpath('//h2/text()').get(default='')
    # 建设单位名称
    jianSheDanWei = selectors.xpath('//td[contains(text(),"建设单位名称:")]/following-sibling::td/text()').get(default='')
    # 中标人名称
    zhongBiaoDanWei = selectors.xpath('//p[contains(text(),"中标人名称")]//span/text()').get(default='')
    # 中 标 价
    zhongBiaoJia = selectors.xpath('//p[contains(text(),"中 标 价")]//span/text()').get(default='')
    # 公告开始时间
    zhongBiaoShiJian = selectors.xpath('//p[contains(text(),"中标公告开始时间")]//span/text()').get(default='')
    # 来源
    laiYuan = re.findall('源：(.*?)统<span>', response.text)
    if laiYuan:
        pass
    else:
        laiYuan = ''

    items = {
        'biaoTi': biaoTi,
        'jianSheDanWei': jianSheDanWei,
        'zhongBiaoDanWei': zhongBiaoDanWei,
        'zhongBiaoJia': zhongBiaoJia,
        'zhongBiaoShiJian': zhongBiaoShiJian,
        'laiYuan': laiYuan,
        'fieldvalue': fieldvalue,
    }

    yield items  # 南京市


# 无锡市
def ruleDetailWuXi(response, fieldvalue):
    selectors = Selector(text=response.text)
    # 标题
    biaoTi = selectors.xpath('//h2/text()').get(default='')
    # 建设单位名称
    jianSheDanWei = selectors.xpath('//td[contains(text(),"建设单位名称:")]/following-sibling::td/text()').get(default='')
    # 中标单位名称
    zhongBiaoDanWei = selectors.xpath('//td[contains(text(),"中标单位名称")]/following-sibling::td/text()').get(default='')
    # 中标价(万元)
    zhongBiaoJia = selectors.xpath('//td[contains(text(),"中标价(万元):")]/following-sibling::td/text()').get(default='')
    # 中标时间
    zhongBiaoShiJian = selectors.xpath('//td[contains(text(),"中标时间:")]/following-sibling::td/text()').get(default='')
    # 来源
    laiYuan = re.findall('源：(.*?)统<span>', response.text)
    if laiYuan:
        laiYuan = laiYuan[0]
    else:
        laiYuan = ''

    items = {
        'biaoTi': biaoTi,
        'jianSheDanWei': jianSheDanWei,
        'zhongBiaoDanWei': zhongBiaoDanWei,
        'zhongBiaoJia': zhongBiaoJia,
        'zhongBiaoShiJian': zhongBiaoShiJian,
        'laiYuan': laiYuan,
        'fieldvalue': fieldvalue,
    }

    yield items


# 徐州市
def ruleDetailXuZhouShi(response, fieldvalue):
    selectors = Selector(text=response.text)
    # 标题
    biaoTi = selectors.xpath('//h2/text()').get(default='')
    # 建设单位名称
    jianSheDanWei = selectors.xpath('//td[contains(text(),"建设单位名称：")]/following-sibling::td//span/span/text()').get(default='')
    # 中标单位名称
    zhongBiaoDanWei = selectors.xpath('//td[contains(text(),"中标单位名称：")]/following-sibling::td//span/text()').get(default='')
    # 中标价(万元)
    zhongBiaoJia = selectors.xpath('//td[contains(text(),"中标价 (万元)：")]/following-sibling::td//span/span/text()').get(default='')
    # 中标时间
    zhongBiaoShiJian = selectors.xpath('//td[contains(text(),"中标时间：")]/following-sibling::td//span/span/text()').get(default='')
    # 来源
    laiYuan = re.findall('源：(.*?)统<span>', response.text)
    if laiYuan:
        laiYuan = laiYuan[0]
    else:
        laiYuan = ''

    items = {
        'biaoTi': biaoTi,
        'jianSheDanWei': jianSheDanWei,
        'zhongBiaoDanWei': zhongBiaoDanWei,
        'zhongBiaoJia': zhongBiaoJia,
        'zhongBiaoShiJian': zhongBiaoShiJian,
        'laiYuan': laiYuan,
        'fieldvalue': fieldvalue,
    }

    yield items


# 常州市
def ruleDetailChangZhouShi(response, fieldvalue):
    selectors = Selector(text=response.text)
    # 标题
    biaoTi = selectors.xpath('//h2/text()').get(default='')

    # 建设单位名称
    jianSheDanWei = selectors.xpath('//td[contains(text(),"建设单位")]/following-sibling::td/text()').get(default='')
    # 中标单位名称
    zhongBiaoDanWei = selectors.xpath('//td[contains(text(),"中标单位")]/following-sibling::td//text()').get(default='')
    # 中标价(万元)
    zhongBiaoJia = selectors.xpath('//td[contains(text(),"中标价")]/following-sibling::td//text()').get(default='')
    # 中标时间
    zhongBiaoShiJian = selectors.xpath('//td[contains(text(),"开标日期")]/following-sibling::td//text()').get(default='')

    # 来源
    laiYuan = re.findall('源：(.*?)统<span>', response.text)
    if laiYuan:
        laiYuan = laiYuan[0]
    else:
        laiYuan = ''

    items = {
        'biaoTi': biaoTi,
        'jianSheDanWei': jianSheDanWei,
        'zhongBiaoDanWei': zhongBiaoDanWei,
        'zhongBiaoJia': zhongBiaoJia,
        'zhongBiaoShiJian': zhongBiaoShiJian,
        'laiYuan': laiYuan,
        'fieldvalue': fieldvalue,
    }

    yield items


# 苏州市
def ruleDetailSuZhouShi(response, fieldvalue):
    selectors = Selector(text=response.text)
    # 标题
    biaoTi = selectors.xpath('//h2/text()').get(default='')

    # 建设单位名称
    jianSheDanWei = selectors.xpath('//td[contains(text(),"建设单位名称")]/following-sibling::td//span/span/text()').get(default='')
    # 中标单位名称
    zhongBiaoDanWei = selectors.xpath('//td[contains(text(),"中标单位名称")]/following-sibling::td//span/text()').get(default='')
    # 中标价(万元)
    zhongBiaoJia = selectors.xpath('//td[contains(text(),"中标价 (元)：")]/following-sibling::td//span/text()').get(default='')
    # 中标时间
    zhongBiaoShiJian = selectors.xpath('//td[contains(text(),"中标时间：")]/following-sibling::td//span/text()').get(default='')

    # 来源
    laiYuan = re.findall('源：(.*?)统<span>', response.text)
    if laiYuan:
        laiYuan = laiYuan[0]
    else:
        laiYuan = ''

    items = {
        'biaoTi': biaoTi,
        'jianSheDanWei': jianSheDanWei,
        'zhongBiaoDanWei': zhongBiaoDanWei,
        'zhongBiaoJia': zhongBiaoJia,
        'zhongBiaoShiJian': zhongBiaoShiJian,
        'laiYuan': laiYuan,
        'fieldvalue': fieldvalue,
    }

    yield items


# 南通市
def ruleDetailNanTongShi(response, fieldvalue):
    selectors = Selector(text=response.text)
    # 标题
    biaoTi = selectors.xpath('//h2/text()').get(default='')

    # 建设单位名称
    jianSheDanWei = selectors.xpath('//td[contains(text(),"招标人名称")]/following-sibling::td//span/text()').get(default='')
    # 中标单位名称
    zhongBiaoDanWei = selectors.xpath('//div[contains(text(),"中标单位名称")]/../following-sibling::td//span/text()').get(default='')
    # 中标价(万元)
    zhongBiaoJia = selectors.xpath('//div[contains(text(),"中标价")]/../following-sibling::td//span/text()').get(default='')
    # 中标时间
    zhongBiaoShiJian = selectors.xpath('//td[contains(text(),"中标时间：")]/following-sibling::td//span/text()').get(default='')

    # 来源
    laiYuan = re.findall('源：(.*?)统<span>', response.text)
    if laiYuan:
        laiYuan = laiYuan[0]
    else:
        laiYuan = ''

    items = {
        'biaoTi': biaoTi,
        'jianSheDanWei': jianSheDanWei,
        'zhongBiaoDanWei': zhongBiaoDanWei,
        'zhongBiaoJia': zhongBiaoJia,
        'zhongBiaoShiJian': zhongBiaoShiJian,
        'laiYuan': laiYuan,
        'fieldvalue': fieldvalue,
    }

    yield items


# 连云港市
def ruleDetailLianYunGangShi(response, fieldvalue):
    selectors = Selector(text=response.text)
    # 标题
    biaoTi = selectors.xpath('//h2/text()').get(default='')

    # 建设单位名称
    jianSheDanWei = selectors.xpath('//td[contains(text(),"建设单位名称")]/following-sibling::td//text()').get(default='')
    # 中标单位名称
    zhongBiaoDanWei = selectors.xpath('//td[contains(text(),"中标单位名称")]/following-sibling::td//text()').get(default='')
    # 中标价(万元)
    zhongBiaoJia = selectors.xpath('//td[contains(text(),"中标价")]/following-sibling::td//text()').get(default='')
    # 中标时间
    zhongBiaoShiJian = selectors.xpath('//td[contains(text(),"中标时间")]/following-sibling::td//text()').get(default='')

    # 来源
    laiYuan = re.findall('源：(.*?)统<span>', response.text)
    if laiYuan:
        laiYuan = laiYuan[0]
    else:
        laiYuan = ''

    items = {
        'biaoTi': biaoTi,
        'jianSheDanWei': jianSheDanWei,
        'zhongBiaoDanWei': zhongBiaoDanWei,
        'zhongBiaoJia': zhongBiaoJia,
        'zhongBiaoShiJian': zhongBiaoShiJian,
        'laiYuan': laiYuan,
        'fieldvalue': fieldvalue,
    }

    yield items


# 淮安市
def ruleDetailHuaiAnShi(response, fieldvalue):
    selectors = Selector(text=response.text)
    # 标题
    biaoTi = selectors.xpath('//h2/text()').get(default='')

    # 建设单位名称
    jianSheDanWei = selectors.xpath('//td[contains(text(),"建设单位名称")]/following-sibling::td//text()').get(default='')
    # 中标单位名称
    zhongBiaoDanWei = selectors.xpath('//td[contains(text(),"中标单位名称")]/following-sibling::td//text()').get(default='')
    # 中标价(万元)
    zhongBiaoJia = selectors.xpath('//td[contains(text(),"中标价")]/following-sibling::td//text()').get(default='')
    # 中标时间
    zhongBiaoShiJian = selectors.xpath('//td[contains(text(),"中标时间")]/following-sibling::td//text()').get(default='')

    # 来源
    laiYuan = re.findall('源：(.*?)统<span>', response.text)
    if laiYuan:
        laiYuan = laiYuan[0]
    else:
        laiYuan = ''

    items = {
        'biaoTi': biaoTi,
        'jianSheDanWei': jianSheDanWei,
        'zhongBiaoDanWei': zhongBiaoDanWei,
        'zhongBiaoJia': zhongBiaoJia,
        'zhongBiaoShiJian': zhongBiaoShiJian,
        'laiYuan': laiYuan,
        'fieldvalue': fieldvalue,
    }

    yield items


# 盐城市
def ruleDetailYanChengShi(response, fieldvalue):
    selectors = Selector(text=response.text)
    # 标题
    biaoTi = selectors.xpath('//h2/text()').get(default='')

    # 建设单位名称
    jianSheDanWei = selectors.xpath('//td[contains(text(),"建设单位名称")]/following-sibling::td//text()').get(default='')
    # 中标单位名称
    zhongBiaoDanWei = selectors.xpath('//td[contains(text(),"中标单位名称")]/following-sibling::td//text()').get(default='')
    # 中标价(万元)
    zhongBiaoJia = selectors.xpath('//td[contains(text(),"中标价")]/following-sibling::td//text()').get(default='')
    # 中标时间
    zhongBiaoShiJian = selectors.xpath('//td[contains(text(),"中标时间")]/following-sibling::td//text()').get(default='')

    # 来源
    laiYuan = re.findall('源：(.*?)统<span>', response.text)
    if laiYuan:
        laiYuan = laiYuan[0]
    else:
        laiYuan = ''

    items = {
        'biaoTi': biaoTi,
        'jianSheDanWei': jianSheDanWei,
        'zhongBiaoDanWei': zhongBiaoDanWei,
        'zhongBiaoJia': zhongBiaoJia,
        'zhongBiaoShiJian': zhongBiaoShiJian,
        'laiYuan': laiYuan,
        'fieldvalue': fieldvalue,
    }

    yield items


# 扬州市
def ruleDetailYangZhouShi(response, fieldvalue):
    selectors = Selector(text=response.text)
    # 标题
    biaoTi = selectors.xpath('//h2/text()').get(default='')

    # 建设单位名称
    jianSheDanWei = selectors.xpath('//td[contains(text(),"建设单位")]/following-sibling::td//text()').get(default='')
    # 中标单位名称
    zhongBiaoDanWei = selectors.xpath('//td[contains(text(),"中标单位")]/following-sibling::td//text()').get(default='')
    # 中标价(万元)
    zhongBiaoJia = selectors.xpath('//td[contains(text(),"中标价")]/following-sibling::td//text()').get(default='')
    # 中标时间
    zhongBiaoShiJian = selectors.xpath('//td[contains(text(),"开标日期")]/following-sibling::td//text()').get(default='')

    # 来源
    laiYuan = re.findall('源：(.*?)统<span>', response.text)
    if laiYuan:
        laiYuan = laiYuan[0]
    else:
        laiYuan = ''

    items = {
        'biaoTi': biaoTi,
        'jianSheDanWei': jianSheDanWei,
        'zhongBiaoDanWei': zhongBiaoDanWei,
        'zhongBiaoJia': zhongBiaoJia,
        'zhongBiaoShiJian': zhongBiaoShiJian,
        'laiYuan': laiYuan,
        'fieldvalue': fieldvalue,
    }

    yield items


# 泰州市
def ruleDetailTaiZhouShi(response, fieldvalue):
    selectors = Selector(text=response.text)
    # 标题
    biaoTi = selectors.xpath('//h2/text()').get(default='')

    # 建设单位名称
    jianSheDanWei = selectors.xpath('//td[contains(text(),"建设单位")]/following-sibling::td//text()').get(default='')
    # 中标单位名称
    zhongBiaoDanWei = selectors.xpath('//td[contains(text(),"中标单位")]/following-sibling::td//text()').get(default='')
    # 中标价(万元)
    zhongBiaoJia = selectors.xpath('//td[contains(text(),"中标价")]/following-sibling::td//text()').get(default='')
    # 中标时间
    zhongBiaoShiJian = selectors.xpath('//td[contains(text(),"开标日期")]/following-sibling::td//text()').get(default='')

    # 来源
    laiYuan = re.findall('源：(.*?)统<span>', response.text)
    if laiYuan:
        laiYuan = laiYuan[0]
    else:
        laiYuan = ''

    items = {
        'biaoTi': biaoTi,
        'jianSheDanWei': jianSheDanWei,
        'zhongBiaoDanWei': zhongBiaoDanWei,
        'zhongBiaoJia': zhongBiaoJia,
        'zhongBiaoShiJian': zhongBiaoShiJian,
        'laiYuan': laiYuan,
        'fieldvalue': fieldvalue,
    }

    yield items


# 宿迁市
def ruleDetailSuQianShi(response, fieldvalue):
    selectors = Selector(text=response.text)
    # 标题
    biaoTi = selectors.xpath('//h2/text()').get(default='')

    # 建设单位名称
    jianSheDanWei = selectors.xpath('//td[contains(text(),"建设单位")]/following-sibling::td//text()').get(default='')
    # 中标单位名称
    zhongBiaoDanWei = selectors.xpath('//td[contains(text(),"中标单位")]/following-sibling::td//text()').get(default='')
    # 中标价(万元)
    zhongBiaoJia = selectors.xpath('//td[contains(text(),"中标价")]/following-sibling::td//text()').get(default='')
    # 中标时间
    zhongBiaoShiJian = selectors.xpath('//td[contains(text(),"开标日期")]/following-sibling::td//text()').get(default='')

    # 来源
    laiYuan = re.findall('源：(.*?)统<span>', response.text)
    if laiYuan:
        laiYuan = laiYuan[0]
    else:
        laiYuan = ''

    items = {
        'biaoTi': biaoTi,
        'jianSheDanWei': jianSheDanWei,
        'zhongBiaoDanWei': zhongBiaoDanWei,
        'zhongBiaoJia': zhongBiaoJia,
        'zhongBiaoShiJian': zhongBiaoShiJian,
        'laiYuan': laiYuan,
        'fieldvalue': fieldvalue,
    }

    yield items


