#!/usr/bin/python
from socket import *
from time import ctime

HOST = 'localhost'
#HOST = '::1'
#HOST = '172.16.1.88'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

#tcpSerSock = socket(AF_INET6, SOCK_STREAM)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
	print('waiting for connection...')
	tcpCliSock, addr = tcpSerSock.accept()
	print '...connected from :',addr

	while True:
		data = tcpCliSock.recv(BUFSIZ)
		if not data:
			break
		tcpCliSock.send('[%s] %s' % (ctime(), data))
#		tcpCliSock.send('[%s] %s' % (bytes(ctime(), 'utf-8'), data))
	tcpCliSock.close()

tcpSerSock.close()
