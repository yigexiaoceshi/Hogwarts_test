#!/usr/bin/python3
# -*- coding:utf-8 -*-
list = [1, 2, 3, "a", 4, 5, 6]
list[0] = 8
print(list)

print("*" * 20, "将列表中的元素a替换成b", "*" * 20)
a_weizhi = list.index("a")  # 找出元素a对应的索引位置
print(type(a_weizhi))  # 索引数据类型为int
print("a元素的索引下标是：", a_weizhi)
list[a_weizhi] = "b"  # 完成元素替换
print(list)
