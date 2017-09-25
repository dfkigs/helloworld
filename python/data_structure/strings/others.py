#!/usr/bin/python

# replace
print('this is a dog'.replace('dog','cat'))

# strip
print('__' + ' long long ago   ' + '___')
print('__' + ' long long ago   '.strip() + '___')

names = ['zhangsan', 'lisi', 'wangwu']
name = 'ZhangSan '

if (name in names):
 print "Found 1!"

if (name.lower().strip() in names):
 print "Found 2, strip works!"

# strip(XXX)
print('XXXthis is a new XXX worldXXX')
print('XXXthis is a new XXX worldXXX'.strip('XXX'))

