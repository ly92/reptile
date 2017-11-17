#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: garner

@file: BaiDuRecommendMv.py

@time: 2017/11/17 16:34

@desc:

'''



from DatabaseManager import OperationDbInterface
from bs4 import BeautifulSoup
import lxml
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import re


class MVInfoList():
    def __init__(self):
        self.web_url = "http://music.baidu.com/mv"
        self.dataManager = OperationDbInterface()

    def getPageSource(self, source_url):
        driver = webdriver.PhantomJS()
        driver.get(source_url)
        return driver.page_source

    def getAllItems(self):
        source = self.getPageSource(self.web_url)
        all_items = BeautifulSoup(source, 'lxml').find_all('a', class_='mv-icon', target='_blank')
        for item in all_items:
            detailUrl = 'http://music.baidu.com' + item['href']
            # print(detailUrl)
            self.getDetailInfo(detailUrl)


    def getDetailInfo(self, url):
        detailSource = self.getPageSource(url)
        sourceStr = str(detailSource)
        startPos = sourceStr.index('videoUrl=') + 9
        endPos = sourceStr.index('.mp4') + 4
        videoUrl = sourceStr[startPos:endPos]
        print('\"' + videoUrl + '\"')
        # self.getVideoUrl(sourceStr[endPos:])


    def getVideoUrl(self,source):
        startPos = source.index('\"file_link\":\"') + 13
        endPos = source.index('.mp4') + 4
        if startPos == None:
            return
        if endPos == None:
            return

        videoUrl = source[startPos:endPos]
        if videoUrl == None:
            return

        videoUrl = videoUrl.replace('\\','')
        subSource = source[endPos:]
        if videoUrl.__len__() > 10:
            self.getVideoUrl(subSource)
            print('\"' + videoUrl + '\"')




mvDriver = MVInfoList()
mvDriver.getAllItems()
# mvDriver.getDetailInfo('')

'''
http://musicdata.baidu.com/data2/video/566414577/356acf8f3ea388f9b212263db7b6d315/566414577.mp4
http://musicdata.baidu.com/data2/video/566404453/209f8156aef486096810324fcc2e2b64/566404453.mp4
http://musicdata.baidu.com/data2/video/566353844/ae89a0b5618bd77e39d1503f2ff1eec2/566353844.mp4
http://musicdata.baidu.com/data2/video/566296095/0ab6259a6fe6476dc1064e4dbd76a8a6/566296095.mp4
http://musicdata.baidu.com/data2/video/566295833/04ab59da9c679b1d564d004ebe56d511/566295833.mp4
http://musicdata.baidu.com/data2/video/566268552/3eaba664b26021cd77f2e35aa9c08bd4/566268552.mp4
http://musicdata.baidu.com/data2/video/566004777/a49845a492eb05b94bb001e10ff915fa/566004777.mp4
http://musicdata.baidu.com/data2/video/566151616/0cfbcd79e621661aff5fc5c5d7cbaa8a/566151616.mp4
http://musicdata.baidu.com/data2/video/566050530/82e3ce14df9831237a2adbd130a30d83/566050530.mp4
http://musicdata.baidu.com/data2/video/566114598/4d6b6fdc573ff7b2604c8aab848222f9/566114598.mp4
http://musicdata.baidu.com/data2/video/566052304/d81ce4b3bcb20e45ba653b9dbf4771b4/566052304.mp4
http://musicdata.baidu.com/data2/video/566051516/01bde2d9036f3446f01d8c8715078a8f/566051516.mp4
http://musicdata.baidu.com/data2/video/566052304/d81ce4b3bcb20e45ba653b9dbf4771b4/566052304.mp4
http://musicdata.baidu.com/data2/video/565986152/fa888c7133dd62d39f3989891ae926ee/565986152.mp4
http://musicdata.baidu.com/data2/video/565967842/eddcf892b35e9b2c9c0f62dd0db3a86c/565967842.mp4
http://musicdata.baidu.com/data2/video/565860269/832856d58c1c51808ecfe065a2ab8d64/565860269.mp4
http://musicdata.baidu.com/data2/video/565864961/e926c196eb6273e0e54d08e2aa02a5a9/565864961.mp4
http://musicdata.baidu.com/data2/video/565879588/13f423b562249570501a1bf1e0e7c907/565879588.mp4
http://musicdata.baidu.com/data2/video/565372149/6d70dd75d0b9634c898676c289251b03/565372149.mp4
http://musicdata.baidu.com/data2/video/560520688/60c10b32f626c2c1e4feed8ab6ad0aa7/560520688.mp4
http://musicdata.baidu.com/data2/video/565502630/00bc24745f3004efc66763c321c89475/565502630.mp4
http://musicdata.baidu.com/data2/video/565003928/a9a1efc48d3a465d79d1683cb15b440e/565003928.mp4
http://musicdata.baidu.com/data2/video/564186988/c01969bf0f1c9587f36485bcc8040440/564186988.mp4
http://musicdata.baidu.com/data2/video/564384224/c32c66f01e9115e02f987587ec2b8c01/564384224.mp4
http://musicdata.baidu.com/data2/video/564072004/5208efd0c72531eb064664c1532749ed/564072004.mp4
'''