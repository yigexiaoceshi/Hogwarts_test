# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
高阶函数：
1、函数A作为函数B的参数，则函数B称为高阶函数
2、函数A作为函数B的返回值，则函数B称为高阶函数
"""
from functools import reduce

# 常见系统高阶函数

# 求一个序列的最大值：函数参数的返回值用来指定比较大小的字段
m = max(5, 0, 4, 9)
print(m)
m = max([1, 2, 4, 3, 8, 3, 9, 20])
print(m)
list1 = [("tom", 10, 90), ("rose", 18, 98), ("jack", 20, 89), ("lucy", 17, 95)]  # 依次是姓名，年龄，考试分数
m = max(list1)
print(m)
m = max(list1, key=lambda x: x[1])  # key函数，相当月遍历list1，每次遍历的元素(即元组)作为参数给x，返回x[1]，找出年龄最大的
print("年龄最大的是：", m)

# 求一个序列的最小值：函数参数的返回值用来指定比较大小的字段
list2 = [("tom", 10, 90), ("rose", 18, 98), ("jack", 20, 89), ("lucy", 17, 95)]  # 依次是姓名，年龄，考试分数
mi = min(list2, key=lambda x: x[2])  # 早出分数最低的
print("分数最低的是：", mi)

# 用来对一个无序列表进行排序：函数参数的返回值规定按照元素的哪个属性进行排序
list3 = [("tom", 10, 90), ("rose", 18, 98), ("jack", 20, 89), ("lucy", 17, 95)]  # 依次是姓名，年龄，考试分数
s = sorted(list3, key=lambda x: x[2], reverse=True)  # 按照分数降序排列
print("按照分数降序排列：", s)

# 用来过滤一个列表里符合规定的所有元素，得到的结果是一个迭代器：函数参数的返回值必须为bool类型，且为真时，为元素满足的过滤条件
list4 = [("tom", 10, 90), ("rose", 18, 98), ("jack", 20, 89), ("lucy", 17, 95)]  # 依次是姓名，年龄，考试分数
f = filter(None, list4)  # 返回一个可迭代对象
print(list(f))
f = filter(lambda x: x[1] > 18, list4)  # lambda表达式里的返回值x[1]>18为真的数据过滤出来，返回一个可迭代对象
print(list(f))

# 将列表里的每一项数据都执行相同的操作，得到的结果是一个迭代器：返回参数的返回值指定列表里元素所执行的操作
list5 = [("tom", 10, 90), ("rose", 18, 98), ("jack", 20, 89), ("lucy", 17, 95)]  # 依次是姓名，年龄，考试分数
map1 = map(lambda x: x[1] + 1, list5)  # 将年龄提取出来，并且都加1
print(list(map1))
map2 = map(lambda x: x[0].title(), list5)  # 提取姓名，首字母大写
print(list(map2))

# 对一个序列进行压缩运算，得到一个值(Python3后，该方法被移到了functools模块)：函数参数的返回值用来指定元素按照哪种方式合并
list6 = [("tom", 10, 90), ("rose", 18, 98), ("jack", 20, 89), ("lucy", 17, 95)]  # 依次是姓名，年龄，考试分数
map3 = map(lambda x: x[1] + 1, list6)
print(list(map3))
r = reduce(lambda x, y: x + y, [11, 19, 21, 18])  # 返回x+y即求列表各元素累加，如果求各元素累积相乘则返回x*y
"""
循环1：x,y=11,19；循环2：x,y=x+y,21；循环3：x,y=x+y,18，所以最终返回x+y=69
循环1：x,y=11,19；循环2：x,y=30,21；循环3：x,y=51,18，最终返回x+y=69，就是个累加的过程，前面2个数之和加上后面一项，一直加到末尾
"""
print(r)

# zip()，自行熟悉
list7 = [("tom", 10, 90), ("rose", 18, 98), ("jack", 20, 89), ("lucy", 17, 95)]  # 依次是姓名，年龄，考试分数
z = zip(list7)
print(list(z))