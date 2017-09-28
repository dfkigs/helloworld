#!/usr/bin/python

'''
basic code
storage = {}
storage['first'] = {}
storage['middle'] = {}
storage['last'] = {}

print storage

me = 'zhang san feng'

storage['first']['zhang'] = [me]
storage['middle']['san'] = [me]
storage['last']['feng'] = [me]

my_sister = 'liu san jie'
storage['first'].setdefault('liu',[]).append(my_sister)
storage['middle'].setdefault('san',[]).append(my_sister)
storage['last'].setdefault('jie',[]).append(my_sister)

print storage['middle']['san']
print storage
'''

def init(data):
	data['first'] = {}
	data['middle'] = {}
	data['last'] = {}

def lookup(data,label,name):
#	print data[label].get(name)
	return data[label].get(name)

# full_name must be XX YY ZZ
# no check below
def store(data,full_name):
	names = full_name.split()
	labels = ['first','middle','last']
	for name,label in zip(names,labels):
		people = lookup(data,label,name)
		if people:
			people.append(full_name)
		else:
			data[label][name] = [full_name]

storage = {}
init(storage)
#store(storage, 'zhang san feng')
#store(storage, 'liu san jie')

def new_store(data,*full_name):
	labels = {'first', 'middle', 'last'}
	for names in full_name:
		a_name = names.split()
		for name,label in zip(a_name,labels):
			people = lookup(data,label,name)
			if people:
				people.append(names)
			else:
				data[label][name] = [names]

new_store(storage, 'liu san jie','zhang san feng','wang san dan')
print storage





