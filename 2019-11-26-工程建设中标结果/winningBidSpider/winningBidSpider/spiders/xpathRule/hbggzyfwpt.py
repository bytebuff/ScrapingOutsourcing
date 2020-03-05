"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: hbggzyfwpt.py
    @time: 2019/11/18 11:51
    @desc:
"""
from parsel import Selector


# 武汉市
def ruleDetailWuHanShi(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        zhaoBiaoRen = selectors.xpath("//td[text()='建设单位(招标人)']/following-sibling::td[1]/text()").get(default='')
        # xiangMuMingCheng = selectors.xpath("//td[text()='报建项目名称']/following-sibling::td[1]/text()").get(default='')
        diZHi = selectors.xpath("//td[text()='建设地址']/following-sibling::td[1]/text()").get(default='')
        zhongBiaoRen = selectors.xpath("//td[text()='中标人']/following-sibling::td[1]/text()").get(default='')
        zhongBiaoJia = selectors.xpath("//td[text()='中标价（万元）']/following-sibling::td[1]/text()").get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia,
            'detailUrl': detailUrl,
            'city': '武汉市'
        }

        yield items


# 省级 湖北省级
def ruleDetailShengJi(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据 转成html
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        # 招标人
        zhaoBiaoRen = selectors.xpath("//td[contains(text(),'招标人：')]/text()").get(default='')
        # 地址 根据招标人定位地址 也可以根据地址文字定位
        diZHi = selectors.xpath("//td[contains(text(),'招标人：')]/../following-sibling::tr[1]/td/text()").get(default='')
        # diZHi = selectors.xpath("//td[contains(text(),'地址：')]/text()").getall()[0]
        # 中标人
        zhongBiaoRen = selectors.xpath("//td[text()='中标人']/../following-sibling::tr/td[1]/text()").get(default='')
        # 中标价
        zhongBiaoJia = selectors.xpath("//td[text()='中标价(元)']/../following-sibling::tr/td[2]/text()").get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia + '元',
            'detailUrl': detailUrl,
            'city': '省级'

        }

        return items


# 黄石市
def ruleDetailHuangShiShi(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据 转成html
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        # 招标人
        zhaoBiaoRen = selectors.xpath("//span[contains(text(),'招 标 人：')]/text()").get(default='')
        # 地址 根据招标人定位地址 也可以根据地址文字定位
        diZHi = selectors.xpath("//span[contains(text(),'招 标 人：')]/../../following-sibling::p[1]//span/text()").get(default='')
        # diZHi = selectors.xpath("//td[contains(text(),'地址：')]/text()").getall()[0]
        # 中标人
        zhongBiaoRen = selectors.xpath("//span[text()='中标人']/../../../following-sibling::tr/td[1]//span/text()").get(default='')
        # 中标价
        zhongBiaoJia = selectors.xpath(
            "//span[text()='中标价（万元）']/../../../following-sibling::tr/td[2]//span/text()").get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia + '万元',
            'detailUrl': detailUrl,
            'city': '黄石市'
        }

        return items


#  十堰市
def ruleDetailShiYanShi(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据 转成html
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        # 招标人
        zhaoBiaoRen = selectors.xpath("//td[contains(text(),'招标人：')]/text()").get(default='')
        # 地址 根据招标人定位地址 也可以根据地址文字定位
        diZHi = selectors.xpath("//td[contains(text(),'招标人：')]/../following-sibling::tr[1]/td/text()").get(default='')
        # diZHi = selectors.xpath("//td[contains(text(),'地址：')]/text()").getall()[0]
        # 中标人
        zhongBiaoRen = selectors.xpath("//td[text()='中标人']/../following-sibling::tr/td[1]/text()").get(default='')
        # 中标价
        zhongBiaoJia = selectors.xpath("//td[text()='中标价(元)']/../following-sibling::tr/td[2]").get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia + '元',
            'detailUrl': detailUrl,
            'city': '十堰市'
        }

        return items


# 荆州市
def ruleDetailJinZhouShi(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据 转成html
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        # 招标人
        zhaoBiaoRen = selectors.xpath("//p[contains(text(),'招标人或代理机构：')]/text()").get(default='')
        # 地址 根据招标人定位地址 也可以根据地址文字定位
        diZHi = selectors.xpath("//p[contains(text(),'地 址：')]/text()").get(default='')
        # diZHi = selectors.xpath("//td[contains(text(),'地址：')]/text()").getall()[0]
        # 中标人
        zhongBiaoRen = selectors.xpath("//div[text()='中标人']/../../following-sibling::tr[1]/td[2]/div/text()").get(default='')
        # 中标价
        zhongBiaoJia = selectors.xpath("//div[text()='中标价']/../../following-sibling::tr[1]/td[3]/div/text()").get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia + '元',
            'detailUrl': detailUrl,
            'city': '荆州市'

        }

        return items


# 宜昌市
def ruleDetailYiChangShi(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        zhaoBiaoRen = selectors.xpath("//div[text()='招标人：']/../following-sibling::td[1]/div/text()").get(default='')
        diZHi = selectors.xpath("//div[text()='建设地点：']/../following-sibling::td[1]/div/text()").get(default='')
        zhongBiaoRen = selectors.xpath("//div[text()='中标人：']/../following-sibling::td[1]/div/text()").get(default='')
        zhongBiaoJia = selectors.xpath("//div[text()='中标价：']/../following-sibling::td[1]/div/text()").get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia,
            'detailUrl': detailUrl,
            'city': '宜昌市'

        }

        yield items


# 襄阳市
def ruleDetailXiangYangShi(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据 转成html
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        # 招标人
        zhaoBiaoRen = selectors.xpath("//span[contains(text(),'招标人：')]/text()").extract_first(default='')
        # 地址 根据招标人定位地址 也可以根据地址文字定位
        diZHi = ''.join(selectors.xpath("//span[contains(text(),'招标人：')]/../following-sibling::p[1]//text()").getall())
        # diZHi = selectors.xpath("//td[contains(text(),'地址：')]/text()").getall()[0]
        # 中标人
        zhongBiaoRen = selectors.xpath(
            "//span[text()='中标人']/../../../following-sibling::tr[1]/td[1]//span/text()").get(default='')
        # 中标价
        zhongBiaoJia = selectors.xpath(
            "//span[text()='中标价']/../../../following-sibling::tr[1]/td[2]//span/text()").get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia + '元',
            'detailUrl': detailUrl,
            'city': '襄阳市'

        }

        return items


# 鄂州市
def ruleDetailEZhouShi(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据 转成html
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        # 招标人
        zhaoBiaoRen = selectors.xpath("//td[text()='招标人：']/following-sibling::td/span/text()").extract_first()
        # 地址 根据招标人定位地址 也可以根据地址文字定位
        diZHi = ''.join(selectors.xpath("//span[contains(text(),'招标人：')]/../following-sibling::p[1]//text()").getall())
        # diZHi = selectors.xpath("//td[contains(text(),'地址：')]/text()").getall()[0]
        # 中标人
        zhongBiaoRen = selectors.xpath("//td[text()='中标人：']/following-sibling::td//span/text()").get(default='')
        # 中标价
        zhongBiaoJia = selectors.xpath("//td[text()='中标价：']/following-sibling::td//span/text()").get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia + '元',
            'detailUrl': detailUrl,
            'city': '鄂州市'

        }

        return items


# 荆门市
def ruleDetailJinMenShi(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据 转成html
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        # 招标人
        zhaoBiaoRen = selectors.xpath(
            "//div[text()='招标人或招标代理机构：']/../following-sibling::td[1]/div/text()").extract_first()
        # 地址 根据招标人定位地址 也可以根据地址文字定位
        diZHi = selectors.xpath("//div[text()='地址：']/../following-sibling::td[1]/div/text()").get(default='')
        # diZHi = selectors.xpath("//td[contains(text(),'地址：')]/text()").getall()[0]
        # 中标人
        zhongBiaoRen = selectors.xpath("//div[text()='中标人']/../../following-sibling::tr[1]/td[2]//text()").get(default='')
        # 中标价
        zhongBiaoJia = selectors.xpath("//div[text()='中标人']/../../following-sibling::tr[1]/td[3]//text()").get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia,
            'detailUrl': detailUrl,
            'city': '荆门市'

        }

        return items


#  黄冈市
def ruleDetailHuangGangShi(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据 转成html
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        # 招标人
        zhaoBiaoRen = selectors.xpath(
            "//div[text()='招标人或招标代理机构：']/../following-sibling::td[1]/div/text()").extract_first()
        # 地址 根据招标人定位地址 也可以根据地址文字定位
        diZHi = selectors.xpath("//div[text()='地址：']/../following-sibling::td[1]/div/text()").get(default='')
        # diZHi = selectors.xpath("//td[contains(text(),'地址：')]/text()").getall()[0]
        # 中标人
        zhongBiaoRen = selectors.xpath("//div[text()='中标人']/../../following-sibling::tr[1]/td[2]//text()").get(default='')
        # 中标价
        zhongBiaoJia = selectors.xpath("//div[text()='中标人']/../../following-sibling::tr[1]/td[3]//text()").get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia,
            'detailUrl': detailUrl,
            'city': '黄冈市'

        }

        return items


# 孝感市
def ruleDetailXiaoGanShi(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据 转成html
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        # 招标人
        zhaoBiaoRen = selectors.xpath(
            "//div[text()='招标人或招标代理机构：']/../following-sibling::td[1]/div/text()").extract_first()
        # 地址 根据招标人定位地址 也可以根据地址文字定位
        diZHi = selectors.xpath("//div[text()='地址：']/../following-sibling::td[1]/div/text()").get(default='')
        # diZHi = selectors.xpath("//td[contains(text(),'地址：')]/text()").getall()[0]
        # 中标人
        zhongBiaoRen = selectors.xpath("//div[text()='中标人']/../../following-sibling::tr[1]/td[2]//text()").get(default='')
        # 中标价
        zhongBiaoJia = selectors.xpath("//div[text()='中标人']/../../following-sibling::tr[1]/td[3]//text()").get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia,
            'detailUrl': detailUrl,
            'city': '孝感市'
        }

        return items


# 咸宁市
def ruleDetailXianNingShi(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据 转成html
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        # 招标人
        zhaoBiaoRen = selectors.xpath(
            "//div[text()='招标人或招标代理机构：']/../following-sibling::td[1]/div/text()").extract_first()
        # 地址 根据招标人定位地址 也可以根据地址文字定位
        diZHi = selectors.xpath("//div[text()='地址：']/../following-sibling::td[1]/div/text()").get(default='')
        # diZHi = selectors.xpath("//td[contains(text(),'地址：')]/text()").getall()[0]
        # 中标人
        zhongBiaoRen = selectors.xpath("//div[text()='中标人']/../../following-sibling::tr[1]/td[2]//text()").get(default='')
        # 中标价
        zhongBiaoJia = selectors.xpath("//div[text()='中标人']/../../following-sibling::tr[1]/td[3]//text()").get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia,
            'detailUrl': detailUrl,
            'city': '咸宁市'

        }

        return items


# 随州市
def ruleDetailSuiZhouShi(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据 转成html
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        # 招标人
        zhaoBiaoRen = selectors.xpath(
            "//td[text()='项目业主（招标人）']/following-sibling::td[1]/text()").extract_first()
        # 地址 根据招标人定位地址 也可以根据地址文字定位
        diZHi = selectors.xpath("//td[text()='开标地点']/following-sibling::td[1]/text()").get(default='')
        # diZHi = selectors.xpath("//td[contains(text(),'地址：')]/text()").getall()[0]
        # 中标人
        zhongBiaoRen = selectors.xpath("//td[contains(text(),'第一名')]/following-sibling::td[1]//text()").get(default='')
        # 中标价
        zhongBiaoJia = selectors.xpath("//td[contains(text(),'投标最高限价( 元)')]/following-sibling::td[1]//text()").get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia+'元',
            'detailUrl': detailUrl,
            'city': '随州市'

        }

        return items


# 恩施市
def ruleDetailEnShiShi(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据 转成html
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        # 招标人
        zhaoBiaoRen = selectors.xpath(
            "//div[text()='招标人或招标代理机构：']/../following-sibling::td[1]/div/text()").extract_first()
        # 地址 根据招标人定位地址 也可以根据地址文字定位
        diZHi = selectors.xpath("//div[text()='地址：']/../following-sibling::td[1]/div/text()").get(default='')
        # diZHi = selectors.xpath("//td[contains(text(),'地址：')]/text()").getall()[0]
        # 中标人
        zhongBiaoRen = selectors.xpath("//div[text()='中标人']/../../following-sibling::tr[1]/td[2]//text()").get(default='')
        # 中标价
        zhongBiaoJia = selectors.xpath("//div[text()='中标人']/../../following-sibling::tr[1]/td[3]//text()").get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia,
            'detailUrl': detailUrl,
            'city': '恩施市'
        }

        return items


# 仙桃市
def ruleDetailXianTaoShi(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据 转成html
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        # 招标人
        zhaoBiaoRen = selectors.xpath('//p[contains(text(),"招标人：")]/text()').extract_first()
        # 地址 根据招标人定位地址 也可以根据地址文字定位
        diZHi = selectors.xpath('//p[contains(text(),"地址：")]/text()').get(default='')
        # diZHi = selectors.xpath("//td[contains(text(),'地址：')]/text()").getall()[0]
        # 中标人
        zhongBiaoRen = selectors.xpath('//th[contains(text(),"企业名称")]/../following-sibling::tr/td[1]/text()').get(default='')
        # 中标价
        zhongBiaoJia = selectors.xpath('//th[contains(text(),"投标报价（万元）")]/../following-sibling::tr/td[2]/text()').get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia + '万元',
            'detailUrl': detailUrl,
            'city': '仙桃市'

        }

        return items


# 天门市
def ruleDetailTianMenShi(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据 转成html
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        # 招标人
        zhaoBiaoRen = selectors.xpath(
            '//span[contains(text(),"招标代理机构：")]/text()').extract_first()
        # 地址 根据招标人定位地址 也可以根据地址文字定位
        diZHi = selectors.xpath('//span[contains(text(),"地址：")]/text()').get(default='')
        # diZHi = selectors.xpath("//td[contains(text(),'地址：')]/text()").getall()[0]
        # 中标人
        zhongBiaoRen = selectors.xpath(
            '//span[contains(text(),"中标人")]/../../../following-sibling::tr/td[1]//span/text()').get(default='')
        # 中标价
        zhongBiaoJia = selectors.xpath(
            '//span[contains(text(),"中标人")]/../../../following-sibling::tr/td[2]//span/text()').get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia + '元',
            'detailUrl': detailUrl,
            'city': '天门市'

        }

        return items


# 潜江市
def ruleDetailQianJiangShi(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据 转成html
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        # 招标人
        zhaoBiaoRen = selectors.xpath(
            '//p[contains(text(),"招标人：")]/text()').extract_first()
        # 地址 根据招标人定位地址 也可以根据地址文字定位
        diZHi = selectors.xpath('//p[contains(text(),"地址：")]/text()').get(default='')
        # diZHi = selectors.xpath("//td[contains(text(),'地址：')]/text()").getall()[0]
        # 中标人
        zhongBiaoRen = selectors.xpath(
            '//p[contains(text(),"中标人")]/../../following-sibling::tr/td[1]/p/text()').get(default='')
        # 中标价
        zhongBiaoJia = selectors.xpath(
            '//p[contains(text(),"中标价")]/../../following-sibling::tr/td[2]/p/text()').get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia + '元',
            'detailUrl': detailUrl,
            'city': '潜江市'

        }

        return items


# 神农架
def ruleDetailShenNongJia(jsonData, detailUrl):
    for dat in jsonData.get('list'):
        # 发布时间
        bulletinIssueTime = dat.get('bulletinIssueTime')
        bulletinName = dat.get('bulletinName')

        # 获取表格中的所有数据 转成html
        bulletinContent = dat.get('bulletincontent')
        selectors = Selector(text=bulletinContent)

        # 标准的格式 类似这种: https://www.hbggzyfwpt.cn/jyxx/jsgcZbjggsDetail?guid=804c6b5b-e69f-4118-8d38-9c9d9413eb65&isOther=false
        # 招标人
        zhaoBiaoRen = selectors.xpath("//td[contains(text(),'招标人：')]/text()").get(default='')
        # 地址 根据招标人定位地址 也可以根据地址文字定位
        diZHi = selectors.xpath("//td[contains(text(),'招标人：')]/../following-sibling::tr[1]/td/text()").get(default='')
        # diZHi = selectors.xpath("//td[contains(text(),'地址：')]/text()").getall()[0]
        # 中标人
        zhongBiaoRen = selectors.xpath("//td[text()='中标人']/../following-sibling::tr/td[1]/text()").get(default='')
        # 中标价
        zhongBiaoJia = selectors.xpath("//td[text()='中标价(元)']/../following-sibling::tr/td[2]/text()").get(default='')

        items = {
            'bulletinIssueTime': bulletinIssueTime,
            'zhaoBiaoRen': zhaoBiaoRen,
            'bulletinName': bulletinName,
            'diZHi': diZHi,
            'zhongBiaoRen': zhongBiaoRen,
            'zhongBiaoJia': zhongBiaoJia + '元',
            'detailUrl': detailUrl,
            'city': '神农架'

        }

        return items

