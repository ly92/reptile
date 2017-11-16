#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: garner

@file: DouBanVideoTop.py

@time: 2017/11/16 18:04

@desc:

'''

'''
1页25个
https://movie.douban.com/top250    
https://movie.douban.com/subject/1292052/
https://movie.douban.com/top250?start=75&filter=
https://movie.douban.com/top250?start=150&filter=
'''


from DatabaseManager import OperationDbInterface
from bs4 import BeautifulSoup
import lxml
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


class VieoList():
    def __init__(self):
        self.web_url = "https://movie.douban.com/top250"
        self.dataManager = OperationDbInterface()

    def getPageSource(self,page):
        driver = webdriver.PhantomJS()
        driver.get(self.web_url)
        #
        return driver.page_source

    def getAllItems(self):
        source = self.getPageSource(1)
        all_items = BeautifulSoup(source, 'lxml').find_all('div',class_='item')
        for item in all_items:
            self.operateItem(item)

    def operateItem(self,item):
        print(str(item))
        picDiv = BeautifulSoup(str(item), 'lxml').find('div', class_='pic')
        print(picDiv)
        #排名int
        rank = BeautifulSoup(str(picDiv), 'lxml').find('em').text.strip()
        # 连接
        intro_link = BeautifulSoup(str(picDiv), 'lxml').find('a')['href']
        #图片
        picture_link = BeautifulSoup(str(picDiv), 'lxml').find('img')['src']

        hdDiv = BeautifulSoup(str(item), 'lxml').find('div', class_='hd')
        #名称string
        name = ''
        # 别名array
        other_name = ''
        all_names = BeautifulSoup(str(hdDiv), 'lxml').find_all('span', class_='title')
        i = 1
        for nameSpan in all_names:
            if i == 1:
                name = nameSpan.text
            else:
                other_name += nameSpan.text
            i += 1
        other_name += BeautifulSoup(str(hdDiv), 'lxml').find_all('span', class_='other').text
        #是否可播放
        playable = False
        play = BeautifulSoup(str(hdDiv), 'lxml').find_all('span', class_='playable')
        if play.text == '[可播放]' or play.text.strip().__len__ > 0:
            playable = True

        bdDiv = BeautifulSoup(str(item), 'lxml').find('div', class_='bd')
        #导演  导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...
        preDirector = BeautifulSoup(str(bdDiv), 'lxml').find('p', class_='').text
        startPos = preDirector.index('导演:') + 3
        endPos = preDirector.index('主演:')
        director = preDirector[startPos:endPos].strip()

        endPos2 = preDirector.index('...') + 4
        beReplaced = preDirector[:endPos2]
        preYear = preDirector.replace(beReplaced,'')
        preYear = preYear.replace('"','').strip()
        preList = preYear.split('/')
        # 年份int
        show_year = ''
        # 国家string
        nationnality = ''
        # 类别
        video_sort = ''
        j = 1
        for str in preList:
            if j == 1:
                show_year = str.strip()
            elif j == 2:
                nationnality = str.strip()
            else:
                video_sort = str.strip()
            i += 1
        #评分
        grade = BeautifulSoup(str(bdDiv), 'lxml').find('span', class_='rating_num').text
        #星级
        # star_level
        #评价人数
        valuator_num = BeautifulSoup(str(bdDiv), 'lxml').find('span', class_='').text
        valuator_num = valuator_num[:3]
        #短简介
        shot_intro = BeautifulSoup(str(bdDiv), 'lxml').find('span', class_='inq').text

#rank,video_name,other_name,director,show_year,nationality,video_sort,grade,star_level,valuator_num,shot_intro,intro_link,intro):
        result = self.dataManager.insert_item(int(rank), name, other_name, director, int(show_year), nationnality, video_sort, int(grade), 3.5, int(valuator_num), shot_intro, intro_link, 'text')
        print(result)


vide_list = VieoList()
vide_list.getAllItems()
