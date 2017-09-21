#!/usr/bin/python

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
