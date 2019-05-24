# -*- coding: utf-8 -*-
__author__ = 'zy008'
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

for data in [b'zhang',b'yang',b'Ada']:
    #发送数据
    s.sendto(data,('127.0.0.1',9999))
    #接收数据
    r=s.recv(1024).decode('utf-8')
    print(r)
s.close()
if __name__ == '__main__':
    pass