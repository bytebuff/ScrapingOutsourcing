# coding:utf-8

# 考虑到大家经常在网上看见python2的代码，而我们现在用python3，所以提示一下：
# 在python3.3后urllib2已经不能再用，而直接用urllib，同时注意它分成了一些子包。
# urlopen() 及 Request对象，都在urllib.request子包下面。
# urlencode() 则在 urllib.parse 子包下面。

import urllib.request
import re

#在mac系统下，要加上以下两句，才可以使用https
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


urls = {}  # 记录所有的url及其是否下载(key是url,而value则是状态waiting或done)


def getPage(url):
    html = urllib.request.urlopen(url).read().decode("utf-8")  # 这里假定都是utf-8编码，这符合90%的网页
    return html


def parsePage(html):
    linkRe = r'href="(https?://.*?)"'  # 这是链接的正则表达式，注意r及单引号、双引号及.*?
    pattern = re.compile(linkRe)
    links = pattern.findall(html)
    # print(links)
    return links


def crawl():
    while len(urls) > 0:

        # 从中找到一个处于waiting状态的url，作为当前要下载的url
        current = None
        for url in urls:
            if urls[url] == "waiting":
                current = url  # 找到一个url作为当前的url
                break
        if current == None:  # 如果没能找到可下载的网页，则退出
            break

        # 下面是真正的开始爬取一个网页
        try:  # 考虑到网络经常出错，最好是用try...except来处理错误
            print(current)
            
            # 得到网页
            html = getPage(current)  
            
            # 解析网页
            links = parsePage(html)  

            # 将新的链接加进来，并且标记为waiting状态
            for link in links:  
                if link not in urls:
                    urls[link] = "waiting"

        except Exception as ex:
            print(ex)
        finally:
            urls[current] = "done"  # 标记该链接已下载


def main():
    startUrl = "http://www.pku.edu.cn"
    urls[startUrl] = "waiting"  # 放入最开始的网页地址

    print("开始爬行...（按Ctrl+C可以中断）")

    crawl()


main()