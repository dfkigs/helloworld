#!/usr/bin/python

def story(**kwds):
	return 'Once upon a time, there was a %(job)s called %(name)s.' % kwds

def power(x,y,*others):
	if others:
		print 'Received redundant parameters:', others
	return pow(x,y)

def interval(start, stop=None, step=1):
	if stop is None:
		start, stop = 0, start
	result = []
	i = start
	while i < stop:
		result.append(i)
		i += step
	return result


print story(job='king',name='dfkigs')
print story(name='dfkigs',job='king')
params = {'name':'dfkigs','job':'king'}
print story(**params)
del params['job']
print story(job='farmer',**params)

print power(y=4,x=2)
print power(2,5)
param = (2,6)
print power(*param)
param = [2,9]
print power(*param)
param = {'x':2,'y':7}
print power(**param)
param = (5,)*5
print power(*param)

print interval(10)
print interval(1,5)
print interval(2,9,2)
print (power(*interval(2,5)))





