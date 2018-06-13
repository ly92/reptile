#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: mxonline

@file: IbmTestOne.py

@time: 2018/6/11 下午10:35

@desc:

'''


import requests
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from DatabaseManager import OperationDbInterface
from time import sleep



class ImbData():
    def __init__(self):
        self.dataManager = OperationDbInterface()

    def request(self, url):
        driver = webdriver.PhantomJS()
        driver.get(url)
        iframe = driver.find_element_by_tag_name('iframe')
        driver.switch_to.frame(iframe)
        soup = BeautifulSoup(driver.page_source,"html.parser")
        return soup


    def operationGoods(self,url):
        source = self.request(url)
        secDivs = BeautifulSoup(str(source),'lxml').find_all('div', class_='section')
        tbody = BeautifulSoup(str(secDivs[2]),'lxml').find('tbody', class_='tbody')
        trs = BeautifulSoup(str(tbody),'lxml').find_all('tr',class_='row')
        # print(trs)
        for tr in trs:
            tds = BeautifulSoup(str(tr),'lxml').find_all('td')
            one = ''
            two = ''
            three = ''
            four = ''
            if len(tds) == 3:
                two = str(tds[0].text).strip()
                three = str(tds[1].text).strip()
                four = str(tds[2].text).strip()
                aTips = BeautifulSoup(str(tds[2]),'lxml').find_all('a')
                for a in aTips:
                    four += str(a.text).strip()
                divs = BeautifulSoup(str(tds[2]),'lxml').find_all('div')
                for div in divs:
                    four += str(div.text).strip()
            elif len(tds) == 4:
                one = str(tds[0].text).strip()
                two = str(tds[1].text).strip()
                three = str(tds[2].text).strip()
                four = str(tds[3].text).strip()
                aTips = BeautifulSoup(str(tds[3]), 'lxml').find_all('a')
                for a in aTips:
                    four += str(a.text).strip()
                divs = BeautifulSoup(str(tds[3]), 'lxml').find_all('div')
                for div in divs:
                    four += str(div.text).strip()
            sql = '''insert into ibmOne(one,two,three,four) values("%s","%s","%s","%s")''' % (one, two, three, four)
            print(sql)
            self.dataManager.op_sql(sql)


    def allGoodsList(self):
        url = "https://www.ibm.com/support/knowledgecenter/POWER8/p8eiq/p8eiq_8001_22c_parts.htm"
        self.operationGoods(url)



list = ImbData()
# list.operationGoods()
list.allGoodsList()
# list.removeRepetition()




