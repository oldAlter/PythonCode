#coding=utf-8
import threading

from time import sleep,ctime

def sing():
    for i in range(3):
        print("正在唱歌...%d"%i)
        sleep(1)


def dance():
    for i in range(3):
        print("正在跳舞...%d"%i)
        sleep(1)


#程序入口
if __name__ == "__main__":
   
    print('---开始---：%s'%ctime())
    
#创建线程实例    
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

#启动线程
    t1.start()
    t2.start()

    sleep(5)
    print('---结束---:%s'%ctime())

#主线程会等待所有的子线程结束才结束。

