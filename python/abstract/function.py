#!/usr/bin/python

def add(x,y):
	return x+y

def hello(name):
	return 'hello. ' + name + '!'

def fibs(nums):
	'Calculates the fibs'
	results = [0,1]
	for i in range(nums-2):
		results.append(results[-2] + results[-1])
	return results

def return_none():
	return

def change_param1(value):
	value = 'changed value'

def change_param2(value):
	value[0] = 'dddd'
	
def inc(x):
	return x+1

def inc_value(x):
	x[0] += 1

print add(10,20)
print hello('dfkigs')
print fibs(2)
print fibs(4)
print fibs.__doc__
#print help(fibs)
print return_none()

name = 'value'
change_param1(name)
print name

name = ['value', 'value2']
change_param2(name)
print name

name = ['value', 'value2']
change_param2(name[:])
print name

foo = [10]
inc_value(foo)
print foo

