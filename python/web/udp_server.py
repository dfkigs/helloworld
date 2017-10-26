#!/usr/bin/python
from socket import *
from time import ctime

HOST = '::1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSrvSock = socket(AF_INET6, SOCK_DGRAM)
udpSrvSock.bind(ADDR)

while True:
	print 'waiting for message...'
	data, addr = udpSrvSock.recvfrom(BUFSIZ)
	udpSrvSock.sendto('[%s] %s' % (ctime(), data), addr)
	print '...received from and return to add:',addr

udpSrvSock.close()
