#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
变量：存放一个数据的容器
列表：存放多个数据的容器
"""
print("*" * 20, "列表定义：空列表", "*" * 20)
list1 = []
print(type(list1))

print("*" * 20, "列表定义：非空列表", "*" * 20)
#  列表支持的数据类型：int，float，str，bool，list，tuple，set，dict
list2 = [1, 0.5, "abc", True, [1, 2, 3], (1, 2, 3), {1, 2, "a"}, {"name": "老王", "age": 20}]
print(type(list2))

print("*" * 20, "获取列表元素：通过索引，从左至右0开始，从右至左-1开始，和字符串一致", "*" * 20)
print(list2[0])
print(list2[-1])

print("*" * 20, "列表切片：和字符串一致，前开后闭，正序取不到最后一个元素，倒序取不到第一个元素", "*" * 20)
print(list2[1:6:2])
print(list2[-1:-5:-2])
print(list2[::-1])

print("*" * 20, "列表元素读取：遍历", "*" * 20)
for i in list2:
    print(i)
