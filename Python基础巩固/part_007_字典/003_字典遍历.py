#!/usr/bin/python3
# -*- coding:utf-8 -*-
book = {'书名': '《三体》', '价格': 16.0, '作者': '刘慈欣', '出版社': 'XXX出版社'}
print("*" * 20, "获取字典所有的key", "*" * 20)
for i in book:
    print(i, end="  ")  # 直接遍历字典，取出来的是key
# 等同于：
for j in book.keys():
    print("\n", j, end="  ")
print(book.keys())
print(list(book.keys()))

print("*" * 20, "获取字典所有的value", "*" * 20)
for k in book.values():
    print(k)
print(book.values())
print(list(book.values()))

print("*" * 20, "获取字典所有的key/value对：dict.items()，每一对放在一个元组里，嵌套成一个列表返回", "*" * 20)
print(book.items())
print(list(book.items()))
for h in book.items():
    print(h)
# 也可以写成：
for x, y in book.items():
    print(x, y)

print("*" * 20, "dict.setdefault(key,value),key存在则默认值无效，key不存在则新增，仅做新增", "*" * 20)
book.setdefault('出版社', '人民教育出版社')
print(book)
book.setdefault("出版时间", 1990)
print(book)

print("*" * 20, "字典合并：dict.update(dict1)，将参数dict1里的键值对添加到dict里", "*" * 20)
dict1 = {"a": 10, "b": 20}
book.update(dict1)
print(book)

print("*" * 20, "字典新增：dict.fromkeys(a,b)，参数a必须是个可迭代对象，作为key，b作为value的默认值", "*" * 20)
xx = dict.fromkeys(["a", "b"], 10)
print(xx)
yy = dict.fromkeys(("a", "b"), ["fsfs", 3234, True])
print(yy)
