# -*- coding: utf-8 -*-
# @Time : 2020/8/3 10:18
# @Author : wangmengmeng

"""
操作目录与文件
os.remove() 删除文件
os.path.split():把一个路径拆成两部分，后一部分总是最后级别的目录或文件名
列出所有的.py文件：[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
"""
import os

print(os.path.split('/Users/michael/testdir/file.txt'))  # ('/Users/michael/testdir', 'file.txt')
print(os.path.splitext('/path/to/file.txt'))  # 获取文件扩展名 ('/path/to/file', '.txt')

