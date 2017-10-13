#!/usr/bin/python

__metaclass__ = type

#
# basic
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

# construction 
# deconstruction  __del__(self)
class FooBar:
	# construction function ,  begin & end with '__'
#	def __init__(self):
#		self.var = 10
	def __del__(self):
		print "del called"
	def __init__(self,value):
		self.var = value
	def hello(self):
		print "self.var=",self.var

f = FooBar(8)
f.hello()

class BaseClass:
	def __init__(self):
		print "from Baseclass"

class ChildClass(BaseClass):
	def __init__(self):
#		BaseClass.__init__(self)
		super(ChildClass,self).__init__()
		print "from ChildClass"
	pass

#b = BaseClass()
c = ChildClass()



