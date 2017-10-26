#!/usr/bin/python
from socket import *

HOST = '::1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET6, SOCK_DGRAM)

while True:
	data = raw_input('> ')
	if not data:
		break
	udpCliSock.sendto(data, ADDR)
	data, ADDR = udpCliSock.recvfrom(BUFSIZ)
	if not data:
		break
	print data

udpCliSock.close()


