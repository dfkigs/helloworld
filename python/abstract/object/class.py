#!/usr/bin/python

__metaclass__ = type

#
# 
class Person:
	def setName(self,name):
		self.name = name
	def getName(self):
		return self.name
	def greet(self):
		print "Hello, I'm",self.name

	# private
	def __inaccessable(self):
		print "cannot see outside"
	# protected
	def _inaccessable2(self):
		print "cannot see outside 2"
	def accessable(self):
		self.__inaccessable()
		self._inaccessable2()
		print "can see outside"

def hello():
	print "Hello"

foo = Person()
bar = Person()

foo.setName("foo")
bar.setName("bar")

foo.greet()
bar.greet()

print foo.name
print bar.name

foo.greet = hello
foo.greet()

foo.accessable()
#foo.__inaccessable()
foo._Person__inaccessable()
#foo._Person_accessable2()
