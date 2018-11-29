#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: garner

@file: filePath.py

@time: 2018/11/15 16:54

@desc:

'''


import os
from DatabaseManager import OperationDbInterface


class FileOperation():
    def __init__(self):
        self.dataManager = OperationDbInterface()

        #brand
        # for brand in os.listdir(file_dir):


        # sql = '''update groups set path="%s" WHERE id=%d''' % (newPath, path['id'])
        # fileOP.dataManager.op_sql(sql)
    # group
    #     id
    #     p_id
    #     title
    #     path
    #
    # article
    #     group_id
    #     title
    #     ext
    #     path

        # for root, dirs, files in os.walk(file_dir):
        #     print(root)#当前目录路径
        #     print(dirs)#当前路径下所有子目录
        #     print(files)#当前路径下所有非目录子文件








fileOP = FileOperation()

url = '/Users/ly/Desktop/整理文档'




# for file in os.listdir(url):
#     # if file == 'EMC':
#     #     path = url + '/' +file
#     #     for root,dirs,files in os.walk(path):
#     #         print(dirs)
#     #         print(files)
#     #         # for dir in dirs:
#     #         #     fileOP.dataManager.insert_group()
#     #         print('*****************************')
#     #         break
#
#     print('-----------------------------------')
#     path = url + '/' + file
#     print(path)
#     for root, dirs, files in os.walk(path):
#         print(dirs)
#         print(files)
#         for file in files:
#             print(os.path.splitext(file)[1])
#         # for dir in dirs:
#         #     fileOP.dataManager.insert_group()
#         print('*****************************')
#         break

#0-17-91-187-314-372-390-398-402-406
paths = fileOP.dataManager.select_all('select * from groups WHERE id>0')
number = 0
for path in paths:
    for root, dirs, files in os.walk(path['path']):
        number += files.__len__()
        print(number)

        # for file in files:
        #     # print(path['id'])
        #     title = os.path.splitext(file)[0]
        #     ext = os.path.splitext(file)[1]
        #     # print(title)
        #     # print(ext)
        #     url = path['path'] + '/' + file
        #     fileOP.dataManager.insert_article(title,path['id'],ext,url)
        break





















