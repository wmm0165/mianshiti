# -*- coding: utf-8 -*-
# @Time : 2019/10/15 10:59
# @Author : wangmengmeng
"""
input：输入包括一个字符串s,字符串s的长度length(1 ≤ length ≤ 50),s只含小写字母('a'-'z')
output：
输出一个整数,表示所有碎片的平均长度,四舍五入保留两位小数。
如样例所示: s = "aaabbaaac"
所有碎片的平均长度 = (3 + 2 + 3 + 1) / 4 = 2.25
"""
s = input()
n = len(s)
k = 0
for i in range(n-1):
    if s[i] !=s[i+1]:
        k = k+1
print(float(n/(k+1)))