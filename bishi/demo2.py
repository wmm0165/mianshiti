# -*- coding: utf-8 -*-
# @Time : 2020/7/23 16:26
# @Author : wangmengmeng
"""
写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写
"""

a = input().lower()
b = input().lower()
print(a.count(b))