#!/usr/bin/python

def factorial(n):
	if n < 1:
		return 0
	elif n == 1:
		return 1
	else:
		return n*factorial(n-1)

n = input("Input N:")

def power(x,n):
	if n < 1:
		return 0
	elif n == 1:
		return x
	else:
		return power(x,n-1)*x

def power2(x,n):
	result = 1
	for i in range(n):
		result *= x
	return result
		

print factorial(n)
print power(5,n)
print power2(5,n)

