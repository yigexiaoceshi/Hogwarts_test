# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
装饰器带参数
"""


def outer_check(time):  # 第一层：接收装饰器的参数
    def check_time(action):  # 第二层：接收原函数
        def do_action():  # 第三层：接收原函数的参数
            if time < 22:
                return action()
            else:
                return "对不起，您不具备该权限！"

        return do_action  # 返回第三层

    return check_time  # 返回第二层


@outer_check(21)
def play_game():
    return "玩游戏"


print(play_game())
