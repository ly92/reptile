#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: garner

@file: DatabaseManager.py

@time: 2017/11/16 16:36

@desc:

'''

'''
pip install PyMySQL

'''



'''mysqlclient

'''

import pymysql
import os
import logging

class OperationDbInterface(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password='11111111',
                                    db='reptile',
                                    port=3306,
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor) # 创建数据库连接
        self.cur = self.conn.cursor() # 创建游标


    # 定义单条数据操作，增删改
    def op_sql(self, params):
        try:
            self.cur.execute(params) # 执行sql语句
            self.conn.commit()
            return True
        except  pymysql.Error as e:
            print("MySQL Error %d: %s" % (e.args[0], e.args[1]))
            logging.basicConfig(filename=os.path.join(os.getcwd(), './log.txt'), level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levekname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return False

    # 查询表中单条数据
    def select_one(self, condition):
        try:
            self.cur.execute(condition)
            results = self.cur.fetchone() # 获取一条结果
        except pymysql.Error as e:
            results = 'sql0001' # 数据库执行失败
            print("MySQL Error %d: %s" % (e.args[0], e.args[1]))
            logging.basicConfig(filename=os.path.join(os.getcwd(), './log.txt'),
                                level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        finally:
            return results


    # 查询表中所有数据
    def select_all(self, condition):
        try:
            self.cur.execute(condition)
            self.cur.scroll(0, mode='absolute') # 光标回到初始位置
            results = self.cur.fetchall() # 返回游标中所有结果
        except pymysql.Error as e:
            results = 'sql0001' # 数据库执行失败
            print("MySQL Error %d: %s" % (e.args[0], e.args[1]))
            logging.basicConfig(filename=os.path.join(os.getcwd(), './log.txt'),
                                level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        finally:
            return results


    def insert_group(self,title,p_id,path):
        if p_id == -1:
            sql = '''insert into groups(title,path) values("%s","%s")''' % (title,path)
            print(sql)
            return self.op_sql(sql)
        else:
            sql = '''insert into groups(title,p_id,path) values("%s",%d,"%s")''' % (title, p_id,path)
            print(sql)
            return self.op_sql(sql)


    def insert_article(self,title,group_id,ext,path):
        sql = '''insert into article(title,group_id,ext,path) values("%s",%d,"%s","%s")''' % (title, group_id, ext,path)
        print(sql)
        return self.op_sql(sql)









# test = OperationDbInterface() # 实例化类
# # result_1 = test.select_one('select*from D_COM_RG_PERN') # 查询一条数据
# # print(result_1)
# result_2 = test.select_all('select*from videos') # 查询所有数据
# print(result_2)
# result = test.insert_item(1,"2","3","4",5,"6","7",8,8.5,9,"10","11")
# print(result)

