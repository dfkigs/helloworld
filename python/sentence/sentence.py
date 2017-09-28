#!/usr/bin/python

# statement block, start with :  
from math import sqrt

# boolean
# False, None, 0, "", {}, (), []
print bool(False)
print bool(None)
print bool(0)
print bool("")
print bool({})
print bool(())
print bool([])


# if / else / elif
#x = raw_input("Which case do you want? if (i) or else (e) or elif (f):")
x = 'i'
if (x == 'i') :
	print "Hello X"
elif (x == 'e') :
	print "Hello Y"
else :
	print "Hello Z"

# condition
# == != > >= < <= 
# is .   is not  . not in . in
x = (1,2)
y = (1,2)
z = x
i = 1
if (x == y):
	print ("x==y")
else:
	print ("x!=y")

if (x is y):
	print ("x is y")
elif (x is not y):
	print ("x is not y")
else:
	print ("x y ?")

if (x == z):
	print ("x==z")

if (x is z):
	print ("x is z")
elif (x is not z):
	print ("x is not z")
else:
	print ("x z ?")

if (i in (1,2)):
	print ("1 in (1,2)")
if (i in [1,2]):
	print ("1 in [1,2]")
if (i in {1:'AAA',2:'BBB'}):
	print ("1 in {1:'AAA',2:'BBB'}")


#  python can use x < y < z
if (1<x<10):
	print "helloworld"

# assert
assert(True)
#assert(False)


# while
i = 0
while i < 5 :
	print "Hello:i=",i
	i += 1

# 
name = ''
while not name:
	name = raw_input("please input your name:")

print name


# pass del  exec
i = 0
if i < 0:
	print 'i < 0'
elif i > 0:
	pass
# without pass , will cause error: IndentationError: expected an indented block
elif i == 0:
	print 'i == 0'

x = [1,2,3]
y = x
del x
print y

print eval(raw_input("enter an expression: "))


# scope
scope = {}
exec "sqrt = 1" in scope
print sqrt(4)
#print scope

exec 'x = 2' in scope
print eval('x*x', scope)



