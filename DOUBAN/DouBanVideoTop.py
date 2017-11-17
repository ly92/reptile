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


class VieoInfoList():
    def __init__(self):
        self.web_url = "https://movie.douban.com/top250"
        self.dataManager = OperationDbInterface()

    def getPageSource(self, source_url):
        driver = webdriver.PhantomJS()
        driver.get(source_url)
        #
        return driver.page_source

    def getAllItems(self):
        source = ''
        for i in range(10):
            webUrl = "https://movie.douban.com/top250?start=%d&filter="%(i*25)
            source = self.getPageSource(webUrl)
            all_items = BeautifulSoup(source, 'lxml').find_all('div', class_='item')
            # time.sleep(10)
            for item in all_items:
                self.operateItem(item)


    def getDetailInfo(self, url):
        source = self.getPageSource(url)
        infoDiv = BeautifulSoup(source, 'lxml').find('div', id='wrapper')
        infoDiv = BeautifulSoup(str(infoDiv), 'lxml').find('div', id='content')
        # 名称
        # video_name = BeautifulSoup(str(infoDiv), 'lxml').find('span', property='v:itemreviewed').text
        # 年份
        show_year = ''
        yearSpan = BeautifulSoup(str(infoDiv), 'lxml').find('span', class_='year')
        if yearSpan == None:
            return '', '', '', ''
        if yearSpan.text != '':
            show_year = yearSpan.text
        show_year = show_year.replace('(','')
        show_year = show_year.replace(')', '')

        # 导演
        director = ''
        allDirectors = BeautifulSoup(str(infoDiv),'lxml').find_all('a', rel='v:directedBy')
        for dir in allDirectors:
            director += str(dir.text).strip() + ' '
        director.rstrip()
        #演员
        actor = ''
        allActors = BeautifulSoup(str(infoDiv),'lxml').find_all('a', rel='v:starring')
        for act in allActors:
            actor += str(act.text).strip() + ' '
        actor.rstrip()

        # 简介
        intro = ''
        introDiv = BeautifulSoup(source, 'lxml').find('div', class_='indent', id='link-report')
        allSpans = BeautifulSoup(str(introDiv), 'lxml').find_all('span')
        for span in allSpans:
            if span.text != '':
                if span.text.__len__() > 100:
                    mutiList = re.compile(r"\n").split(span.text.strip())
                    for strs in mutiList:
                        intro += str(strs).strip()
            if intro.__len__() > 100:
                if intro.endswith('(展开全部)') or intro.endswith('...'):
                    intro = ''
                else:
                    break

        intro = intro.replace('"', '\\\"')
        intro = intro.replace('“', '\\\"')
        intro = intro.replace('”', '\\\"')
        return show_year,director,actor,intro

    def operateItem(self, item):
        picDiv = BeautifulSoup(str(item), 'lxml').find('div', class_='pic')
        # print(picDiv)
        # 排名int
        rank = BeautifulSoup(str(picDiv), 'lxml').find('em').text.strip()

        sqi = 'select * from videos_copy where rank=%s'%rank
        result = self.dataManager.select_one(sqi)
        if result != None:
            return
        # 连接
        intro_link = BeautifulSoup(str(picDiv), 'lxml').find('a')['href']
        # 图片
        picture_link = BeautifulSoup(str(picDiv), 'lxml').find('img')['src']
        # 是否可播放
        playable = 0
        hdDiv = BeautifulSoup(str(item), 'lxml').find('div', class_='hd')
        play = BeautifulSoup(str(hdDiv), 'lxml').find_all('span', class_='playable')
        for playItem in play:
            playable = 1

        bdDiv = BeautifulSoup(str(item), 'lxml').find('div', class_='bd')
        # 评价人数
        valuator_num = BeautifulSoup(str(bdDiv), 'lxml').find('span', class_='', property='').text
        valuator_num = valuator_num.replace('人评价', '')
        # 短简介
        shot_intro = ''
        shortSpan = BeautifulSoup(str(bdDiv), 'lxml').find('span', class_='inq')
        if shortSpan != None:
            shot_intro = shortSpan.text.strip()

        # 评分
        grade = BeautifulSoup(str(bdDiv), 'lxml').find('span', class_='rating_num').text

        # 年份int
        show_year = ''
        # 名称string
        video_name = ''
        # 导演
        director = ''
        # 演员
        actor = ''
        # 简介
        intro = ''
        # 简介
        show_year, director, actor, intro = self.getDetailInfo(intro_link)
        if show_year == '' and director == '' and actor == '' and intro == '':
            show_year = '0000'
            director = 'superman'
            actor = 'superman'
            intro = 'superintro'
            # return

        # 别名array
        other_name = ''
        all_names = BeautifulSoup(str(hdDiv), 'lxml').find_all('span', class_='title')
        i = 1
        for nameSpan in all_names:
            if i == 1:
                video_name = nameSpan.text.strip()
                # sqi = 'select * from videos where rank=%s'%rank
                # result = self.dataManager.select_one(sqi)
                # if result == None:
                #     return
                # sql = "update videos set video_name='%s' where rank=%s" % (video_name,rank)
                # result2 = self.dataManager.op_sql(sql)
            else:
                other_name += nameSpan.text.strip()
            i += 1

        other_name += BeautifulSoup(str(hdDiv), 'lxml').find('span', class_='other').text
        other_name = other_name.replace('/','').strip()
        other_name = str(other_name)
        video_name = video_name.replace('/','').strip()
        mutiStr = BeautifulSoup(str(bdDiv), 'lxml').find('p', class_='').text.strip()
        mutiList = re.compile(r"\n").split(mutiStr)
        preYear = str(mutiList[1]).strip()
        preList = preYear.split('/')
        # 国家string
        nationality = ''
        # 类别
        video_sort = ''
        j = 1
        for strs in preList:
            if j == 2:
                nationality = str(strs).strip()
            else:
                video_sort = str(strs).strip()
            j += 1

        # print('rank=%s,video_name=%s,other_name=%s,director=%s,show_year=%s,nationality=%s,'
        #       'video_sort=%s,grade=%s,valuator_num=%s,shot_intro=%s,intro_link=%s ,picture_link=%s ,'
        #       'playable=%s,intro=%s' % (rank, video_name, other_name, director, show_year, nationality, video_sort,
        #                                 grade, valuator_num, shot_intro, intro_link, picture_link, playable, intro))

        result = self.dataManager.insert_item(int(rank), video_name, other_name,
                                              director, int(show_year), nationality, video_sort, float(grade),
                                              int(valuator_num), shot_intro, intro_link, intro, playable, actor)
        print(result)

    #去重
    def removeRepetition(self):
        rankArr = []
        idArr = []
        secrchArr = self.dataManager.select_all('select * from videos')
        for item in secrchArr:
            idArr.append(item['id'])
            if rankArr.__contains__(item['rank']):
                deleteSql = 'delete from videos_copy where id=%d'%item['id']
                result = self.dataManager.op_sql(deleteSql)
                print(result)
            else:
                rankArr.append(item['rank'])



