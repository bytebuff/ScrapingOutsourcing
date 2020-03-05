# coding:gbk
import requests
import re
import execjs
from pprint import pprint

url = 'https://www.whoscored.com/matchesfeed/?d=20190415'
headers = {
    'accept': 'text/plain, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': 'visid_incap_774904=fU6xUqILRe2ljOs7rHNT4xz/r1wAAAAAQUIPAAAAAADTr/hLFJfTan7WTjhCIOny; _ga=GA1.2.901709446.1555037986; _ym_uid=155503799141660844; _ym_d=1555037991; incap_ses_795_774904=fFBKQgYNPQ/BKieoAWkICySdtVwAAAAA8N1zLQv8sM1SqYTBJ6ZH4g==; _gid=GA1.2.1923591844.1555406123; incap_ses_462_774904=s0e4WI6+qzyIdJI+YVtpBqDAtVwAAAAAm5hDFP55aDLR1PyzKVSFbA==; incap_ses_635_774904=fikcTTH3mQKXXPHcG/rPCHKctlwAAAAAxoI9hUkHvExOpIxRn3pioQ==; _ym_isad=2; incap_ses_426_774904=HOn5fAdTLRHeHMCrsnXpBRTOtlwAAAAAA2U/wm4MnIUTSC7ZwO3PBw==; incap_ses_407_774904=iitcW7TwYQY7lxHWY/alBZjrtlwAAAAAjWWpao0WZcC0gOCv3jhNxA==; _ym_visorc_52685938=w',
    'model-last-mode': '7eEPm91xLct1ym6cQmP6//joAEWAZzFOklNiepvJ8jM=',
    'referer': 'https://www.whoscored.com/LiveScores',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
response = requests.get(url, headers=headers).text

data = execjs.eval(f'{response}')

pprint(data[1])