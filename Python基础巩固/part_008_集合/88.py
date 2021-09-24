#!/usr/bin/python3
# -*- coding:utf-8 -*-
dict = [{"name":"laoli","age":17,"sex":"男"},{"name":"laojiang","age":15,"sex":"女"}]
for i in dict:
    if i["name"] == "laoli" and i["sex"] == "男":
        i["age"] += 1
print(dict)