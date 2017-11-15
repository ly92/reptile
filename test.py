#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: garner

@file: test.py

@time: 2017/11/15 14:56

@desc:

'''


import requests
from bs4 import BeautifulSoup
import lxml
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#自动用简书搜索Python
# driver = webdriver.Safari()
# driver.get("http://www.jianshu.com")
# print(driver.title)
# # assert "Python" in driver.title
# elem = driver.find_element_by_name("q")#获取搜索框
# elem.clear()
# elem.send_keys("python")
# elem.send_keys(Keys.RETURN)
# print(driver.page_source)
# assert "No results found." not in driver.page_source
# driver.close()






class BeautifulPicture():
    def __init__(self):
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5'}
        self.web_url = 'http://www.jianshu.com/recommendations/users?utm_source=desktop&utm_medium=index-users'
        self.folder_path = '/Users/ly/Desktop/python/picture'

    def request(self,url):
        driver = webdriver.PhantomJS()
        driver.get(url)
        self.click_more(driver,5)
        return driver.page_source

    def click_more(self,driver,times):
        for i in range(times):
            print("开始执行第", str(i + 1),"次点击操作")
            #复合类的名称不允许
            # elem = driver.find_element_by_class_name("btn btn-danger load-more-btn")
            elem = driver.find_element_by_class_name("load-more-btn")
            elem.click()
            time.sleep(5)

    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
            return True
        else:
            print(path, '文件夹已经存在了，不再创建')
            return False

    def get_pic(self):
        print('开始网页get请求')
        r = self.request(self.web_url)
        print('开始获取所有item')
        all_item = BeautifulSoup(r, 'lxml').find_all('div',class_='col-xs-8')
        print('开始创建文件夹')
        is_new_folder =  self.mkdir(self.folder_path)
        print('开始切换文件夹')
        os.chdir(self.folder_path)
        for item in all_item:
            img_url, name = self.getImgUrlAndName(item)
            if is_new_folder:
                self.save_img(img_url, name)
            else:
                all_files = os.listdir(self.folder_path)
                if name not in all_files:
                    self.save_img(img_url, name)


    def save_img(self, url, name):
        print('开始保存图片...%s'%name)
        img = requests.get(url)
        time.sleep(5)
        print('开始保存文件')
        f = open(name, 'ab')
        f.write(img.content)
        print(name, '文件保存成功！')
        f.close()

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
