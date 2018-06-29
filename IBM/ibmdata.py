#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: garner

@file: ibmdata.py

@time: 2018/6/29 12:26

@desc:

'''



import requests
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from DatabaseManager import OperationDbInterface
from time import sleep
import re


class ImbData():
    def __init__(self):
        self.dataManager = OperationDbInterface()

    def operationGoods(self,url):
        driver = webdriver.PhantomJS()
        driver.get(url)
        source = driver.page_source

        name = '' #备件名
        cap = '' #表格描述
        one = '' #表格内容
        two = ''
        three = ''
        four = ''
        five = ''
        six = ''
        seven = ''
        eight = ''

        header = BeautifulSoup(str(source),'lxml').find('h1')
        name += str(header.text).strip()
        spans = BeautifulSoup(str(header),'lxml').find_all('span')
        for span in spans:
            name += str(span.text).strip()

        # print(name)
        sql = '''insert into ibmOne(one) values("%s")''' % (name)
        print(sql)
        self.dataManager.op_sql(sql)

        secDivs = BeautifulSoup(str(source),'lxml').find_all('div', class_='section')
        for secDiv in secDivs:
            tbody = BeautifulSoup(str(secDiv),'lxml').find('tbody', class_='tbody')

            if not tbody:
                continue


            tablecap = BeautifulSoup(str(secDiv), 'lxml').find('caption')
            span = BeautifulSoup(str(tablecap), 'lxml').find('span', class_='tablecap')
            cap = str(span.text).strip()
            sql = '''insert into ibmOne(one) values("%s")''' % (cap)
            print(sql)
            self.dataManager.op_sql(sql)

            trs = BeautifulSoup(str(tbody),'lxml').find_all('tr',class_='row')
            for tr in trs:
                tds = BeautifulSoup(str(tr),'lxml').find_all('td')
                for i in range(0,len(tds)):
                    tmp = ''
                    td = tds[i]
                    tmp = str(td.text).strip()
                    aTips = BeautifulSoup(str(td), 'lxml').find_all('a')
                    for a in aTips:
                        tmp += str(a.text).strip()
                    divs = BeautifulSoup(str(td), 'lxml').find_all('div')
                    for div in divs:
                        tmp += str(div.text).strip()
                    if i == 0:
                        one = tmp
                    elif i == 1:
                        two = tmp
                    elif i == 2:
                        three = tmp
                    elif i == 3:
                        four = tmp
                    elif i == 4:
                        five = tmp
                    elif i == 5:
                        six = tmp
                    elif i == 6:
                        seven = tmp
                    elif i == 7:
                        eight = tmp




                # print(one)
                # print(two)
                # print(three)
                # print(four)
                # print(five)
                # print(six)
                # print(seven)
                # print(eight)
                # print('-------------------------------------------------------------------------')
                sql = '''insert into ibmOne(one,two,three,four,five,six,seven,eight) values("%s","%s","%s","%s","%s","%s","%s","%s")''' % (one, two, three, four,five,six,seven,eight)
                print(sql)
                self.dataManager.op_sql(sql)


    def allGoodsList(self,url):
        self.operationGoods(url)



list = ImbData()

urlStr = '''
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/5888parts.htm;
'''

urlList = re.split('[;]',urlStr)
for url in urlList:
    print(url)
    list.allGoodsList(url+";")


'''
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/p7ecsparts_72x_74x.htm;
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/p7ecsparts_8202e4c.htm;
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/p7ecsparts_71x_73x.htm;
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/p7ecsparts_8231e1c.htm;
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/p7ecsp7ebsparts.htm;
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/p7ecsparts_75x_76x.htm;
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/p7ecsp7eanparts.htm;
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/p7ecsparts_9179mhc.htm;
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/p7ecsparts_79x.htm;
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/p7ecsparts_775.htm;
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/p7ecsp7reatparts.htm;
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/p7ecsp7reb8parts.htm;
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/p7ecsp7ecwparts.htm;
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/p7ecsp7ecxparts.htm;
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/p7ecsp7eblparts.htm;
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/5887parts.htm;
https://www.ibm.com/support/knowledgecenter/POWER7/p7ecs/5888parts.htm;
'''