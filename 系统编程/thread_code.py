#coding=utf-8

import threading

import time

def attackDamage():
    print('平A')
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        #创建线程实例
        t = threading.Thread(target=attackDamage)
        #启动线程
        t.start()

