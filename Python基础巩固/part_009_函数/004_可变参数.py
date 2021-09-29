#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
*args ：
**kwargs

拆包和装包
"""
# 元组和列表的拆包
print("*" * 20, "字符串、列表、元组、集合的解包：变量前面加一个*号", "*" * 20)
str_a = "123a"
print("变量前面加*号表示解包：", *str_a)
tuple_a = (1, 2, 3, "a")
print("变量前面加*号表示解包：", *tuple_a)
list_a = [1, 2, 3, "a"]
print("变量前面加*号表示解包：", *list_a)
set_a = {1, 2, 3, "a"}
print("变量前面加*号表示解包：", *set_a)
print("*" * 20, "字典解包，加两个**号", "*" * 20)
dict_a = {1: "a", 2: "b", 3: "c"}

print("*" * 20, "求n个数之和", "*" * 20)


# 参数的个数不确定
def get_sum(*args):
    sum_number = 0
    for i in args:
        sum_number += i
    print(sum_number)


get_sum(1)
get_sum(1, 2, 3)
get_sum(1, 2, 3, 4, 5)
