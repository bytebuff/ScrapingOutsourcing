import requests

url = 'https://apigateway-toc.youzy.cn/Data/ScoreLines/Fractions/Professions/Query'

headers = {
    'Youzy-Signature': '72ee2a12217e7eccf8def78c9b8154af',
    'YouzyApp_Sign': 'TZONLZSLZfBOFDOfDZNDtZtGFFCZOSCSNZO',
    'YouzyApp_ApiSign': 'LYWVLluIWulRQLrWlrWLIhurrPLyLVRP',
    'YouzyApp_DataSign': 'OYATPRAIPTOQSSSPTAEQYAOTAPTTQtYOYITTPYY',
    'YouzyApp_SuperSign': 'NXHMqXHCZBHMJQqVBXKMZLqXK',
    'YouzyApp_FromSource': 'Android-5.0',
    'YouzyApp_IP': '192.168.0.101',
    'WelcomeYouzyApi': 'How much do you want Please call me at 13626686806',
    'YouzyMedia_Signature': 'TZOCNLZSLZfBOFDOfDZN',
    'Content-Type': 'application/json; charset=UTF-8',
    'Content-Length': '77',
    'Host': 'apigateway-toc.youzy.cn',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.10.0',
}

data={"batch":1,"courseType":0,"uCode":"61_838_0_0","yearFrom":2015,"yearTo":2015}

response = requests.post(url, json=data, headers=headers)

print(response.json())