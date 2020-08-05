# -*- coding: utf-8 -*-
# @Time : 2020/4/29 9:43
# @Author : wangmengmeng
"""filter():过滤序列，与map()类似，会根据返回结果是True还是False决定保留还是丢弃该元素"""


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
