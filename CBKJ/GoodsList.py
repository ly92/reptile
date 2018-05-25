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


class GoodsList():
    def __init(self):
        self.dataManager = OperationDbInterface()

    def request(self, url):
        driver = webdriver.PhantomJS()
        driver.get(url)
        return driver.page_source


    def operationGoods(self):
        source = self.request('http://www.tradeunix.com/product.php?page=1&cid=&fid=&bid=&keywords=&search_sna=&search_name=')
        contentDiv = BeautifulSoup(source, 'lxml').find('div', class_='productcontent')
        all_lis = BeautifulSoup(str(contentDiv), 'lxml').find_all('li')
        for li in all_lis:
            a = BeautifulSoup(str(li), 'lxml').find('a', class_='a_hui')
            name = str(a.get('title')).strip()
            goodsId = str(a.get('href')).replace('productlist.php?pid=','').strip()
            # print(name)
            # print(goodsId)
            # print('-----------------------------')

            result = self.dataManager.insert_item(name,int(goodsId))
            print(result)




list = GoodsList()
list.operationGoods()