#!/usr/bin/python

# L is  iterable,  but it's not a iterator
L = [1,2,3,4,5,6]

print [2*x for x in L]
# TypeError: list object is not an iterator
# print next(L)

# I is a iterator
I = iter(L)
print I
print list(I)

# ***
# after list(I), I will be at the end
I = iter(L)

# 1
print next(I)
# 2
print next(I)
# 3
print next(I)
# 4
print next(I)

#
for i in I:
	print 2*i
