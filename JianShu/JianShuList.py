#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: garner

@file: JianShuList.py

@time: 2018/1/4 18:50

@desc:

'''


# from JianShu.DatabaseManager import Operation
#
# class JianshuList(object):
#     def __init__(self):
#         self.dataManager = Operation()
#
#     def test(self):
#         self.dataManager.insert_item('yyyyyyy', 'ooooooooooo')
#
#
#
# jianshu = JianshuList()
# jianshu.test()

import requests
import xml
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from JianShu.DatabaseManager import Operation

class JianShuList():
    def __init__(self):
        self.dataManager = Operation()

    def request(self, url):
        driver = webdriver.PhantomJS()
        driver.get(url)
        return driver.page_source

    #提取博客标题和短内容
    def operationBlog(self):
        source = self.request('https://www.jianshu.com/u/82854a3500fc')
        content_list = BeautifulSoup(source, 'lxml').find('div', id='list-container')
        ul_list = BeautifulSoup(str(content_list), 'lxml').find('ul', class_='note-list')
        all_lis = BeautifulSoup(str(ul_list), 'lxml').find_all('li')
        for li in all_lis:
            name = BeautifulSoup(str(li), 'lxml').find('a', class_='title').text.strip()
            detail = BeautifulSoup(str(li), 'lxml').find('p', class_='abstract').text.strip()
            self.dataManager.insert_item(name,detail)

    #获取作者ID
    # def getAuthorId(self):



jianshu = JianShuList()
jianshu.getAuthorId()

'''
https://www.jianshu.com/users/82854a3500fc
https://www.jianshu.com/users/neLruC
https://www.jianshu.com/users/3aa040bf0610
https://www.jianshu.com/users/5462ec6828f6
https://www.jianshu.com/users/78f970537a5e
https://www.jianshu.com/users/5SqsuF
https://www.jianshu.com/users/55b597320c4e
https://www.jianshu.com/users/c5580cc1c3f4
https://www.jianshu.com/users/b52ff888fd17
https://www.jianshu.com/users/74307f7c1d61
https://www.jianshu.com/users/4632c37c9fee
https://www.jianshu.com/users/d88ac7d50d72
https://www.jianshu.com/users/2cc2a1362992
https://www.jianshu.com/users/7afd62d4284a
https://www.jianshu.com/users/12532d36e4da
https://www.jianshu.com/users/7bf8f8f0a172
https://www.jianshu.com/users/93666dd4205b
https://www.jianshu.com/users/e9dd67d5e1b0
https://www.jianshu.com/users/2482b41ccb37
https://www.jianshu.com/users/Rx9gFA
https://www.jianshu.com/users/034fbfcf5e9f
https://www.jianshu.com/users/2LSzkz
https://www.jianshu.com/users/3a32d073a21d
https://www.jianshu.com/users/017d943147bb
'''
