# -*- coding: utf-8 -*-
__author__ = 'zy008'
#导入socket库
import socket

#创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
#建立连接
s.connect(('www.sina.com.cn',80));
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#接收数据
buffer=[]
while True:
    #最多每次接受1K数据
    d = s.recv(1024)
    if d:
         buffer.append(d)
    else:
         break
data = b''.join(buffer)
#关闭连接
s.close()
print(data.decode('utf-8'))
'''
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)'''
if __name__ == '__main__':
    pass