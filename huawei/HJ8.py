# -*- coding: utf-8 -*-
# @Time : 2020/7/26 1:19
# @Author : wangmengmeng
"""合并表记录"""
from collections import defaultdict

while True:
    try:
        a,dd = int(input()), defaultdict(int)
        for i in range(a):
            key,value = map(int,(input().split()))
            dd[key] += value
        for k in sorted(dd.keys()):
            print(str(k)+" " +str(dd[k]))
    except:
        break