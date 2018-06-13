#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: mxonline

@file: GoodsDetail.py

@time: 2018/5/25 下午3:48

@desc:

'''


import requests
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from DatabaseManager import OperationDbInterface
from time import sleep



class GoodsDetail():
    def __init__(self):
        self.dataManager = OperationDbInterface()

    def request(self, url):
        driver = webdriver.PhantomJS()
        driver.get(url)
        return driver.page_source


    def operationGoods(self, goods_id):
        url = 'http://www.tradeunix.com/productlist.php?pid=%d'%(goods_id)
        source = self.request(url)
        contentDiv = BeautifulSoup(source, 'lxml').find('div', id='prolist')
        if len(BeautifulSoup(str(contentDiv), 'lxml').find_all('table', class_='ibm-data-table')) > 0:
            tables = BeautifulSoup(str(contentDiv), 'lxml').find_all('table', class_='ibm-data-table')
            for table in tables:
                tbodys = BeautifulSoup(str(table), 'lxml').find_all('tbody')
                for tbody in tbodys:
                    trs = BeautifulSoup(str(tbody), 'lxml').find_all('tr')
                    for tr in trs:
                        th = BeautifulSoup(str(tr), 'lxml').find('th')
                        desc1 = str(th.text).strip()
                        # 'insert into real_goods_list(goods_name,goods_id) values("%s",%d)'''%(goods_name,goods_id)'
                        tds = BeautifulSoup(str(tr), 'lxml').find_all('td')
                        key = ''
                        value = ''
                        for i in range(len(tds)):
                            td = str(tds[i].text).strip()
                            key += ',' + 'desc%d'%(i+2)
                            value += ',' + '"%s"'%(td)
                        sql = '''insert into real_goods_detail(goods_id,%s) values(%d,"%s"%s)'''%('desc1'+key,goods_id,desc1,value)
                        result = self.dataManager.op_sql(sql)
                        if result == False:
                            print(sql)
        elif len(BeautifulSoup(str(contentDiv), 'lxml').find_all('table', class_='MsoNormalTable')) > 0:
            tables = BeautifulSoup(str(contentDiv), 'lxml').find_all('table', class_='MsoNormalTable')
            for table in tables:
                tbodys = BeautifulSoup(str(table), 'lxml').find_all('tbody')
                for tbody in tbodys:
                    trs = BeautifulSoup(str(tbody), 'lxml').find_all('tr')
                    for tr in trs:
                        tds = BeautifulSoup(str(tr), 'lxml').find_all('td')
                        key = ''
                        value = ''
                        for i in range(len(tds)):
                            td = tds[i]
                            spans = BeautifulSoup(str(td), 'lxml').find_all('span')
                            desc = ''
                            for span in spans:
                                desc += str(span.text).strip()
                            key += ',' + 'desc%d' % (i + 1)
                            value += ',' + '"%s"'%(desc)
                        sql = '''insert into real_goods_detail(goods_id%s) values(%d%s)''' % (
                            key,goods_id, value)
                        result = self.dataManager.op_sql(sql)
                        if result == False:
                            print(sql)
        else:
            ps = BeautifulSoup(str(contentDiv), 'lxml').find_all('p')
            desc = ''
            for p in ps:
                desc += str(p.text).strip()
            sql = '''insert into real_goods_detail(goods_id,desc1) values(%d,"%s")''' % (goods_id,desc)
            result = self.dataManager.op_sql(sql)
            if result == False:
                print(sql)


# 36522
#         tables = BeautifulSoup(str(contentDiv), 'lxml').find_all('table', class_='ibm-data-table')
#         for table in tables:
#             tbodys = BeautifulSoup(str(table), 'lxml').find_all('tbody')
#             for tbody in tbodys:
#                 trs = BeautifulSoup(str(tbody), 'lxml').find_all('tr')
#                 for tr in trs:
#                     th = BeautifulSoup(str(tr), 'lxml').find('th')
#                     print(str(th.text).strip())
#                     tds = BeautifulSoup(str(tr), 'lxml').find_all('td')
#                     for td in tds:
#                         print(str(td.text).strip())
#                     print('---------------------')

        # 41170
        # tables = BeautifulSoup(str(contentDiv), 'lxml').find_all('table', class_='ibm-data-table')
        # for table in tables:
        #     tbodys = BeautifulSoup(str(table), 'lxml').find_all('tbody')
        #     for tbody in tbodys:
        #         trs = BeautifulSoup(str(tbody), 'lxml').find_all('tr')
        #         for tr in trs:
        #             th = BeautifulSoup(str(tr), 'lxml').find('th')
        #             print(str(th.text).strip())
        #             tds = BeautifulSoup(str(tr), 'lxml').find_all('td')
        #             for td in tds:
        #                 print(str(td.text).strip())
        #             print('---------------------')



# 35755
        # tables = BeautifulSoup(str(contentDiv), 'lxml').find_all('table', class_='MsoNormalTable')
        # for table in tables:
        #     tbodys = BeautifulSoup(str(table), 'lxml').find_all('tbody')
        #     for tbody in tbodys:
        #         trs = BeautifulSoup(str(tbody), 'lxml').find_all('tr')
        #         for tr in trs:
        #             tds = BeautifulSoup(str(tr), 'lxml').find_all('td')
        #             for td in tds:
        #                 spans = BeautifulSoup(str(td), 'lxml').find_all('span')
        #                 desc = ''
        #                 for span in spans:
        #                     desc += str(span.text).strip()
        #                 print(desc)
        #             print('---------------------')

    # 36560
    # ps = BeautifulSoup(str(contentDiv), 'lxml').find_all('p')
    # for p in ps:
    #     print(str(p.text).strip())

    def getAll(self):
        secrchArr = self.dataManager.select_all('select goods_id from real_goods_list')
        for item in secrchArr:
            # print(item['goods_id'])
            self.operationGoods(item['goods_id'])

detai = GoodsDetail()
# 'http://www.tradeunix.com/productlist.php?pid=36560'
# 'http://www.tradeunix.com/productlist.php?pid=41170'
# 'http://www.tradeunix.com/productlist.php?pid=36522'
# for id in [35755,36560,41170,36522]:
#     detai.operationGoods(id)

detai.getAll()