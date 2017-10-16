#!/usr/bin/python

def drawChessBoard(queen):
	for pos in queen:
		print '[ ]'* pos + '[*]' + '[ ]' * (len(queen)-1-pos)
		pass
		
def drawQueens(queens):
	while True:
		try:
			queen = queens.next()
			print queen
			drawChessBoard(queen)
		except StopIteration:
			break

def conflict(state,nextX):
	nextY = len(state)
	for i in range(nextY):
		# 0, same col; nextY - i, in diagonal
		if (abs(state[i]-nextX) in (0,nextY-i)):
#			print state,nextX,"conflict"
			return True
#	print state,nextX,"not conflict"
	return False

# yield the possible poses to (A,B,...)
def queens(num,state=()):
	if len(state) == num-1:
		for pos in range(num):
			if not conflict(state, pos):
#				print (pos,)
				yield (pos,)
	# not the last line,
	else:
		for pos in range(num):
			# find not conflict line, 
			if not conflict(state, pos):
				# recursion search the next lines
				for result in queens(num,state+(pos,)):
					# since recursion,  result must be at the end
#					print (pos,) + result
					yield (pos,) + result

# queens(4) is a generator
x = queens(4)
drawQueens(x)

