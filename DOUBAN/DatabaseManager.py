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
1页25个
https://movie.douban.com/top250    
https://movie.douban.com/subject/1292052/
https://movie.douban.com/top250?start=75&filter=
https://movie.douban.com/top250?start=150&filter=

1、某导演所执导的所有电影
2、某国家的
3、按照年份分类

1、排名int rank
2、名称string name
3、别名array other_name
4、导演 director
5、年份int show_year
6、国家string nationnality
7、类别 video_sort
8、评分 grade
9、星级 star_level
10、评价人数 valuator_num
11、短简介 shot_intro

12、简介 intro
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

    def insert_item(self,rank,video_name,other_name,director,show_year,nationality,video_sort,grade,
                    valuator_num,shot_intro,intro_link,intro,playable,actor):
        sql = '''insert into videos_copy(rank,video_name,other_name,director,show_year,nationality,video_sort,grade,valuator_num,shot_intro,intro_link,intro,playable,actor) values(%d,"%s","%s","%s",%d,"%s","%s",%.1f,%d,"%s","%s","%s",%d,"%s")'''%(rank,video_name,other_name,director,show_year,nationality,video_sort,grade,valuator_num,shot_intro,intro_link,intro,playable,actor)
        # print(sql)
        return self.op_sql(sql)






# test = OperationDbInterface() # 实例化类
# # result_1 = test.select_one('select*from D_COM_RG_PERN') # 查询一条数据
# # print(result_1)
# result_2 = test.select_all('select*from videos') # 查询所有数据
# print(result_2)
# result = test.insert_item(1,"2","3","4",5,"6","7",8,8.5,9,"10","11")
# print(result)

