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
import re


class VieoList():
    def __init__(self):
        self.web_url = "https://movie.douban.com/top250"
        # self.dataManager = OperationDbInterface()

    def getPageSource(self,source_url):
        driver = webdriver.PhantomJS()
        driver.get(source_url)
        #
        return driver.page_source

    def getAllItems(self):
        source = self.getPageSource(self.web_url)
        all_items = BeautifulSoup(source, 'lxml').find_all('div',class_='item')
        for item in all_items:
            self.operateItem(item)

    def operateItem(self,item):
        picDiv = BeautifulSoup(str(item), 'lxml').find('div', class_='pic')
        # print(picDiv)
        #排名int
        rank = BeautifulSoup(str(picDiv), 'lxml').find('em').text.strip()
        # 连接
        intro_link = BeautifulSoup(str(picDiv), 'lxml').find('a')['href']
        intro = self.getDetailInfo(intro_link)
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
        other_name += BeautifulSoup(str(hdDiv), 'lxml').find('span', class_='other').text
        #是否可播放
        playable = False
        play = BeautifulSoup(str(hdDiv), 'lxml').find_all('span', class_='playable')
        for playItem in play:
            playable = True

        bdDiv = BeautifulSoup(str(item), 'lxml').find('div', class_='bd')
        #导演
        mutiStr = BeautifulSoup(str(bdDiv), 'lxml').find('p', class_='').text.strip()
        mutiList = re.compile(r"\n").split(mutiStr)
        preDirector = str(mutiList[0]).strip()
        preYear = str(mutiList[1]).strip()
        startPos = preDirector.index('导演:') + 3
        endPos = preDirector.index('主')
        director = preDirector[startPos:endPos].strip()
        preList = preYear.split('/')
        # 年份int
        show_year = ''
        # 国家string
        nationality = ''
        # 类别
        video_sort = ''
        j = 1
        for strs in preList:
            if j == 1:
                show_year = strs.strip()
            elif j == 2:
                nationality = strs.strip()
            else:
                video_sort = strs.strip()
            j += 1
        #评分
        grade = BeautifulSoup(str(bdDiv), 'lxml').find('span', class_='rating_num').text
        #星级
        # star_level
        #评价人数
        valuator_num = BeautifulSoup(str(bdDiv), 'lxml').find('span', class_='',property='').text
        valuator_num = valuator_num.replace('人评价','')
        #短简介
        shot_intro = BeautifulSoup(str(bdDiv), 'lxml').find('span', class_='inq').text

        print('rank=%s,video_name=%s,other_name=%s,director=%s,show_year=%s,nationality=%s,video_sort=%s,grade=%s,valuator_num=%s,shot_intro=%s,intro_link=%s ,picture_link=%s ,playable=%s,intro=%s' %(rank,name,other_name,director,show_year,nationality,video_sort,grade,valuator_num,shot_intro,intro_link,picture_link,playable,intro))


    def getDetailInfo(self,url):
        source = self.getPageSource(url)
        introDiv = BeautifulSoup(source,'lxml').find('div',class_='indent',id='link-report')
        allSpans = BeautifulSoup(str(introDiv), 'lxml').find_all('span')
        result = ''
        for span in allSpans:
            if span.text != '':
                if span.text.__len__() > 50:
                    mutiList = re.compile(r"\n").split(span.text.strip())
                    for strs in mutiList:
                        result += str(strs).strip()
        return result

#rank,video_name,other_name,director,show_year,nationality,video_sort,grade,star_level,valuator_num,shot_intro,intro_link,intro):
        # result = self.dataManager.insert_item(int(rank), name, other_name, director, int(show_year), nationnality, video_sort, int(grade), 3.5, int(valuator_num), shot_intro, intro_link, 'text')
        # print(result)



vide_list = VieoList()
vide_list.getAllItems()
# vide_list.getDetailInfo('https://movie.douban.com/subject/1307914/')
