import time, re
from scrapy.loader.processors import SelectJmes


def timeStampTransform(timeStamp):
    # 时间戳转日期
    timeArray = time.localtime(timeStamp / 1000)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime  # 2019-12-29 11:30:00


def paimaiStatus(paimaiStatusResp):
    # 拍断拍卖状态 已结束(流拍, 成功)
    auctionStatus = SelectJmes('auctionStatus')(paimaiStatusResp)  # 拍卖状态
    orderStatus = SelectJmes('orderStatus')(paimaiStatusResp)  # 拍卖详细状态

    if auctionStatus == '1':  # 正在拍卖
        if orderStatus == 3:
            return '正在进行'
    elif auctionStatus == '0':  # 预告中
        if orderStatus == 3:
            return '尚未开始'
    elif auctionStatus == '2':
        if orderStatus in [0, -1]:
            return '流拍'
        else:
            return '成功'
    return ''


def principalAmount(amount):
    if amount:
        amount = ''.join(amount)
        result = re.search('贷款余额： (.*? 元)', amount)
        if result: return result.group(1)
        result = re.search('本金 为 (.*? 元)', amount)
        if result: return result.group(1)
        result = re.search('贷款余额：(.*?元)', amount)
        if result: return result.group(1)
        result = re.search('(.*?元)', amount)
        if result: return result.group(1)
        result = re.search('(.*?万元)', amount)
        if result: return result.group(1)
        result = re.search('(合计.*?)', amount)
        if result: return result.group(1)
        result = re.search('债权本金：(.*?元)', amount)
        if result: return result.group(1)
        result = re.search('债权本金(.*?元)', amount)
        if result: return result.group(1)
        result = re.search('本金(.*?元)', amount)
        if result: return result.group(1)
        result = re.search('本金(.*?万元)', amount)
        if result: return result.group(1)
        print('*'*80)
        print(result, amount)
    else:
        return ''

def wanYuanToyuan(wanYuan):
    # 万元转换成元

    # 先统一格式
    wanYuan = re.sub(',| ', '', wanYuan)
    if '万元' in wanYuan:
        wanYuan_float = re.search('(\d+(\.\d+)?)', wanYuan).group(1)
        yuan = round(float(wanYuan_float) * 10000, 4)
        return str(yuan) + '元'
    else:
        return wanYuan
    return wanYuan


def cleanNotIncludeYuan(notYuan):
    if '元' not in notYuan:
        return ''
    elif 20 < len(notYuan):
        return ''
    else:
        return notYuan



if __name__ == '__main__':
    timeStampTransform(1577590200000)
    paimaiStatus({})