videoInfo = VieoInfoList()
videoInfo.getAllItems()
# videoInfo.removeRepetition()



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
        #简介
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

        mutiStr = BeautifulSoup(str(bdDiv), 'lxml').find('p', class_='').text.strip()
        mutiList = re.compile(r"\n").split(mutiStr)
        preDirector = str(mutiList[0]).strip()
        preYear = str(mutiList[1]).strip()
        startPos = preDirector.index('导演:') + 3
        endPos = preDirector.index('主')
        # 导演
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

        print('rank=%s,video_name=%s,other_name=%s,director=%s,show_year=%s,nationality=%s,'
              'video_sort=%s,grade=%s,valuator_num=%s,shot_intro=%s,intro_link=%s ,picture_link=%s ,'
              'playable=%s,intro=%s' %(rank,name,other_name,director,show_year,nationality,video_sort,
                                       grade,valuator_num,shot_intro,intro_link,picture_link,playable,intro))


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


        # result = self.dataManager.insert_item(int(rank), name, other_name,
        # director, int(show_year), nationnality, video_sort, int(grade), 3.5,
        # int(valuator_num), shot_intro, intro_link, 'text')
        # print(result)

# vide_list = VieoList()
# vide_list.getAllItems()
# vide_list.getDetailInfo('https://movie.douban.com/subject/1307914/')

