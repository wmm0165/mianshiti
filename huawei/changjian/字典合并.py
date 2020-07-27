# -*- coding: utf-8 -*-
# @Time : 2020/3/22 23:23
# @Author : wangmengmeng
from collections import Counter

x = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
y = {'b': 3, 'd': 5, 'e': 7, 'm': 9}
print(Counter(x))
print(dict(Counter(x) + Counter(y)))
