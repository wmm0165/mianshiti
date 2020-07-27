# -*- coding: utf-8 -*-
# @Time : 2020/3/20 17:32
# @Author : wangmengmeng
"""
s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
"""
s = "ajldjlajfdljfddd"
s = set(s)
s = list(s)
s.sort(reverse=False)
print(s)
res = ''.join(s)
print(res)