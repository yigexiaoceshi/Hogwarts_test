#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
global：可变数据类型才需要加global关键字，可变数据类型不需要添加
"""
# 全局变量
a = 100


def func1():
    # 局部变量：作用范围仅限函数内部
    a = 0  # 先找函数体内是否有变量，如果有则覆盖全局变量的值直接使用，如果没有则到函数体外找全局变量并引用
    b = 8
    print("a=", a)
    print("b=", b)


func1()


def func2():
    b = 9
    print("a=", a)  # 此处使用的是全局变量
    print("b=", b)


func2()


def func3():
    # b = a - 10  # 仅拿全局变量做计算是可以的，只要不改变a的值
    global a  # 必须先声明全局变量，然后再赋值
    a += 11  # =号右侧a+11没有问题，但是赋值给a相当于要改变全局变量的值，所以必须加global
    b = a - 10
    print("改为全局变量后a：", a)
    print("b = ", b)


func3()

def func4():
    print("此时a的值是：", a)


func4()


def func5():
    list1 = [1, 2, 3]
    return list1


print(func5())

"""
定义函数1：is_login，参数username和password，函数体判断是否登录，登录返回True，未登录返回False
定义函数2:borrow_book，参数book_name，函数体 判断是否登录，登录可借，未登录不可借
"""
print("******************************************************")

login = False


def is_login(username, password):
    if username == "admin" and password == "1234":
        global login  # 改为全局变量，才会更改函数体外变量login的值
        login = True
    else:
        print("登录失败！")


def borrow_book(book_name):
    if login:
        print(f"{book_name}可以借阅！")
    else:
        print("用户未登录，不可借书！")
        username = input("请输入登录用户名：")
        password = input("请输入登录密码：")
        is_login(username, password)


borrow_book("红楼梦")
borrow_book("红楼梦")
