# -*- coding: utf-8 -*-
import scrapy
import execjs
import time, calendar

# 时间的计算
def get_all_days():

    for year in range(2019, 2020):
        for month in range(1, 13):
            days = calendar.monthcalendar(year=year, month=month)
            flatten_days = sum(days, [])
            for flatten_day in flatten_days:
                if flatten_day!=0:
                    # print(flatten_day)
                    if len(str(month))==1:
                        if len(str(flatten_day))==1:
                            time_format = str(year) + '0'+str(month) + '0'+str(flatten_day)
                            yield time_format
                        else:
                            time_format = str(year) + '0' + str(month) + str(flatten_day)
                            yield time_format
                    else:
                        if len(str(flatten_day))==1:
                            time_format = str(year) + str(month) + '0'+str(flatten_day)
                            yield time_format
                        else:
                            time_format = str(year) + str(month) + str(flatten_day)
                            yield time_format



class WhoscoredSpider(scrapy.Spider):
    name = 'whoscored'
    allowed_domains = ['whoscored.com']
    # start_urls = [f'https://www.whoscored.com/matchesfeed/?d={d}' for d in get_all_days()]
    start_urls = [f'https://www.whoscored.com/matchesfeed/?d=20190505']

    def parse(self, response): # 第一组中的第14个元素代表的是是否有Report的国家 然后再在国家里面选择球赛(一个国家可能对应几个球赛， 而这些球赛都有Report)
        # 使用JS转化为数组，在Python中就是列表
        try:
            list_data = execjs.eval(response.text)
            for dat1 in list_data[1]:
                if dat1[14] == 1:
                    for dat2 in list_data[2]:
                        if dat1[0] in dat2:
                            match_id = dat2[1] # 提取match_id 用来构造网址
                            team_id = dat2[4] # 提取team_id用来构造网址
                            data = dat1 + dat2
                            #yield data

                            items = {
                                'data': data
                            }

                            yield items
        except:
            pass
            # match_summary_url = f'https://www.whoscored.com/StatisticsFeed/1/GetMatchCentrePlayerStatistics?category=summary&subcategory=all&statsAccumulationType=0&isCurrent=true&playerId=&teamIds={team_id}&matchId={match_id}&stageId=&tournamentOptions=&sortBy=&sortAscending=&age=&ageComparisonType=&appearances=&appearancesComparisonType=&field=&nationality=&positionOptions=&timeOfTheGameEnd=&timeOfTheGameStart=&isMinApp=&page=&includeZeroValues=&numberOfPlayersToPick='
            # match_offensive_url = f'https://www.whoscored.com/StatisticsFeed/1/GetMatchCentrePlayerStatistics?category=offensive&subcategory=all&statsAccumulationType=0&isCurrent=true&playerId=&teamIds={team_id}&matchId={match_id}&stageId=&tournamentOptions=&sortBy=&sortAscending=&age=&ageComparisonType=&appearances=&appearancesComparisonType=&field=&nationality=&positionOptions=&timeOfTheGameEnd=&timeOfTheGameStart=&isMinApp=&page=&includeZeroValues=&numberOfPlayersToPick='
            # match_defensive_url = f'https://www.whoscored.com/StatisticsFeed/1/GetMatchCentrePlayerStatistics?category=defensive&subcategory=all&statsAccumulationType=0&isCurrent=true&playerId=&teamIds={team_id}&matchId={match_id}&stageId=&tournamentOptions=&sortBy=&sortAscending=&age=&ageComparisonType=&appearances=&appearancesComparisonType=&field=&nationality=&positionOptions=&timeOfTheGameEnd=&timeOfTheGameStart=&isMinApp=&page=&includeZeroValues=&numberOfPlayersToPick='
            # match_passing_url = f'https://www.whoscored.com/StatisticsFeed/1/GetMatchCentrePlayerStatistics?category=passing&subcategory=all&statsAccumulationType=0&isCurrent=true&playerId=&teamIds={team_id}&matchId={match_id}&stageId=&tournamentOptions=&sortBy=&sortAscending=&age=&ageComparisonType=&appearances=&appearancesComparisonType=&field=&nationality=&positionOptions=&timeOfTheGameEnd=&timeOfTheGameStart=&isMinApp=&page=&includeZeroValues=&numberOfPlayersToPick='
            # 网址的拼凑是dat2中的第二个参数和第九个参数  category=summary 用来控制分类
            # 数据分开保存吧。不对应数据了
            # 球赛一个表 球员数据一个表
            # yield scrapy.Request(match_summary_url, callback=self.matchParse)
            # yield scrapy.Request(match_offensive_url, callback=self.matchParse)
            # yield scrapy.Request(match_defensive_url, callback=self.matchParse)
            # yield scrapy.Request(match_passing_url, callback=self.matchParse)


    # def matchParse(self, response):
    #     # 不同的数据建议通过外键连接两个数据表
    #     # 提取比赛数据
    #     print(response.text)
