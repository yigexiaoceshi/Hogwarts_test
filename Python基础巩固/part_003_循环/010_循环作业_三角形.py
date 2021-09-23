#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
示例1：使用while循环打印出三角形
*
**
***
****
*****
"""
print("~~~~~~~~~~~写法1~~~~~~~~~~~~")
n = 1  # 循环次数和每次循环打印的星星数一致，所以定义一个变量即可
while n < 6:
    print("*" * n)
    n += 1

print("~~~~~~~~~~~写法2~~~~~~~~~~~~")
m = 1  # 定义循环次数
while m < 6:
    l = 0  # 定义在嵌套循环的外层，表明每个嵌套while的l都是从0开始，然后执行l += 1
    while l < m:  # 定义每个循环打印的星星数，循环第一次m=1，l只有一个取值0，循环一次一个*，m=2，l有2个取值0和1，循环2次2个*，类推
        print("*", end="")  # 每一次小循环取消换行
        l += 1  # 控制小循环次数，即星星数
    m += 1  # 控制循环次数
    print()  # 每一次大循环换行一次

print("~~~~~~~~~~~写法1：打印倒三角形~~~~~~~~~~~~")
g = 1
while g < 6:
    print((6 - g) * "*")
    g += 1

print("~~~~~~~~~~~写法2：打印倒三角形~~~~~~~~~~~~")
i = 1
while i < 6:
    j = 6
    while i < j:
        print("*", end='')
        j -= 1
    i += 1
    print()

"""使用for循环打印三角形"""
print("~~~~~~~~~~~for循环：打印三角形~~~~~~~~~~~~")
for a in range(1, 6):
    print("*" * a)

print("~~~~~~~~~~~for循环：打印倒三角形~~~~~~~~~~~~")
for b in range(1, 6):
    print("*" * (6 - b))
