#coding=utf-8

#导入os模块
import os

#创建进程
ret = os.fork()
print(ret)

if ret>0:
    print("---父进程--%d-"%os.getpid())
else:
    print("---子进程--%d-%d-"%(os.getpid(),os.getppid()))
