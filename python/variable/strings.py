#!/usr/bin/python
from string import Template
from math import pi

# format string
format = "Hello, %s : %d : %f : %.3f"
name = "No"
number = 5
aFloat = 3.1415926
aTuple = ('No',1,1.222222,1.222222)
aList = ['No',2,1.2222,1.222222]

# only tuple can format more than one values !
print(format % (name,number,aFloat,aFloat))
print(format % aTuple)
# error :  print(format % aList)
print(format % (aList,3,111.2222,1.222222))

# display %
format = "Hello, %%s : %d"
print(format % 222)


# template string
print("template & substitute")
s = Template('$x you, $x me, $x you togother')
z = s.substitute(x='see')
print(z)
# s is unchanged
print(s)

# dictionary
s = Template('i have a $pen, i hava a $apple, $apple$pen')
# dictionary variable
d = {}
d['pen'] = 'pen'
d['apple'] = 'apple'
z = s.substitute(d)
print(z)

# template string example 
print("template string example ")
print('price of %s is: $%s' % ('eggs',15))
print('price of eggs is: $%d' % 15)
print('price of eggs is: $%f' % 3.1415)
print('price of eggs is: $%10.4f' % 3.1415)
print('price of eggs is: $%010.4f' % 3.1415)
print('price of eggs is: $%+10.4f' % -3.1415)

# find 
title = 'hello world, hello dfkigs'
# 1.substr
print(title.find('hello'))
# 2.substr, start
print(title.find('hello', 1))
# 3.substr, start , end
print(title.find('hello', 1, 3))



