#!/usr/bin/python

aTuple = (1,2,3,'a','ddd','zz')
emptyTuple = ()

print(aTuple)
print(emptyTuple)

# only one value's tuple
print("only one value's tuple")
oneValueTuple = (222,)
faultOneValueTuple = (222)
print(oneValueTuple)
print(faultOneValueTuple)


# functions
print('abc')
print(tuple(('abc',)))
print(tuple('abc'))
print(list('abc'))

# list \  string \ tuple
a = 1,2,3,'a','b'
b = (1,2,3,'d','e')
c = "123ab"
print(a)
print(b)
print(c)
print(list(c))
