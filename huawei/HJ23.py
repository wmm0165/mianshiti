# -*- coding: utf-8 -*-
# @Time : 2020/8/5 18:04
# @Author : wangmengmeng
from collections import Counter

while True:
    try:
        c = Counter(input())
        la = [key for key, value in c.items() if value == 1]
        if la:
            print(la[0])
        else:
            print(-1)
    except:
        break


c = list(map(lambda c: c[0], list(filter(lambda c: c[1] == 1, Counter(a).most_common()))))