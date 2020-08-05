# -*- coding: utf-8 -*-
# @Time : 2020/8/3 10:01
# @Author : wangmengmeng
"""
read():一次性读取文件的全部内容，文件很大时不适用
readlines():调用readlines()一次读取所有内容并按行返回list
write():写入文件
"""
with open(r"D:\myproject\mianshiti\hh\a.txt", 'r') as f:
    # content = f.read()
    # print(content)
    count = 0
    for line in f.readlines():
        count += 1
        print(line.strip())  # # 把末尾的'\n'删掉
    print(count)

with open(r"D:\myproject\mianshiti\hh\a.txt", 'a') as f:  # a是追加，w是覆写
    f.write("hello world!")
