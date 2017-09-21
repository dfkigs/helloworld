#!/usr/bin/python

print('Hello World')
print('Hello World'.lower())

names = ['zhangsan', 'lisi', 'wangwu']
name = 'ZhangSan'
name2 = 'ZhangSan '

if (name in names):
 print "Found 1!"

if (name.lower() in names):
 print "Found 2, lower() works!"

if (name2.lower() in names):
 print "Found 3!"

if (name2.lower().strip() in names):
 print "Found 4, strip works!"

