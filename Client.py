# -*- coding: utf-8 -*-
import socket

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect(('127.0.0.1',8888))

#ss.sendall('filter&&1')
#ss.sendall('water purify&&1')
ss.sendall('3972061&&2')
ss.send('EOF')
data = ss.recv(20480)
print(data)
ss.close()
