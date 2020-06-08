# -*- coding: utf-8 -*-
# @Time : 2019/11/29 0:01
# @Author : wangmengmeng
"""字典如何删除和合并两个字典"""
dic = {"name":"wangmm","age":18}
del dic['name']
print(dic)
dic2 = {"cc":"ff"}
dic.update(dic2)
print(dic)