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
	print parameter+external

def combine2(parameter):
	print globals()['parameter'] + external

external = 'world'
parameter = 'goodbye'

combine('hello')
