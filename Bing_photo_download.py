#!/usr/bin/python
# -*- coding: utf-8 -*-

#检查文件夹是否存在，如果不存在就创建
#之后下载图片到本地

import os
import requests
import urllib.request
from bs4 import BeautifulSoup

file_path="/Users/zixincai/github/python_learn/Bing_photo"
if  os.path.exists(file_path) :
    print("文件夹存在")
else:
    os.makedirs(file_path)


# url="https://www.bing.com/th?id=OHR.IAFtricolor_EN-IN2504926029_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp"
# img_data=urllib.request.urlopen(url).read()
# img_name=url

# f = open("1.jpg",'wb')
# f.write(img_data)
# f.close()

# print("下载成功")


# bing_url="https://www.bing.com/"
# url_data=urllib.request.urlopen(bing_url).read()
# bs0bj=BeautifulSoup(url_data,"lxml")
# urList=bs0bj.findall("href")
# for ul in ulList:
#     print(ul)



sourceLink = "https://cn.bing.com"
html = urllib.request.urlopen(sourceLink).read()
bsObj = BeautifulSoup(html,'lxml')
t1 = bsObj.find_all('link')
t2=str(t1[0])
html_link=sourceLink+t2[23:84]

file_path="/Users/zixincai/github/python_learn/Bing_photo/"
Photo_name=t2[34:48]
Full_name=file_path+Photo_name+".jpg"
img_data=urllib.request.urlopen(html_link).read()


f = open(Full_name,'wb')
f.write(img_data)
f.close()

print("下载成功")




