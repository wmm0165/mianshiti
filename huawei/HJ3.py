# -*- coding: utf-8 -*-
# @Time : 2020/7/25 15:00
# @Author : wangmengmeng
while True:
    try:
        num = int(input())
        l = []
        for i in range(num):
            l.append(int(input()))
        for i in sorted(set(l)):
            print(i)
    except:
        break