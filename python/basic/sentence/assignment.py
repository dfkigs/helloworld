#!/usr/bin/python

# assignment
# 1)  
x,y = 1,2

# 1 2 
print x,y
# (1, 2)
print (x,y)

# exchange x,y
x,y = y,x
print x,y

phonebook = {'name':'zhangsan',"number":'1234567'}
contact = phonebook.popitem()
print contact

# 2) 
print ('-'*10 + 'x=y=somefunction()')
phonebook = {'name':'zhangsan',"number":'1234567'}
x = y = phonebook.popitem()
print (x)
print (y)
x = phonebook.popitem()
print (x)
print (y)

# 3) x, y , x=y, change x , y change or not ?
print ('-'*10 + 'x=(1,2), then x=(2,3)')
x = (1,2)
y = x
# x point to (2,3) , but y is still point to (1,2)
x = (2,3)
print (x)
print (y)

print ('-'*10 + 'x changed to a new dict, y unchanged')
x = {1:'ddd',2:'zzz'}
y = x
x = {3:'zdd',4:'222'}
print (x)
print (y)

print ('-'*10 + 'x changed value, y changed too')
x = {}
y = x
x['key'] = 'value'
print (x)
print (y)


# 3)
# += -= ... *=

