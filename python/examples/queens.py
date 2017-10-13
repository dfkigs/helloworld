#!/usr/bin/python


# n * n == > 0~n-1
def drawChessBoard(row,col):
	for i in range(row):
		print col*'[ ]'

#drawChessBoard(8,8)

def conflict(state,nextX):
	nextY = len(state)
	for i in range(nextY):
		if (abs(state[i]-nextX) in (0,nextY-i)):
			return True
	return False
# 
def queens(num,state=()):
	for pos in range(num):
		if not conflict(state,pos):
			if len(state) == num - 1:
				yield(pos,)
			else:
				for result in queens((num),state+(pos,)):
					yield(pos,)+result

for i in range(8):
	print "i=",i,len(list(queens(i)))
