#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: mxonline

@file: operation.py

@time: 2018/8/10 下午5:08

@desc:

'''


from DatabaseManager import OperationDbInterface



class Operation():
    def __init__(self):
        self.dataManager = OperationDbInterface()





info = Operation()


partses = info.dataManager.select_all("select * from qxf_kfpartsmachine")
for parts in partses:
    machines = info.dataManager.select_all("select * from qxf_kfmachine WHERE machine_url='%s'"%(parts['machine_url']))
    id_arr = []
    for machine in machines:
        id_arr.append(str(machine['machine_id']))
    ids = ','.join(id_arr)
    sql = '''UPDATE qxf_kfpartsmachine SET machine_id = %s WHERE id = %d''' % (ids, parts['id'])
    # print(sql)
    result = info.dataManager.op_sql(sql)
    print(result)
    print('------------------')







# info.dataManager.op_sql("delete from qxf_kfmachineinfo where info_name = '整机信息'")


# partses = info.dataManager.select_all("select * from qxf_kfparts WHERE machine_id=1")
# part_arr = []
# part_dict = {}
# for parts in partses:
#     # sql = '''UPDATE qxf_kfmachine SET machine_id = %d WHERE id = %d''' % (parts['id'],parts['id'])
#     # result = info.dataManager.op_sql(sql)
#     # print(result)
#     # print(machine_url)
#     # print(parts['machine_id'])
#
#     part_name = parts['parts_name']
#
#     if part_name in part_dict:
#         arr = list(part_dict[part_name])
#         arr.append(parts)
#         part_dict[part_name] = arr
#     else:
#         arr = list()
#         arr.append(parts)
#         part_dict[part_name] = arr
#
#     if not part_arr.__contains__(parts['parts_name']):
#         part_arr.append(parts['parts_name'])
#
# # print(part_arr)
# print(part_dict)





