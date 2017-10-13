#!/usr/bin/python

# keyword :  yield
def flatten(nested):
	for sublist in nested:
		for element in sublist:
			yield element


def flatten_recursion(nested):
	try:
		try:
			nested + ''
		except TypeError:
			pass
		else:
			raise TypeError
		for sublist in nested:
			for element in flatten_recursion(sublist):
				yield element
	except TypeError:
		yield nested

nested = [[1,2],[3,4],[5]]

nested2 = [[1,2],[3,4],5]
nested3 = [[1,2],[3,4],[5,6,[7,8]]]
nested4 = [[1,2],[3,4],[5,6,[7,8]],'test']


print "nested"
for n in flatten(nested):
	print n
print list(flatten(nested))

print "nested2"
for n in flatten_recursion(nested2):
	print n
print list(flatten_recursion(nested2))

print "nested3"
for n in flatten_recursion(nested3):
	print n
print list(flatten_recursion(nested3))

print "nested4"
for n in flatten_recursion(nested4):
	print n
print list(flatten_recursion(nested4))

# fib
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b=b,a+b
		n += 1

print fib(5)

# run steps
def odd():
	print 'step 1'
	yield 1
	print 'step 2'
	yield 2
	print 'step 3'
	yield 3

o = odd()
print o.next()


#



