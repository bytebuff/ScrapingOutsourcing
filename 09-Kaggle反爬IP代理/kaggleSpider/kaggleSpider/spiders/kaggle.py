# -*- coding: utf-8 -*-
import scrapy
import json, re, time
import requests
from scrapy.utils.project import get_project_settings


class KaggleSpider(scrapy.Spider):
    name = 'kaggle'
    allowed_domains = ['kaggle.com']
    start_urls = [f'https://www.kaggle.com/topics.json?sortBy=new&group=all&page={page}&pageSize=20&category=all' for page in range(525, 300000)]
    headers = get_project_settings().get('DEFAULT_REQUEST_HEADERS')
    def parse(self, response):
        print(response.url)
        json_data = json.loads(response.text)
        if json_data.get('topics'):
            for dat in json_data['topics']:
                displayName = dat.get('userAvatar').get('displayName') # 显示的名字
                title = dat.get('title')
                _id = dat.get('id') # 提取id 用来获取评论信息
                userUrl = dat.get('userAvatar').get('userUrl')
                tier = dat.get('userAvatar').get('tier')

                item = self.getUserData(userUrl, self.headers)

                items = f'{title},{displayName},{tier},' + item

                #print(items)

                # 获取的是评论人的信息
                commentsUrl = f'https://www.kaggle.com/topics/{_id}/comments.json?filter=all&sort=hot'
                response = requests.get(commentsUrl, headers=self.headers).json()
                #print(response)
                if response.get('comments'):
                    for com in response['comments']:
                        userUrl = com.get('author').get('userUrl')
                        _displayName = com.get('author').get('displayName')
                        tier = com.get('author').get('tier')
                        comments = self.getUserData(userUrl, headers=self.headers)

                        allItem = items + f"{_displayName},{tier}," + comments

                        allItem = {
                            'allItem': allItem
                        }

                        yield allItem

    # 获取用户的level, Post， comment信息
    @staticmethod
    def getUserData(userUrl, headers):
        _userUrl = f'https://www.kaggle.com{userUrl}/discussion_counts.json'  # 用来获取Total Post等
        # _user = f'https://www.kaggle.com{userUrl}/discussion'

        responseJson = requests.get(_userUrl, headers=headers) # 返回json数据
        # time.sleep(2.5)
        # responseText = requests.get(_user, headers=headers)  # 获取的是文本数据
        json_data = responseJson.json()
        # 获取Json数据
        totalDiscussions = json_data.get('totalDiscussions')
        totalReplies = json_data.get('totalReplies')

        # 获取文本数据 "performanceTier":"expert","performanceTierCategory":"competitions",
        # level = re.findall('"performanceTier":"(.*?)","performanceTierCategory":"(.*?)"', responseText.text)
        # level = '-'.join(reversed(list(*level)))


        # 返回数据
        return f'{totalDiscussions},{totalReplies},'