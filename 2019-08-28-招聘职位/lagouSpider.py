import time
import requests


class LaGouSpider(object):

    def __init__(self):
        # 招聘数据网址
        self.url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
        # 请求头的添加-->反爬虫
        self.header = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            #'Content-Length': '20',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': '_ga=GA1.2.1240643066.1540209044; user_trace_token=20181022195043-b4f35172-d5f0-11e8-977d-525400f775ce; LGUID=20181022195043-b4f35434-d5f0-11e8-977d-525400f775ce; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22166ebeb76562b8-0fce0a466e86c9-36664c08-1049088-166ebeb765710%22%2C%22%24device_id%22%3A%22166ebeb76562b8-0fce0a466e86c9-36664c08-1049088-166ebeb765710%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpt_baidu_pc%22%7D%7D; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=7; JSESSIONID=ABAAABAAAIAACBI3291E87D2E06945F5495A1614DEC99FC; _gat=1; _gid=GA1.2.664604178.1556024620; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1555221774,1555913567,1555917348,1556024620; LGSID=20190423210340-370ef058-65c8-11e9-9c2e-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=index_search; SEARCH_ID=a3403390e0f8427b8778c63f6bfb1a26; X_HTTP_TOKEN=010cabdaca147f5d62642065515e2327bd48e181a6; LGRID=20190423210346-3aaaad9a-65c8-11e9-b0bc-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1556024627',
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_?labelWords=&fromSearch=true&suginput=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
            'X-Anit-Forge-Code': '0',
            'X-Anit-Forge-Token': 'None',
            'X-Requested-With': 'XMLHttpRequest',
        }

    def laGouSpider(self, pageNum):
        '''获取数据'''

            # 表单数据
        data = {
            'first': 'false',
            'pn': str(pageNum),
            'kd': ''
        }
        # 暂停1s
        # 提交表单数据
        response = requests.post(self.url, data=data, headers=self.header)

        # 返回结果
        return response.json()

    def parseResponse(self, response):
        '''解析数据 提取数据'''
        data = response['content']['positionResult']
        # 遍历提取数据
        for dat in data['result']:
            # 岗位职称
            positionName = dat['positionName']
            # 工作经验
            workYear = dat['workYear']
            # 学历要求
            education = dat['education']
            # 工作类型
            jobNature = dat['jobNature']
            # 公司发展
            financeStage = dat['financeStage']
            # 工作地点
            city = dat['city']
            # 工资
            salary = dat['salary']
            # 工作福利
            # positionAdvantage = dat['positionAdvantage']
            # 公司名称
            companyShortName = dat['companyShortName']

            data = f'{positionName},{workYear},{education},{jobNature},{financeStage},{city},{salary},{companyShortName}'
            print(data)
            # 保存数据
            self.save2File(data)

    def save2File(self, data):
        '''保存数据'''

        with open('BeiJingData.csv', 'a', encoding='utf-8') as fp:
            fp.write(data + '\n')


if __name__ == '__main__':
    # 实例化爬虫类
    lagouspider = LaGouSpider()
    # 调用爬取数据的方法
    for pn in range(1, 31):
        jsonResponse = lagouspider.laGouSpider(pn)
        print(jsonResponse)
        # 循环遍历数据并解析保存
        print(pn)
        lagouspider.parseResponse(jsonResponse)
        time.sleep(60)


