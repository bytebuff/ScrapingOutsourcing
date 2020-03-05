# -*- coding: utf-8 -*-
import requests
import base64

#获取access_token
#ApiKey为官网获取的AK，SecretKey 为官网获取的SK
ApiKey = "Lgk3vC7FXQfQGW76zVg4pZKO"   #此处填写自己申请的key
SecretKey = "bB8kbhl1Pnef3NG6MfG5AaYmI3SV53YC"   #此处填写自己申请的key
url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'

headers={'Content-Type': 'application/json; charset=UTF-8'}
response1=requests.post(url=url.format(ApiKey,SecretKey), headers=headers)
json1 = response1.json() #<class 'dict'>
access_token=json1['access_token']

#转换图片数据成base64编码
filepath=r'C:\Users\tds\Pictures\7.jpg'
f = open(filepath, 'rb')
pic = base64.b64encode(f.read())
f.close()
base64=str(pic,'utf-8')
#print(base64)

#访问人脸检测api
request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
params = {"image":base64, "image_type":"BASE64",
    "face_field":"age,beauty,expression,faceshape,gender,glasses,race,quality,facetype"}  #还可以有landmark
headers={'Content-Type': 'application/json'}
request_url = request_url + "?access_token=" + access_token
response1=requests.post(url=request_url, data=params, headers=headers)
json1 = response1.json()#<class 'dict'>
print(json1)

face = json1["result"]["face_list"][0]
print("性别:", face['gender']['type'])
print("年龄:", face['age'])
print("颜值:", face['beauty'])
print("脸型:", face['face_shape']['type'])
print("表情:", face['expression']['type'])

import os
os.startfile(filepath) #打开图片文件