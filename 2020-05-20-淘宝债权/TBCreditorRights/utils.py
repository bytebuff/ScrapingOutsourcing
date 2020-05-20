"""
     工具函数
"""
import datetime

def daybyday(startdate, enddate):
    """
    输入开始和结束时间返回在此区间内的每天的时间
    :param startdate: 开始时间 eg：2020-01-01
    :param enddate: 结束时间：eg：2020-02-01
    :return: 在这个时间内的每一天的日期
    """
    startdate = datetime.datetime.strptime(startdate, "%Y-%m-%d")
    enddate = datetime.datetime.strptime(enddate, "%Y-%m-%d")

    day_list = []
    while startdate <= enddate:
        date_str = startdate.strftime("%Y-%m-%d")
        day_list.append(date_str)
        startdate += datetime.timedelta(days=1)
    return day_list