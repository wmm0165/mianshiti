# -*- coding: utf-8 -*-
# @Time : 2019/11/28 22:32
# @Author : wangmengmeng
"""python实现排序算法"""


def bubble_sort(list):
    """冒泡排序
    每一次排序最后一个元素是最大的"""
    for i in range(len(list)):
        for j in range(1, len(list) - i):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
    return list


def quickSort(myList, start, end):
    """快速排序"""
    if start < end:
        i, j = start, end
        base = myList[i]
        while i < j:
            while (i < j and myList[j] >= base):
                j -= 1
            myList[i] = myList[j]
            while (i < j and myList[i] <= base):
                i += 1
            myList[j] = myList[i]
        myList[i] = base  # 第一轮结束，i=j，将基准值放进去
        quickSort(myList, start, i - 1)
        quickSort(myList, i + 1, end)
    return myList


if __name__ == '__main__':
    l = [2, 1, 4, 5, 3]
    # ln = quickSort(l, 0, 4)
    # print(ln)
    l2 = [2, 9]
    print(l + l2)
