# -*- coding: utf-8 -*-
# @Time : 2020/7/25 16:31
# @Author : wangmengmeng

while True:
    try:
        string = input()
        n = len(string)
        # print(string[0:8]) if n >= 8 else print((8 - n) * str(0) + string)
        if n <= 8:
            print(string + (8 - n) * str(0))
        else:
            while len(string) >8:
                print(string[:8])
                string = string[8:]
            print(string + (8 - len(string)) * str(0))
    except:
        break
