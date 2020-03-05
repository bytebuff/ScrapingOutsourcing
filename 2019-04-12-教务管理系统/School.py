import requests # 导入模块 安装pip install requests
from parsel import Selector # 导入数据提取的模块 安装pip install parsel

# 数据采集的类
class School(object):

    # 初始化
    def __init__(self):
        # post网址
        self.url = 'https://curricula.bfsu.edu.cn/academic/manager/score/studentOwnScore.do?groupId=&moduleId=2021&randomString=20190412154854jQaI8c'
        # 提交的数据
        self.data = {
                'year': '',
                'term': '',
                'prop': '',
                'para': '0',
                'sortColumn': '',
                'Submit': '查询'
            }
        # 请求头  加上Cookie 登陆信息
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'content-length': '62',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'JSESSIONID=5502D2338DAFFB68DA5F55F7C10275DF.TA3',
            'origin': 'https://curricula.bfsu.edu.cn',
            'referer': 'https://curricula.bfsu.edu.cn/academic/manager/score/studentOwnScore.do?groupId=&moduleId=2021&randomString=20190412154854jQaI8c',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
            }

    def postData(self):
        # 发出请求
        response = requests.post(self.url, data=self.data, headers=self.headers)
        selector = Selector(text=response.text)
        # 提取数据
        for sel in selector.xpath('//table[@class="datalist"]/tr'):
            data = sel.xpath('.//td/text()').getall()
            if data:
                data.pop(-1)
                data.pop(-1)
                data.pop(-1)
                data.pop(-3)
                data.pop(2)
                data = [data.strip() for data in data]
                str_data = ','.join(data)
                yield str_data
            
    # 保存数据
    def save2csv(self, data):
        with open('School.csv', 'a', encoding='utf-8') as fp:
            fp.write(data+'\n')

if __name__ == "__main__":

    # 实例化类
    school = School()
    # 调用方法采集数据
    data = school.postData()
    # 保存数据 data是生成器
    for dat in data:
        print(dat)
        school.save2csv(dat)
