# -*- coding: utf-8 -*-
# @Time : 2019/11/28 17:57
# @Author : wangmengmeng
"""已知一个队列[1, 3, 6, 9, 7, 3, 4, 6]"""
a = [1, 3, 6, 9, 7, 3, 4, 6]
a.sort()
print(a) # 正序排序
a.sort(reverse=True)
print(a) # 倒序排序
print(list(set(a))) # 去重
