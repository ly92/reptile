#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: garner

@file: test3.py

@time: 2017/11/15 18:15

@desc:

'''


import requests
from bs4 import BeautifulSoup
import lxml
import os
import time


class BeautifulPicture():
    def __init__(self):
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5'}
        self.web_url = 'http://www.jianshu.com/recommendations/users?utm_source=desktop&utm_medium=index-users'
        self.folder_path = '/Users/ly/Desktop/Python/picture'

    def request(self,url):
        r = requests.get(url)
        return r

    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
        else:
            print(path, '文件夹已经存在了，不再创建')

    def save_img(self, url, name):
        print('开始保存图片...%s'%name)
        img = self.request(url)
        time.sleep(5)
        print('开始保存文件')
        f = open(name, 'ab')
        f.write(img.content)
        print(name, '文件保存成功！')
        f.close()

    def get_pic(self):
        print('开始网页get请求')
        r = self.request(self.web_url)
        print('开始获取所有item')
        all_item = BeautifulSoup(r.text, 'lxml').find_all('div',class_='col-xs-8')
        print('开始创建文件夹')
        self.mkdir(self.folder_path)
        print('开始切换文件夹')
        os.chdir(self.folder_path)
        for item in all_item:
            img_url, name = self.getImgUrlAndName(item)
            self.save_img(img_url, name)

    def getImgUrlAndName(self, item):
        img = str(BeautifulSoup(str(item), 'lxml').find('img',class_='avatar',alt='180'))
        prePos = img.rstrip().index('//upload')
        sufPos = img.rstrip().index('imageMogr2') - 1
        img_url = 'http:' + img[prePos:sufPos]
        suffixPos = img_url.rindex('.')
        suffix = img_url[suffixPos:]
        if suffix.__len__() > 5:
            suffix = '.png'

        nameStr = BeautifulSoup(str(item), 'lxml').find('h4',class_='name')
        name = nameStr.text.strip() + suffix

        return img_url,name

beauty = BeautifulPicture()
beauty.get_pic()
