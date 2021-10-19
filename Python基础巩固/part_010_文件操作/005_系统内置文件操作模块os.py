#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os

"""
OS模块：主要对文件和目录进行操作
常用方法：
os.mdkir()：创建目录
os.removedirs()：删除目录或文件
os.getcwd()：获取当前目录
os.path.exists(dir or file)：判断文件或目录是否存在
os.path.dirname(__file__)：返回当前文件所在目录的绝对路径
os.path.join(str1,str2)：字符串拼接
"""
# 获取当前文件所在目录的完整路径，返回一个字符串
print(os.path.dirname(__file__))

# 获取当前目录
print(os.getcwd())

# 在当前目录创建文件夹"testdir"，再次执行会报错，提示文件已存在
os.mkdir("testdir")

# 列出当前目录或指定目录所有的文件和文件夹，返回一个列表
print(os.listdir("./"))

# 删除目录或文件，同理再次执行会报错，提示文件不存在
os.removedirs("testdir")

if not os.path.exists("b"):  # 判断当前目录是否存在目录b
    os.mkdir("b")  # 不存在则创建

if not os.path.exists("b/test.txt"):  # 如果目录b下没有test.txt
    file = open("b/test.txt", "w")  # 则创建并打开test.txt，文件权限为w时理解为打开b目录下的test.txt文件，不存在则新建一个
    file.write("你好，我是test.txt文件")  # 往文件test.txt里写入字符串

# 将目录123.jpg文件复制到当前文件所在目录，建立两个文件流，分别链接2个文件，一个读取原文件内容，一个将内容写入目标文件
with open("/Users/liyong/Downloads/123.jpg", "rb") as stream2:
    content1 = stream2.read()
    # 获取文件名
    name = stream2.name
    file_name = name[name.rfind("\\")+1:]  # str.rfind("str")从右至左查找str，返回当前index，加1一直截取到末尾，得到文件名
    path = os.path.dirname(__file__)  # 获取当前文件所在目录的绝对路径，返回字符串
    full_path = os.path.join(path, file_name)  # os.path.join(str1,str2)，字符串拼接方法，得到文件的完整路径
    with open(full_path, "wb") as stream3:
        stream3.write(content1)

print("完成文件复制")
