# -*- coding: utf-8 -*-
# @Time : 2020/4/10 15:48
# @Author : wangmengmeng

def get_type_1(s):
    """方法一：使用字符串的分割获取"""
    print(s)
    type = s.split('.')[-1]
    return '.'+type


def get_type_2(s):
    """方法二：使用正则表达式"""


if __name__ == '__main__':

    s = "http://blog.sina.com.cn/s/blog_17bce02530102ytft.html"
    print(get_type_1(s))
