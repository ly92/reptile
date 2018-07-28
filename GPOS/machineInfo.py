#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: garner

@file: machineInfo.py

@time: 2018/7/27 17:10

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


class MachineInfo():
    def __init__(self):
        self.dataManager = OperationDbInterface()

    def operationGoods(self,url,machine_id):
        options = Options()
        options.add_argument('-headless')
        driver = Firefox(executable_path='/usr/local/bin/geckodriver', firefox_options=options)
        driver.get(url)
        source = driver.page_source
        driver.close()

        #整机
        info_name = ''
        info_desc = ''

        #配件
        parts_name = ''
        parts_fc = ''
        parts_pn = ''
        parts_desc = ''
        parts_url = ''
        print(source)

        tedi = BeautifulSoup(str(source),'lxml').find('div',class_='aspNetHidden')
        # print(tedi)

        # body_div = BeautifulSoup(str(source),'lxml').find('div',id='body')
        # print(body_div)
        # content_div = BeautifulSoup(str(body_div),'lxml').find('div', class_='prodDetails')
        # print('-----')
        # print(content_div)
        # print('-----------')
        return
        tables = BeautifulSoup(str(content_div),'lxml').find_all('table', class_='ptmtb')

        machine_table = tables[0]
        machine_tbody = BeautifulSoup(str(machine_table),'lxml').find('tbody')
        mac_trs = BeautifulSoup(str(machine_tbody),'lxml').find_all('tr')
        for tr in mac_trs:
            # 清理上次记录
            info_name = ''
            info_desc = ''

            tds = BeautifulSoup(str(tr),'lxml').find_all('td')
            if len(tds) == 2:
                info_name = str(tds[0].text).strip()
                info_desc = str(tds[1].text).strip()
            else:
                info_name = '整机信息'

            print('-------------------------------------------------------------------------')
            machine_sql = '''insert into qxf_kfmachineinfo(machine_id,info_name,info_desc) values(%d,"%s","%s")''' % (
            machine_id, info_name, info_desc)
            print(machine_sql)

        parts_table = tables[1]
        parts_tbody = BeautifulSoup(str(parts_table), 'lxml').find('tbody')
        parts_trs = BeautifulSoup(str(parts_tbody), 'lxml').find_all('tr')
        parts_index = 1
        for tr in parts_trs:
            #清理上次记录
            # parts_name = ''
            parts_fc = ''
            parts_pn = ''
            parts_desc = ''
            parts_url = ''

            tds = BeautifulSoup(str(tr), 'lxml').find_all('td')
            if len(tds) == 1:
                parts_name = str(tds[0].text).strip()
            elif len(tds) == 3:
                index = 1
                for td in tds:
                    a = BeautifulSoup(str(td), 'lxml').find('a')
                    if index == 1:
                        if parts_index == 2:
                            parts_fc = str(td.text).strip()
                        else:
                            if a:
                                parts_fc = str(a.text).strip()
                    elif index == 2:
                        if parts_index == 2:
                            parts_pn = str(td.text).strip()
                        else:
                            if a:
                                parts_pn = str(a.text).strip()
                                parts_url = a['href']
                    else:
                        parts_desc = str(td.text).strip()
                    index += 1
                print('-------------------------------------------------------------------------')
                parts_sql = '''insert into qxf_kfparts(machine_id,parts_name,parts_fc,parts_pn,parts_desc,parts_url) values(%d,"%s","%s","%s","%s","%s")''' % (
                machine_id, parts_name, parts_fc, parts_pn, parts_desc, parts_url)
                print(parts_sql)
            parts_index += 1

        # self.dataManager.op_sql(sql)



info = MachineInfo()
machines = info.dataManager.select_all('select * from qxf_kfmachine')
for machine in machines:
    url = 'http://www.gpos.cn' + machine['machine_url']
    machine_id =  machine['id']
    print(url)
    print(machine_id)
    info.operationGoods(url,machine_id)
    # break
