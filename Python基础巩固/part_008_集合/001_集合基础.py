#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
集合（set）：
1、无序：无索引概念，无法通过下标读取元素
2、元素不重复：类似字典里的key
3、符号：{}
4、花括号里非键值对且非空时，为集合
"""
print("*" * 20, "定义空集合：set()", "*" * 20)
# 注：a = {}，此时a是个字典，空集合用set()表示
set1 = set()
print("set1的类型为：{}，值为：{}".format(type(set1), set1))

print("*" * 20, "定义非空集合：set()", "*" * 20)
set2 = {1, "a", "你好", False}
print("set2的类型为：{}，值为：{}".format(type(set2), set2))

# 例题：列表元素去重，转为集合再转换回列表就去重了
lista = [1, 3, 3, 4, 5, 6, 5, 7, 8, 9, 9]
print(list(set(lista)))

print("*" * 20, "集合添加单个元素：set.add(元素)", "*" * 20)
set3 = set()
set3.add("西游记")
set3.add("红楼梦")
print(set3)

print("*" * 20, "集合合并：set.update(集合1)，将集合1的所有元素添加到set里", "*" * 20)
set4 = {"a", "b", "c"}
set5 = {1, 2, 3}
set5.update(set4)  # 将set4里的元素合并到set5，set4本身不变
print(set4)
print(set5)
