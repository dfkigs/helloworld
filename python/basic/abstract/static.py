#!/usr/bin/python

__metaclass__ = type

class MyClass:
	# self
	def normal_method(self):
		print "this is a normal function"

	# cls
	@classmethod
	def class_method(cls):
		print "this is a class method of class:",cls
	#cmeth = classmethod(cmeth)

	# no self or cls
	@staticmethod
	def static_method():
		print "this is a static function"
#	smeth = staticmethod(smeth)    same as @staticmethod
	#smeth = staticmethod(smeth)

	@staticmethod
	def test_method(self):
		print "this is a test function"

# all ok
m = MyClass()
m.normal_method()
m.class_method()
m.static_method()

# 
# error TypeError: unbound method normal_method() must be called with MyClass instance as first argument (got nothing instead)
# MyClass.normal_method()
MyClass.normal_method(m)
MyClass.class_method()
MyClass.static_method()

# 
MyClass.test_method(m)
# TypeError: test_method() takes exactly 1 argument (0 given)
m.test_method()


