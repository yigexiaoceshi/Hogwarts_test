#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
元组：
1、不能增加、删除、修改元素
2、使用小括号()
3、元组中只有一个元素时，末尾必须添加一个逗号(,)，比如：(1,)，("ABC",)，(2.9,)
4、元组支持索引和切片
注：字符串切片返回字符串，列表切片返回列表，元组切片返回元组
"""

print("*" * 20, "元组定义", "*" * 20)
a = 1, 2, 3
b = (4, 5, 6)
c = ()
d = (7,)  # 仅有一个元素的时候，必须在末尾加个逗号，
e = (8)  # 仅有一个元素的时候，必须在末尾加个逗号，
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(a, b, c, d, e)

print("*" * 20, "元组索引", "*" * 20)
f = ("a", "b", "c", "d", "e", "FFF", 123, True)
print(f[0])

print("*" * 20, "元组切片", "*" * 20)
g = ("a", "b", "c", "d", "e", "FFF", 123, True)
print(g[1:-1:2])  # 元组切片返回元组

print("*" * 20, "元组常用操作：tuple.count('元素')，返回int型的元素个数", "*" * 20)
h = (1, 2, 3, 4, 4, 6, 7, 1)
print("元组h内含有元素4的个数为：", h.count(4))

print("*" * 20, "元组常用操作：tuple.index('元素')，返回当前元素的索引下标值，也是int类型", "*" * 20)
i = ("a", 123, "c", False, "你好", "666", False)
print("元组i里的元素'666'的索引下标为：", i.index("666"))
print("元组i里的元素'666'的索引下标为：", i.index(False, 1, 5))  # 从i[1]开始，到i[5]结束，寻找是否有元素False，没有会报错
print("元组i里的元素'666'的索引下标为：", i.index(False, 4, 9))  # 从i[4]开始到末尾查找False，9可以省略，也可以超出元组的index长度

print("*" * 20, "元组元素的查找：in 或者 not in", "*" * 20)
j = (1, 2, 3, "AAA")
if "AAA" in j:
    print("元素'AAA'在元组j里！")
else:
    print("元素'AAA'不在元组j里！")

print("*" * 20, "元组元素的遍历：for ...in ...", "*" * 20)
k = (1, 2, 3, "g", "3r")
for l in k:
    print(l, end="  ")
