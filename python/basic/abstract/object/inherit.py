#!/usr/bin/python

def foo(x):
	return x*x

bar = lambda x:x*x

print foo(5)
print bar(5)

class Filter:
	def init(self):
		self.blocked = []
	def filter(self,sequence):
		return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
	def init(self):
		self.blocked = ['SPAM']

f = Filter()
f.init()
print f.filter([1,2,3])

s = SPAMFilter()
s.init()
print "s.filter(['SPAM','foo','bar'])=",s.filter(['SPAM','foo','bar'])

# True
print "issubclass(SPAMFilter,Filter)=",issubclass(SPAMFilter,Filter)

# False
print "issubclass(Filter,SPAMFilter)=",issubclass(Filter,SPAMFilter)

print SPAMFilter.__bases__

print "isinstance(s,SPAMFilter)=",isinstance(s,SPAMFilter)
print "isinstance(s,Filter)=",isinstance(s,Filter)


class Calculator:
	def calculate(self,expression):
		self.value = eval(expression)
	def hi(self):
		print "hi from Calculator"

class Talker:
	def talk(self):
		print "hi, my value is ", self.value
	def hi(self):
		print "hi from Talker"

# function hi depend by the order : Calculator,Talker
class TalkingCalculator(Calculator,Talker):
	pass

tc = TalkingCalculator()
tc.calculate("5+6*3")
tc.talk()
# hi from Calculator
tc.hi()
print "hasattr(tc,'talk')",hasattr(tc,'talk')
print "hasattr(tc,'calculate')",hasattr(tc,'calculate')
print "hasattr(tc,'hello')",hasattr(tc,'hello')


