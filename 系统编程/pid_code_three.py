#coding=utf-8

import os
import time

# fork函数不能再windows运行

#第一次创建进程
pid = os.fork()

if pid == 0:
    print("lol1")

else:
    print("lol2")

#第二次创建进程
pid = os.fork()

if pid == 0:
    print("lol3")

else:
    print("lol4")
