# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
装饰器带参数
"""


def outer_check(time):
    def check_time(action):
        def do_action():
            if time < 22:
                return action()
            else:
                return "对不起，您不具备该权限！"

        return do_action

    return check_time  # 此处返回check_time之后，为什么会执行check_time()，语句先后顺序该函数已经提前加载到内存了


@outer_check(21)
def play_game():
    return "玩游戏"


print(play_game())
