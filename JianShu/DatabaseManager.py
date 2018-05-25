#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: garner

@file: DatabaseManager.py

@time: 2018/1/4 18:50

@desc:

'''

import pymysql
import os

class Operation(object):

    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password = '11111111',
                                    db = 'jianshu',
                                    port = 3306,
                                    charset = 'utf8',
                                    cursorclass = pymysql.cursors.DictCursor)
        self.cur = self.conn.cursor()

    def op_sql(self, params):
        try:
            self.cur.execute(params)
            self.conn.commit()
            return True
        except pymysql.Error as e:
            print('MySql Error %d:%s' % (e.args[0], e.args[1]))
        return False

    def insert_Blog_item(self,blog_name, blog_detail,like,comment,see,author_id):
        sql = "insert into Blogs_blog(blog_name,blog_detail,see_num,comment_num,like_num,author_id) values('%s','%s',%d,%d,%d,%d)" % (blog_name,blog_detail,see,comment,like,author_id)
        print(sql)
        return self.op_sql(sql)

    def insert_Author_item(self,name, atten, like,id):
        sql = "insert into Author_author(author_name,attention_num,like_num,author_id) values('%s',%d,%d,%d)" % (name,atten,like,id)
        print(sql)
        return self.op_sql(sql)
