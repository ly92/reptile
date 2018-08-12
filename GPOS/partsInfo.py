#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: mxonline

@file: partsInfo.py

@time: 2018/7/30 上午9:30

@desc:

'''




import requests
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from DatabaseManager import OperationDbInterface
from time import sleep
import re


class PartsInfo():
    def __init__(self):
        self.dataManager = OperationDbInterface()

    def operationGoods(self,url,parts_id):
        options = Options()
        options.add_argument('-headless')
        driver = Firefox(executable_path='/usr/local/bin/geckodriver', firefox_options=options)
        driver.get(url)
        source = driver.page_source
        driver.close()

        # driver = webdriver.PhantomJS()
        # driver.get(url)
        # source = driver.page_source
        # print(source)

        #配件
        info_name = ''
        info_desc = ''

        #配件关联整机
        machine_name = ''
        machine_url = ''

        # print(source)


        contentDiv = BeautifulSoup(str(source),'lxml').find('div',id='contentPH_partDetails')
        table = BeautifulSoup(str(contentDiv),'lxml').find('table',class_='ptmtb')
        tbody = BeautifulSoup(str(table),'lxml').find('tbody')
        trs = BeautifulSoup(str(tbody),'lxml').find_all('tr')
        isCommon = False
        for tr in trs:
            tds = BeautifulSoup(str(tr),'lxml').find_all('td')
            if len(tds) == 1:
                if 'ppSub2' in tds[0]['class']:
                    isCommon = True
                else :
                    isCommon = False
            else:
                if isCommon:
                    aList = BeautifulSoup(str(tds[1]),'lxml').find_all('a',target='_blank')
                    for a in aList:
                        machine_name = ''
                        machine_url = ''
                        machine_name = str(a.text).strip()
                        machine_url = a['href']
                        pM_sql = '''insert into qxf_kfpartsmachine(parts_id,machine_name,machine_url) values(%d,"%s","%s")''' % (
                        parts_id, machine_name, machine_url)
                        result1 = self.dataManager.op_sql(pM_sql)
                        if result1:
                            print('true' + str(parts_id))
                        else:
                            print('-------------------------------------------------------------------------')
                            print(pM_sql)
                            print('false' + str(parts_id))
                else:
                    info_name = ''
                    info_desc = ''
                    info_name = str(tds[0].text).strip().replace('"','')
                    info_desc = str(tds[1].text).strip().replace('"','')
                    parts_sql = '''insert into qxf_kfpartsinfo(parts_id,info_name,info_desc) values(%d,"%s","%s")''' % (parts_id, info_name, info_desc)
                    result2 = self.dataManager.op_sql(parts_sql)
                    if result2:
                        print('common-true' + str(parts_id))
                    else:
                        print('-------------------------------------------------------------------------')
                        print(parts_sql)
                        print('common-false' + str(parts_id))



info = PartsInfo()
partses = info.dataManager.select_all('select * from qxf_kftemp where parts_id > 100583 AND parts_id < 100801')
for parts in partses:
    url = parts['parts_url']
    parts_id =  parts['parts_id']

    # print(parts_id)
    print(url)

    # info.operationGoods(url,parts_id)



# info.dataManager.op_sql('delete from qxf_kfpartsmachine where id != 0')



# sql1 = '''insert into qxf_kfpartsmachine(parts_id,machine_name,machine_url) values(81332,"HP StorageWorks MSL5026 Tape Library 293472-B21/293472-B22/293472-B23/293472-B24/293472-B25/293472R-B21/293472R-B22/293472R-B23/293472R-B24/293472R-B25/293473-B21/293473-B22/293473R-B21/293473R-B22/302511-B21/302511-B22/302511R-B21/302511R-B22/302512-B21/302512-B22/302512R-B21/302512R-B22/231821-B21/231821-B22/231821R-B22/231822-B21/231822-B22/231891-B21/231891-B22/231891R-B21/231891R-B22/231892-B21/231892-B22/231892R-B22/231979-B21","/ProductCenter/ProductDetails/Resources-ProductInfo/TapeMachine/f891a42b-0d06-44de-a28c-7906c2750e5f/")'''
# sql2 = '''insert into qxf_kfpartsmachine(parts_id,machine_name,machine_url) values(81348,"HP StorageWorks MSL5026 Tape Library 293472-B21/293472-B22/293472-B23/293472-B24/293472-B25/293472R-B21/293472R-B22/293472R-B23/293472R-B24/293472R-B25/293473-B21/293473-B22/293473R-B21/293473R-B22/302511-B21/302511-B22/302511R-B21/302511R-B22/302512-B21/302512-B22/302512R-B21/302512R-B22/231821-B21/231821-B22/231821R-B22/231822-B21/231822-B22/231891-B21/231891-B22/231891R-B21/231891R-B22/231892-B21/231892-B22/231892R-B22/231979-B21","/ProductCenter/ProductDetails/Resources-ProductInfo/TapeMachine/f891a42b-0d06-44de-a28c-7906c2750e5f/")'''
# sql3 = '''insert into qxf_kfpartsmachine(parts_id,machine_name,machine_url) values(81350,"HP StorageWorks MSL5026 Tape Library 293472-B21/293472-B22/293472-B23/293472-B24/293472-B25/293472R-B21/293472R-B22/293472R-B23/293472R-B24/293472R-B25/293473-B21/293473-B22/293473R-B21/293473R-B22/302511-B21/302511-B22/302511R-B21/302511R-B22/302512-B21/302512-B22/302512R-B21/302512R-B22/231821-B21/231821-B22/231821R-B22/231822-B21/231822-B22/231891-B21/231891-B22/231891R-B21/231891R-B22/231892-B21/231892-B22/231892R-B22/231979-B21","/ProductCenter/ProductDetails/Resources-ProductInfo/TapeMachine/f891a42b-0d06-44de-a28c-7906c2750e5f/")'''
# sql4 = '''insert into qxf_kfpartsmachine(parts_id,machine_name,machine_url) values(81353,"HP StorageWorks MSL5026 Tape Library 293472-B21/293472-B22/293472-B23/293472-B24/293472-B25/293472R-B21/293472R-B22/293472R-B23/293472R-B24/293472R-B25/293473-B21/293473-B22/293473R-B21/293473R-B22/302511-B21/302511-B22/302511R-B21/302511R-B22/302512-B21/302512-B22/302512R-B21/302512R-B22/231821-B21/231821-B22/231821R-B22/231822-B21/231822-B22/231891-B21/231891-B22/231891R-B21/231891R-B22/231892-B21/231892-B22/231892R-B22/231979-B21","/ProductCenter/ProductDetails/Resources-ProductInfo/TapeMachine/f891a42b-0d06-44de-a28c-7906c2750e5f/")'''
# sql5 = '''insert into qxf_kfpartsmachine(parts_id,machine_name,machine_url) values(81355,"HP StorageWorks MSL5026 Tape Library 293472-B21/293472-B22/293472-B23/293472-B24/293472-B25/293472R-B21/293472R-B22/293472R-B23/293472R-B24/293472R-B25/293473-B21/293473-B22/293473R-B21/293473R-B22/302511-B21/302511-B22/302511R-B21/302511R-B22/302512-B21/302512-B22/302512R-B21/302512R-B22/231821-B21/231821-B22/231821R-B22/231822-B21/231822-B22/231891-B21/231891-B22/231891R-B21/231891R-B22/231892-B21/231892-B22/231892R-B22/231979-B21","/ProductCenter/ProductDetails/Resources-ProductInfo/TapeMachine/f891a42b-0d06-44de-a28c-7906c2750e5f/")'''
# sql6 = '''insert into qxf_kfpartsmachine(parts_id,machine_name,machine_url) values(81357,"HP StorageWorks MSL5026 Tape Library 293472-B21/293472-B22/293472-B23/293472-B24/293472-B25/293472R-B21/293472R-B22/293472R-B23/293472R-B24/293472R-B25/293473-B21/293473-B22/293473R-B21/293473R-B22/302511-B21/302511-B22/302511R-B21/302511R-B22/302512-B21/302512-B22/302512R-B21/302512R-B22/231821-B21/231821-B22/231821R-B22/231822-B21/231822-B22/231891-B21/231891-B22/231891R-B21/231891R-B22/231892-B21/231892-B22/231892R-B22/231979-B21","/ProductCenter/ProductDetails/Resources-ProductInfo/TapeMachine/f891a42b-0d06-44de-a28c-7906c2750e5f/")'''
# sql7 = '''insert into qxf_kfpartsmachine(parts_id,machine_name,machine_url) values(81328,"HP StorageWorks MSL5026 Tape Library 293472-B21/293472-B22/293472-B23/293472-B24/293472-B25/293472R-B21/293472R-B22/293472R-B23/293472R-B24/293472R-B25/293473-B21/293473-B22/293473R-B21/293473R-B22/302511-B21/302511-B22/302511R-B21/302511R-B22/302512-B21/302512-B22/302512R-B21/302512R-B22/231821-B21/231821-B22/231821R-B22/231822-B21/231822-B22/231891-B21/231891-B22/231891R-B21/231891R-B22/231892-B21/231892-B22/231892R-B22/231979-B21","/ProductCenter/ProductDetails/Resources-ProductInfo/TapeMachine/f891a42b-0d06-44de-a28c-7906c2750e5f/")'''
# sql8 = '''insert into qxf_kfpartsmachine(parts_id,machine_name,machine_url) values(81331,"HP StorageWorks MSL5026 Tape Library 293472-B21/293472-B22/293472-B23/293472-B24/293472-B25/293472R-B21/293472R-B22/293472R-B23/293472R-B24/293472R-B25/293473-B21/293473-B22/293473R-B21/293473R-B22/302511-B21/302511-B22/302511R-B21/302511R-B22/302512-B21/302512-B22/302512R-B21/302512R-B22/231821-B21/231821-B22/231821R-B22/231822-B21/231822-B22/231891-B21/231891-B22/231891R-B21/231891R-B22/231892-B21/231892-B22/231892R-B22/231979-B21","/ProductCenter/ProductDetails/Resources-ProductInfo/TapeMachine/f891a42b-0d06-44de-a28c-7906c2750e5f/")'''
# for sql in [sql1,sql2,sql3,sql4,sql5,sql6,sql7,sql8]:
#     result = info.dataManager.op_sql(sql)
#     if result:
#         print('true')



