# -*- coding: utf-8 -*-
# @Time : 2020/7/26 9:24
# @Author : wangmengmeng

def gcd(n1,n2):
    """greatest common divisor function """
    return gcd(n2, n1 % n2) if n2 > 0 else n1




c = gcd(12,54)
print(gcd(10,5))