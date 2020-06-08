# -*- coding: utf-8 -*-
# @Time : 2019/11/28 22:32
# @Author : wangmengmeng
"""python实现排序算法"""

def bubble_sort(list):
    """冒泡排序
    每一次排序最后一个元素是最大的"""
    for i in range(len(list)):
        for j in range(1,len(list)-1):
            if list[j-1] > list[j]:
                list[j - 1],list[j] = list[j],list[j - 1]
    return list