#!/usr/bin/python3
# -*- coding:utf-8 -*-
list = ['兔子', '老虎', '狮子', '狮子', '熊猫', '狮子']
for i in range(len(list) - 1, -1, -1):
    print(i, end='  ')

for j in range(0, len(list), 2):  # [0,1,2,3,4,5,6)
    print(j, end='  ')

for k in range(5, -1, -1):
    print(k)
print(f"你好，你的名字是{'张三'}")