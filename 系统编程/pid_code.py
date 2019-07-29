#coding=utf-8

#导入系统模块
import os

#注意，fork函数只能在linux、unix、Mac上运行，windows不行

#创建进程
pid = os.fork()

if pid == 0:
    print("PID1")

else:
    print("PID2")

