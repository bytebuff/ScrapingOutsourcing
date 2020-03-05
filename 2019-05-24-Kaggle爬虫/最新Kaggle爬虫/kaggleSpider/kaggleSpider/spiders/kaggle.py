# -*- coding: utf-8 -*-
import scrapy
import json, re, time
import requests
from scrapy.utils.project import get_project_settings


class KaggleSpider(scrapy.Spider):

    name = 'kaggle'
    allowed_domains = ['kaggle.com']
    start_urls = [f'https://www.kaggle.com/forums/130117/topics.json?sortBy=hot&group=all&page={page}&pageSize=20&category=all&turbolinks%5BrestorationIdentifier%5D=8c2d47d4-5382-41ed-89ed-ad95e75178c0' for page in range(30, 45)]
    headers = get_project_settings().get('DEFAULT_REQUEST_HEADERS')

    def parse(self, response):
        print(response.url)
        json_data = json.loads(response.text)
        if json_data.get('topics'):
            for dat in json_data['topics']:
                displayName = dat.get('userAvatar').get('displayName') # 显示的名字
                # 标题
                title = dat.get('title')
                # 添加发布时间
                postDate = dat.get('postDate')
                _id = dat.get('id') # 提取id 用来获取评论信息
                # userUrl = dat.get('userAvatar').get('userUrl')
                tier = dat.get('userAvatar').get('tier')

                item = {
                    'displayName': displayName,
                    'title': title,
                    'postDate': postDate,
                    '_id': _id,
                    # 'userUrl': userUrl,
                    'tier': tier,
                }

                topics_url = f'https://www.kaggle.com/topics/{_id}.json'

                yield scrapy.Request(topics_url, callback=self.parse_topic, meta=item)

    def parse_topic(self, response):

        item = response.meta

        json_data = json.loads(response.text)

        # 发帖人的
        if json_data.get('comment'):
            data = json_data['comment']
            # 提取数据
            _displayName = data.get('author').get('displayName')
            _tier = data.get('author').get('tier')
            _competitionRanking = data.get('competitionRanking')
            _postDate = data.get('postDate')
            _userUrl = data.get('author').get('userUrl')
            _totalDiscussions, _totalReplies, _totalTopics, _totalUpvotes = self.get_user_data(_userUrl, headers=self.headers)
            _city, _userJoinDate, _followers, _following = self.get_user_city(_userUrl, headers=self.headers)
        # 发帖人
        item.update({
            '_displayName': _displayName,
            '_tier': _tier,
            '_competitionRanking': _competitionRanking,
            '_postDate': _postDate,
            '_userUrl': _userUrl,

            '_totalDiscussions': _totalDiscussions,
            '_totalReplies': _totalReplies,
            '_totalTopics': _totalTopics,
            '_totalUpvotes': _totalUpvotes,

            '_city': _city,
            '_userJoinDate': _userJoinDate,
            '_followers': _followers,
            '_following': _following,
        })

        # 评论人的
        if json_data.get('commentList').get('comments'):
            for data in json_data['commentList']['comments']:
                displayName = data.get('author').get('displayName')
                tier = data.get('author').get('tier')
                competitionRanking = data.get('competitionRanking')
                # _id_ = data.get('id')

                postDate = data.get('postDate')
                userUrl = data.get('author').get('userUrl')

                totalDiscussions, totalReplies, totalTopics, totalUpvotes = self.get_user_data(userUrl, headers=self.headers)
                city, userJoinDate, followers, following = self.get_user_city(userUrl, headers=self.headers)

                # 评论人
                item.update({
                    'displayName': displayName,
                    'tier': tier,
                    'competitionRanking': competitionRanking,
                    'postDate': postDate,
                    'userUrl': userUrl,

                    'totalDiscussions': totalDiscussions,
                    'totalReplies': totalReplies,
                    'totalTopics': totalTopics,
                    'totalUpvotes': totalUpvotes,

                    'city': city,
                    'userJoinDate': userJoinDate,
                    'followers': followers,
                    'following': following,
                    # '_id_': _id_,

                })

                data = [
                        # 发帖人
                        item.get('title'), item.get('_displayName'), item.get('_tier'),
                        item.get('_postDate'), item.get('_competitionRanking'),
                        item.get('_totalDiscussions'), item.get('_totalReplies'),
                        item.get('_totalTopics'), item.get('_totalUpvotes'),
                        item.get('_city'), item.get('_userJoinDate'),
                        item.get('_followers'), item.get('_following'),
                        # 回帖人
                        item.get('displayName'), item.get('tier'),
                        item.get('postDate'), item.get('competitionRanking'),
                        item.get('totalDiscussions'), item.get('totalReplies'),
                        item.get('totalTopics'), item.get('totalUpvotes'),
                        item.get('city'), item.get('userJoinDate'),
                        item.get('followers'), item.get('following'),
                        ]

                items = {
                    'data': data
                }

                yield items


    # 得到用户的 Total Posts   Comments  Topics  Net Votes
    @staticmethod
    def get_user_data(userUrl, headers):
        # print('我是userUrl', userUrl)
        _userUrl = f'https://www.kaggle.com{userUrl}/discussion_counts.json'  # 用来获取Total Post等
        responseJson = requests.get(_userUrl, headers=headers) # 返回json数据
        json_data = responseJson.json()
        # 获取Json数据
        totalDiscussions = json_data.get('totalDiscussions')
        totalReplies = json_data.get('totalReplies')
        totalTopics = json_data.get('totalTopics')
        totalUpvotes = json_data.get('totalUpvotes')

        # 返回数据 可能存在数据没有的情况 也就是说必须返回四个 调用的时候才能正常解包
        return totalDiscussions,totalReplies,totalTopics,totalUpvotes

    # 获取城市等地方
    @staticmethod
    def get_user_city(userUrl, headers):

        url_ip = 'http://127.0.0.1:5010/get/'

        ip = requests.get(url_ip).text

        proxies = {
            'https': ip.strip(),
            'http': ip.strip()
        }

        print(proxies)

        user_url = f'https://www.kaggle.com{userUrl}/discussion'
        response = requests.get(user_url, headers=headers, proxies=proxies).text

        city = re.findall('"city":"(.*?)"', response)
        city = city[0] if city else ''

        country = re.findall('"country":"(.*?)"', response)
        country = country[0] if country else ''

        userJoinDate = re.findall('"userJoinDate":"(.*?)"', response)
        userJoinDate = userJoinDate[0] if userJoinDate else ''


        # userLastActive = re.findall('"userLastActive":"(.*?)"', response)
        count = re.findall('"count":(\d+),', response) # 会得到两个follow 第一个是Followers 第二个是Following
        if len(count)==2:
            followers = count[0]
            following = count[1]
        else:
            followers = ''
            following = ''

        # 返回数据 可能存在数据没有的情况 也就是说必须返回四个 调用的时候才能正常解包
        return city+"-"+country,userJoinDate,followers,following