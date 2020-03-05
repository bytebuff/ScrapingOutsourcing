"""
使用正则表达式将headers转换成python字典格式的工具函数
"""

import re

headers_str = """


Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Content-Length: 242
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: OUTFOX_SEARCH_USER_ID=1726048911@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=998841688.7251934; _ntes_nnid=a31cda64b2586670bbfaa1138bf220fc,1554879349324; _ga=GA1.2.851305956.1555316006; UM_distinctid=16da61899b0103-06f9f6efe74f1c-67e1b3f-100200-16da61899b1586; JSESSIONID=abc-yRFtO39wFfDRIpR9w; ___rl__test__cookies=1578054065598
Host: fanyi.youdao.com
Origin: http://fanyi.youdao.com
Pragma: no-cache
Referer: http://fanyi.youdao.com/?keyfrom=fanyi-new.logo
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36
X-Requested-With: XMLHttpRequest


"""

pattern = '^(.*?): (.*)$'
#           1     2
for line in headers_str.splitlines():
    print(re.sub(pattern, '\'\\1\': \'\\2\',', line))
