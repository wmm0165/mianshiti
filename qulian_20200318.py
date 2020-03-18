# -*- coding: utf-8 -*-
# @Time : 2020/3/18 23:15
# @Author : wangmengmeng
from collections import Counter


def compare_two_list(list1, list2):
    """找出两个列表中的相同元素"""
    list = []
    for i in list1:
        if i in list2:
            list.append(i)
    return list


def get_repeat2(list):
    """找出一个列表中重复两次的元素"""
    b = Counter(list)
    print(b)
    c = [key for key, value in b.items() if value == 2]
    return c


if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [2, 4]
    l = compare_two_list(list1, list2)
    print(l)
    list3 = [4, 4, 6, 7, 7]
    print(get_repeat2(list3))
