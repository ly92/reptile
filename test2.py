#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: garner

@file: test2.py

@time: 2017/11/15 16:48

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
        self.web_url = 'http://www.jianshu.com/p/8e475552e169'
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
        file_name = name + '.png'
        print('开始保存文件')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, '文件保存成功！')
        f.close()

    def get_pic(self):
        print('开始网页get请求')
        r = self.request(self.web_url)
        print('开始获取所有img标签')
        all_img = BeautifulSoup(r.text, 'lxml').find_all('img',alt='')
        print('开始创建文件夹')
        self.mkdir(self.folder_path)
        print('开始切换文件夹')
        os.chdir(self.folder_path)
        i = 1
        for img in all_img:
            img_url = img['src']
            # img_str = 'CreateDeveloperAccount' + str(i)
            self.save_img(img_url,str(i))
            i += 1



beauty = BeautifulPicture()
beauty.get_pic()