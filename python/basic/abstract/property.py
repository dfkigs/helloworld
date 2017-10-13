#!/usr/bin/python

__metaclass__ = type

class Rectangel:
	def __init__(self):
		self.width = 0
		self.height = 0

	def setSize(self,size):
		self.width,self.height = size

	def getSize(self):
		return self.width,self.height

#	property (fget,fset,fdel,doc)
	size = property(getSize,setSize)

r = Rectangel()
r.size = (10,20)
print r.size

class Rectangel2:
	def __init__(self):
		# self.width ==> __setattr(self,width,0)
		self.width = 0
		self.height = 0

	def __setattr__(self,name,value):
		if name == 'size':
			self.width,self.height = value
		else:
			self.__dict__[name] = value
		
	def __getattr__(self,name):
		if name == 'size':
			return (self.width,self.height)
		else:
			return self.__dict__[name]


r2 = Rectangel2()
print "r2.getattr('size'):",r2.size
r2.size = (10,20)
print "r2.getattr('size'):",r2.size

