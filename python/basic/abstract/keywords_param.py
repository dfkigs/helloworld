#!/usr/bin/python

# 1 )  
def hello(greeting, name):
	print '%s %s!' % (greeting, name)

def hello2(greeting='hello2', name='world'):
	print '%s %s!' % (greeting, name)
#hello('hello', 'world')

def print_params(*params):
	print params

def print_params2(title, *params):
	print title
	print params

def print_params3(**params):
	print params

def print_params4(x,y,z,*param1,**param2):
	print x,y,z
	print param1
	print param2

hello(name='world', greeting='hello')
hello2()

print_params('tests')
print_params2('tests',1,2,3)
print_params3(x=1,y=2,z=3)
print_params4(1,2,3,7,bar=6)


def test(x):
	print x

def test2(x,y=1):
	print x,y

#  SyntaxError: non-default argument follows default argument
#  def test3(x=1,y):

test(100)
test2(200,y=5)
# test2(y=5,200)
# SyntaxError: non-keyword arg after keyword arg

# 2) 
def add(a,b):
	return a+b

param = (3,4)
print add(param[0],param[1])
print add(*param)

def say_hello(name,number):
	print name,number

#  key ==> function's param name
#  value ==> function's param value
param = {'name':'zhangsan','number':'13421232229'}
say_hello(**param)



