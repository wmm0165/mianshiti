# -*- coding: utf-8 -*-
# @Time : 2020/4/22 16:30
# @Author : wangmengmeng
"""map、reduce函数"""
from functools import reduce


def f(x):
    return x * x


a_list = [3, 6, 7]
r = map(f, a_list)  # 返回的是个迭代器
print(r)
print(list(r))

a_str = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 把list的所有数字转为字符串
print(a_str)


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))
