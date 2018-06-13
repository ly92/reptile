#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: mxonline

@file: GoodsList.py

@time: 2018/5/24 下午10:55

@desc:

'''

import requests
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from DatabaseManager import OperationDbInterface
from time import sleep


class GoodsList():
    def __init__(self):
        self.dataManager = OperationDbInterface()

    def request(self, url):
        driver = webdriver.PhantomJS()
        driver.get(url)
        return driver.page_source


    def operationGoods(self,url):
        source = self.request(url)
        contentDiv = BeautifulSoup(source, 'lxml').find('div', class_='productcontent')
        all_lis = BeautifulSoup(str(contentDiv), 'lxml').find_all('li')
        for li in all_lis:
            a = BeautifulSoup(str(li), 'lxml').find('a', class_='a_hui')
            name = str(a.get('title')).strip()
            goodsId = str(a.get('href')).replace('productlist.php?pid=','').strip()
            # print(name)
            # print(goodsId)
            # print('-----------------------------')

            # result = self.dataManager.insert_item(name, int(goodsId))
            # print(result)

            secrchArr = self.dataManager.select_all('select goods_id from real_goods_list')
            if secrchArr.__contains__({'goods_id': int(goodsId)}) is False:
                result = self.dataManager.insert_item(name, int(goodsId))
                print(result)
            # if secrchArr.__contains__({'goods_id': int(goodsId)}):
            #     print(goodsId)
            #     return
            # else:
            #     result = self.dataManager.insert_item(name, int(goodsId))
            #     print(result)


    def allGoodsList(self):#291~1434未获取
        for i in range(1,3):
            print(i)
            url = "http://www.tradeunix.com/product.php?page=%d&cid=1&fid=1&bid=&keywords=&search_sna=&search_name="%(i)
            print(url)
            self.operationGoods(url)

            # sleep(2)

    # 去重
    def removeRepetition(self):
        rankArr = []
        idArr = []
        secrchArr = self.dataManager.select_all('select * from real_goods_list')
        for item in secrchArr:
            idArr.append(item['goods_id'])
            if rankArr.__contains__(item['goods_id']):
                deleteSql = 'delete from real_goods_list where goods_id=%d' % item['goods_id']
                result = self.dataManager.op_sql(deleteSql)
                print(result)
            else:
                rankArr.append(item['goods_id'])

list = GoodsList()
# list.operationGoods()
list.allGoodsList()
# list.removeRepetition()


# http://www.tradeunix.com/product.php?page=2&cid=1&fid=1&bid=&keywords=&search_sna=&search_name=