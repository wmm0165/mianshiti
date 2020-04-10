# -*- coding: utf-8 -*-
# @Time : 2020/3/22 22:34
# @Author : wangmengmeng
"""
输入：abcd12345ed125ss123058789
输出：123058789,9
"""


class Data(object):
    def __new__(self):
        print("new")

    def __init__(self):
        print("init")

data = Data()