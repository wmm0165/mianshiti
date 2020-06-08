# -*- coding: utf-8 -*-
# @Time : 2019/11/28 23:44
# @Author : wangmengmeng
"""如何在函数内部修改全局变量"""
a = 5


def fn():
    global a
    a = 4


fn()
print(a)
