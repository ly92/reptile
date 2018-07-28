#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: garner

@file: machine.py

@time: 2018/7/27 15:40

@desc:

'''




from bs4 import BeautifulSoup
from DatabaseManager import OperationDbInterface
import re

class Machine():
    def __init__(self):
        self.dataManager = OperationDbInterface()
        self.COUNT = 0

    def operationGoods(self,ulStr,brand_id,type_id):
        machine_name = ''
        machine_url = ''

        lis = BeautifulSoup(str(ulStr),'lxml').find_all('li')
        for li in lis:
            a = BeautifulSoup(str(li),'lxml').find('a')
            machine_name = str(a.text).strip()
            machine_url = a['href']
            print('-------------------------------------------------------------------------')
            sql = '''insert into qxf_kfmachine(machine_name,machine_url,brand_id,type_id) values("%s","%s",%d,%d)''' % (machine_name,machine_url,brand_id,type_id)
            # print(sql)
            self.COUNT += 1
            print(self.COUNT)
            # 防止误操作重复数据，将下面注释
            # self.dataManager.op_sql(sql)

machine = Machine()

filePath = '/Users/ly/Desktop/123213/1-hp.html;/Users/ly/Desktop/123213/1-sun.html;/Users/ly/Desktop/123213/2-hp.html;/Users/ly/Desktop/123213/2-ibm.html;/Users/ly/Desktop/123213/2-sun.html;/Users/ly/Desktop/123213/3-hp.html;/Users/ly/Desktop/123213/3-ibm.html;/Users/ly/Desktop/123213/3-sun.html;/Users/ly/Desktop/123213/4-hp.html;/Users/ly/Desktop/123213/4-ibm.html;/Users/ly/Desktop/123213/4-sun.html;/Users/ly/Desktop/123213/5-ibm.html;/Users/ly/Desktop/123213/5-sun.html;/Users/ly/Desktop/123213/6-hp.html;/Users/ly/Desktop/123213/6-ibm.html;/Users/ly/Desktop/123213/7-hp.html;/Users/ly/Desktop/123213/7-ibm.html;/Users/ly/Desktop/123213/7-sun.html'

def read_txt(dir):
    with open(dir,'r') as f:
        return f.readlines()
    return ''


urlPaths = re.split('[;]',filePath)
for url in urlPaths:
    sss = read_txt(url)
    aaa = url.replace('/Users/ly/Desktop/123213/','')
    aaa = aaa.replace('hp.html', '1')
    aaa = aaa.replace('ibm.html', '2')
    aaa = aaa.replace('sun.html', '3')
    indexs = re.split('[-]',aaa)
    type_id = indexs[0]
    brand_id = indexs[1]
    machine.operationGoods(sss, int(brand_id), int(type_id))

#
# for ss in ['HP','IBM','SUN']:
#     sql = '''insert into qxf_kfbrand(brand_name) values("%s")''' % (ss)
#     print(sql)
#     machine.dataManager.op_sql(sql)
#
# for ss in ['小型机','PC服务器','存储整机','磁带库','NAS','SAN','刀片服务器']:
#     sql = '''insert into qxf_kfmachinetype(type_name) values("%s")''' % (ss)
#     print(sql)
#     machine.dataManager.op_sql(sql)
