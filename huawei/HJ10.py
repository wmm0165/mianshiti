# -*- coding: utf-8 -*-
# @Time : 2020/7/26 1:55
# @Author : wangmengmeng
from collections import Counter
l = [1, 'a', 4]
c = Counter(l)
print(c)
print(c.keys())

# print(c)  # 2aaa3 Counter({'a': 3, '2': 1, '3': 1})
# print(c.keys())
# l = []
# for k in c.keys():
#     if isinstance(k,str):
#         l.append(k)
# print(len(l))