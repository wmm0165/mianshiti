# -*- coding: utf-8 -*-
# @Time : 2020/7/23 16:46
# @Author : wangmengmeng

"""
给定两个字符串a b，注意：其中a字符串中有空格。求b字符串在a字符串中出现的次数

输入：a="abc cc d"，b="cc"。
输出：b在a中出现次数为：2次
"""



a="abc cc d cc"
b="cc"
# 方式一
# aa = a.split()
# print(aa)
# new = "".join(aa)
# print(new.count(b))
# 方式二
aa = a.strip()
print(aa.count(b))