# -*- coding: utf-8 -*-
# @Time : 2020/7/26 1:43
# @Author : wangmengmeng
from collections import OrderedDict
s = input()
l = s[::-1]
o = OrderedDict()
for k in l:
    o[k] = 0

for i in o.keys():
    print(i,end='')



