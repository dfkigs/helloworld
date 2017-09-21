#!/usr/bin/python

phonebook = {
	'zhangsan' : {
		'number' : '1111111',
		'email' : 'zhangsan@163.com'
	},
	'lisi' : {
		'number' : '2222222',
		'email' : 'lisi@163.com'
	},
	'wangwu' : {
		'number' : '33333333',
		'email' : 'wangwu@163.com'
	},
}

options = {'e':'email','n':'number'}

name = raw_input('Please input name:')
option = raw_input('which do you want, email (e) or number (n)?')
key = options[option]

if (name in phonebook) :
	print("%s's %s is %s" % (name,key,phonebook[name][key]))
else :
	print("%s is not found in phonebook" % name)

#print(phonebook)
