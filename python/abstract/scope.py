#!/usr/bin/python


# 1) basic
scope = vars()
print scope

print '-'*30

x = 1

print scope
print scope['x']

scope['x'] += 1

print x

#2) 
def combine(parameter):
	print parameter,external

def combine2(parameter):
	print globals()['parameter'],external


def change_global():
	global x
	x = x + 1

external = 'world'
parameter = 'goodbye'

combine('hello')
combine2('hello')
print "before change_global, x=",x
change_global()
print "after change_global, x=",x

def multiplier(factor):
	def multiplyByFactor(number):
		return number*factor
	return multiplyByFactor

double = multiplier(2)
print double(5)

	
