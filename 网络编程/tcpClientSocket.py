#创建tcp客户端
# -*- coding:UTF-8-*-

#coding=uft-8
from socket import *

#创建socket
tcpClientSocket = socket(AF_INET, SOCK_STREAM)

#链接服务器
serAddr = ('192.168.1.102', 7788)
tcpClientSocket.connect(serAddr)

#提示用户输入数据
sendData = raw_input("请输入要发送的数据:")

tcpClientSocket.send(sendData)

#接受对方送过来的数据，最大接收1024个字节
recvData = tcpClientSocket.recv(1024)
print ('接收到的数据为：' + recvData)


#关闭套接字

tcpClientSocket.close()
