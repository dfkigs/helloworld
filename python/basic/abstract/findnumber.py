#!/usr/bin/python
import random

r = random.randint(0, 100)

def find(x):
	if x == r:
		print "found , r=",r
		return True
	elif x < r:
		print "too small"
	else:
		print "too big"
	return False

# enable below code , when need test
#while True:
#	x = input("Please guess: r = ?")
#	if find(x):
#		break

def search_number(sequence,number,lower=0,upper=None):
	if upper == None:
		upper = len(sequence) - 1

	if lower > upper:
		return -1
	elif lower == upper:
		if number == sequence[upper]:
			return upper
		return -1
	else:
		middle = (lower+upper)/2
		if number > sequence[middle]:
			return search_number(sequence,number,middle+1,upper)
		elif number == sequence[middle]:
			return middle
		else:
			return search_number(sequence,number,lower,middle)


def search_number2(sequence,number):
	lower = 0
	upper = len(sequence) - 1

	while True:
		if lower == upper:
			if number == sequence[lower]:
				return lower
			return -1
			
		middle = (lower+upper)/2
		if (number == sequence[middle]):
			return middle
		elif number < sequence[middle]:
			upper = middle
			continue
		else:
			lower = middle+1
			continue

seq = [18,29,33,65,8,7,9,23,89,72]
seq.sort()

print seq
number = input("input number:")
print number
print search_number(seq,number)
print search_number2(seq,number)



