#!/usr/bin/python
from copy import deepcopy

# without dict
names = ['zhangsan','lisi','wangwu','liumazi']
numbers = ['11111','22222','333333','444444']

print(numbers[names.index('wangwu')])


# dict
phonebook = {'zhangsan':'11111','lisi':'22222','wangwu':'333333','liumazi':'444444'}
print(phonebook)
print(phonebook['zhangsan'])

# dict(key='value',key2='value2' ......)
newphonebook = dict(zhangsan='11111',lisi='22222',wangwu='333333',liumazi='444444')
print(newphonebook)


# dict op
print (len(newphonebook))
print (newphonebook['wangwu'])
newphonebook['wangwu'] = '5555555'
print (newphonebook['wangwu'])
if ('wangwu' in newphonebook) :
	print 'wangwu in newphone'
	del newphonebook['wangwu']

if ('wangwu' in newphonebook) :
	print 'wangwu in newphone'


# empty dict
#x = []
#x[42] = '333'
#print(x)
#  IndexError: list assignment index out of range
y = {}
y[42] = '333'
print(y)


# use dict format  string
# ... %(key)s ... % dict
print("zhangsan's phonenumber is %(zhangsan)s." % newphonebook)

template = '''<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(content)s</p>
</body>
</html>
'''

data = {'title':'Hello everybody','content':'hello world'}
print(template % data)


# dict, functions
# clear
x = {}
y = x
x['key'] = 'value'
print (x)
print (y)

y = {}
print ("after y = {}")
print (x)
print (y)

y = x
y.clear()
print ("after y.clear()")
print (x)
print (y)

# copy
# y change, x unchange
x = {'name':'zhangsan','number':['111111','22222']}
y = x.copy()
y['name'] = 'lisi'
print (x)
print (y)

# y change, x unchange
y['email'] = 'zhangsan@163.com'
print (x)
print (y)

# y change, x change
y['number'].remove('111111')
print (x)
print (y)

# deepcopy
x = {'name':'zhangsan','number':['111111','22222']}
y = x.copy()
z = deepcopy(x)
x['number'].append('333333')

print (x)
print (y)
# z unchanged 
print (z)

# fromkeys
print({}.fromkeys(['name','age']))
print({}.fromkeys(['name','age'],'unknown'))

# get, get a empty key , 
d = {}
# error
#print (d['name'])
# return : None
print (d.get('name'))
print (d.get('name', 'N/A'))

# has_key
print(x.has_key('name'))

# items
print(x.items())
print(list(x.iteritems()))

# keys
print(x.keys())
print(list(x.iterkeys()))

# pop
x = {'name':'zhangsan','number':'111111'}
print(x)
print(x.pop('name'))
print(x)

# popitem , random pop
x = {'name':'zhangsan','number':'111111'}
print(x.popitem())
print(x)

# setdefault
# default value only changes at the first time
print('-' *20 + 'set default' + '-'*20)
x= {}
print(x.setdefault('name', 'N/A'))
print(x)
print(x.setdefault('name'))
print(x)

# update
print('-' *20 + 'update' + '-'*20)
name = {'name':'wangwu','number':'222222'}
number = {'number':'123456','email':'wangwu@163.com'}
print(name.update(number))
print(name)


# value
x = {'name':'zhangsan','number':['111111','22222']}
print(x.values())
print(list(x.itervalues()))

