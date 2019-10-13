#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import requests
import urllib.request
from bs4 import BeautifulSoup
import json

file_path="/Users/zixincai/github/python_learn/Bing_photo/"
if  os.path.exists(file_path) :
    print("文件夹存在")
else:
    os.makedirs(file_path)

Bing_photo_api = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
#Bing_photo_api = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=3"
html_data = urllib.request.urlopen(Bing_photo_api).read()
# print(type(html_data))
html=html_data.decode('utf-8')
dict_json=json.loads(html)
list_photo=dict_json['images']
dict_three=list_photo[0]
url=dict_three['url']
url_photo='http://cn.bing.com'+url
dict_four=str(dict_three['copyright'])
dict_five=dict_four[0:8]
print(dict_five)

Photo_name=dict_five+dict_three['startdate']+'.jpg'

full_path = file_path + Photo_name
print(full_path)
img_data=urllib.request.urlopen(url_photo).read()

f = open(full_path,'wb')
f.write(img_data)
f.close()

print("下载成功")



