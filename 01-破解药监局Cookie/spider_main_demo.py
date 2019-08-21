#coding:utf-8
import requests
import execjs
from lxml import etree
from urllib import parse


with open('getcookie.js','r',encoding='utf-8') as f:
    js1 = f.read()
    ecjs = execjs.compile(js1)

class SpiderMain(object):

    def __init__(self, tableId, tableView, page):

        self.tableView = tableView
        # 参数
        self.F82S = ''
        self.F82T = ''
        self.F82T_true = ''
        self.JSESSIONID = ''
        self.meta = ''
        self.url = 'http://app1.sfda.gov.cn/datasearchcnda/face3/base.jsp?tableId=27&tableName=TABLE27&title=%E8%BF%9B%E5%8F%A3%E5%99%A8%E6%A2%B0&bcId=152904442584853439006654836900'
        self.url_list = 'http://app1.sfda.gov.cn/datasearchcnda/face3/search.jsp'
        # 请求头
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache - Control": "max - age = 0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Host": "app1.sfda.gov.cn",
            "Referer": "http://app1.sfda.gov.cn/datasearchcnda/face3/base.jsp?tableId=28&tableName=TABLE28&title=%BB%A5%20%%20C1%20%%20AA%20%%20CD%20%%20F8%20%%20D2%20%%20A9%20%%20C6%20%%20B7%20%%20D0%20%%20C5%20%%20CF%20%%20A2%20%%20B7%20%%20FE%20%%20CE%20%%20F1%20&%20bcId%20=%20152912030752488832300204864740",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
        }
        # 请求cookie
        self.cookies = {
            'FSSBBIl1UgzbN7N82S':'',
            'FSSBBIl1UgzbN7N82T':'',
            'JSESSIONID':''
        }
        # 列表页请求参数 post表单
        self.data = {
            'tableId': tableId, # 器械的id
            'curstart': str(page), # 控制翻页
            # 器械的编码
            'tableView': parse.quote(tableView,encoding='gbk') ,   #'%E4%BA%92%E8%81%94%E7%BD%91%E8%8D%AF%E5%93%81%E4%BF%A1%E6%81%AF%E6%9C%8D%E5%8A%A1',
        }

    def getCookie(self):
        rsq =requests.get(self.url,headers = self.headers)
        rsq.close()
        print(rsq.cookies)
        #第一次请求得到假的f82s,f82t,和metacontent
        self.F82S = rsq.cookies['FSSBBIl1UgzbN7N82S']
        self.F82T = rsq.cookies['FSSBBIl1UgzbN7N82T']
        rsqHtml = etree.HTML(rsq.text)
        self.meta = rsqHtml.xpath('//*[@id="9DhefwqGPrzGxEp9hPaoag"]/@content')[0]
        self.F82T_true = ecjs.call("getcookie", self.meta,self.F82T)
        self.cookies['FSSBBIl1UgzbN7N82S'] = self.F82S
        self.cookies['FSSBBIl1UgzbN7N82T'] = self.F82T_true
        # rsq = requests.get(self.url, headers=self.headers,cookies = self.cookies)
        # print(rsq.cookies)
        #self.JSESSIONID = rsq.cookies['JSESSIONID']
        #self.cookies['JSESSIONID'] = self.JSESSIONID



    def getlist(self):
        rsqlist = requests.post(self.url_list, headers=self.headers, cookies=self.cookies, data=self.data)
        rsqlistHtml = etree.HTML(rsqlist.text)
        print(rsqlist.cookies)
        lists = rsqlistHtml.xpath('//a[contains(@href,"javascript:commitForECMA")]')
        for list in lists:
            name = list.xpath('./text()')[0]
            url = list.xpath('./@href')[0]
            url = "http://app1.sfda.gov.cn/datasearchcnda/face3/" + url[url.index('content.jsp?'):url.index("',null")]
            detail_url = parse.quote(url, safe='/:?=&', encoding='gbk')
            print(name)
            #
            print(detail_url)
            # 详情页
            content = requests.get(detail_url, headers=self.headers, cookies=self.cookies)
            contentHtml = etree.HTML(content.text)
            contentList = contentHtml.xpath('//div[@class="listmain"]//tr')
            list_content = []
            for i in range(1,len(contentList)-1):
                contentList[i].xpath('./tr/text()')
                value_ls = contentList[i].xpath("./td")
                # 标题 键 key
                value1 = value_ls[0].xpath('string(.)')
                # 对应的值 value
                value2 = value_ls[1].xpath('string(.)')
                print(value1)
                print(value2)


def save_to_file(data):
    '''
    保存数据
    :return: None
    '''
    with open() as fp:
        fp.write(data)


if __name__ == '__main__':

    for page in range(1, 3):

        spider = SpiderMain(26, '国产器械', page)
        spider.getCookie()
        spider.getlist()
