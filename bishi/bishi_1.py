# -*- coding: utf-8 -*-
# @Time : 2019/11/28 17:25
# @Author : wangmengmeng
"""统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]"""
a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
b = [i for i in a if i > 0]
print(len(b))
c = [i for i in a if i < 0]
print(len(c))