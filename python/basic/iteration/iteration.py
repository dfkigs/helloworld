#!/usr/bin/python

class Fibs:
	def __init__(self):
		self.a = 0
		self.b = 1

	def next(self):
		self.a,self.b = self.b,self.a+self.b
		return self.a

	def __iter__(self):
		return self


fibs = Fibs()
for f in fibs:
	print f
	if f>100:
		break


class TestIteration:
	value = 0
	def next(self):
		self.value += 1
		if self.value > 10: raise StopIteration
		return self.value
	
	def __iter__(self):
		return self

t1 = TestIteration()
print list(t1)
# print t1
# <__main__.TestIteration instance at 0x7fdaf9a44c68>
		
