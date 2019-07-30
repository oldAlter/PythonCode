#coding=utf-8

#封装Thread方法，用类来执行线程
import threading
import time

class MyThread(threading.Thread):
    #重写run方法
    def run(self):
        for i in range(3):
            time.sleep(1)
            #name属性保存当前的线程的名字
            msg = "I'm " + self.name + "@" + str(i)

            print(msg)

if __name__ == '__main__':
    t = MyThread()
    t.start()

