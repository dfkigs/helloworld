#!/usr/bin/python

def checkIndex(key):
	if not isinstance(key,(int,long)):raise TypeError
#	if key<0: raise IndexError

class ArithMeticSequence:
	def __init__(self,start=0,step=1):
		self.start = start
		self.step = step
		self.change = {}
	
	def __len__(self):
		return 3

	def __getitem__(self,key):
		checkIndex(key)
		try :
			return self.change[key]
		except KeyError:
			return self.start + key*self.step

	def __setitem__(self,key,value):
		checkIndex(key)
		self.change[key] = value

s = ArithMeticSequence(1,5)
print s[4]
s[4] = 10

# __len__(self)
print len(s)

for i in range(4):
	print s[i]
