"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: cqggzyRule.py
    @time: 2019/11/28 19:12
    @desc:
"""
from scrapy.selector import Selector


def ruleDetail(response):
    # 标题
    biaoTi = response.xpath('//h3/text()').get(default='')
    # 建设单位名称
    jianSheDanWei = response.xpath('//span[contains(text(),"单位名称")]/../../following-sibling::td//span/text()').get(default='')
    if not jianSheDanWei:
        jianSheDanWei = response.xpath('//span[contains(text(),"招标人")]/../../following-sibling::td//span/text()').get(default='')
    if not jianSheDanWei:
        jianSheDanWei = response.xpath('//span[contains(text(),"人")]/../../following-sibling::td//span/text()').get(default='')

    # 中标人名称
    zhongBiaoDanWei = response.xpath('//span[contains(text(),"第一中标候选人")]/../../following-sibling::td//span/text()').get(default='')
    if not zhongBiaoDanWei:
        zhongBiaoDanWei = response.xpath('//span[contains(text(),"中标人")]/../../following-sibling::td//span/text()').get(default='')
    # 中 标 价
    zhongBiaoJia = response.xpath('//span[contains(text(),"中标金额")]/../../following-sibling::td//span/text()').get(default='')
    if not zhongBiaoJia:
        zhongBiaoJia = response.xpath('//span[contains(text(),"中标价")]/../../following-sibling::td//span/text()').get(default='')
    # 公告开始时间
    zhongBiaoShiJian = response.xpath('//div[@class="info-source"]/text()').get(default='')
    if not zhongBiaoShiJian:
        zhongBiaoShiJian = response.xpath('//div[@class="info-source"]/text()').get(default='')

    items = {
        'biaoTi': biaoTi,
        'jianSheDanWei': jianSheDanWei,
        'zhongBiaoDanWei': zhongBiaoDanWei,
        'zhongBiaoJia': zhongBiaoJia,
        'zhongBiaoShiJian': zhongBiaoShiJian,
    }

    yield items

