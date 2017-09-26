#!/usr/bin/python
from math import sqrt

# 1)  basic
names = ['dfkigs','zhangsan','lisi','wangwu']
tuples = (22222,33333,"adsdasdasda")
dists = {1:'dfkigs',2:'zhangsan',3:'lisi','foo':'bar'}

for name in names:
	print "hello",name

for param in tuples:
	print "hello",param

# dist is not sorted !
for key in dists:
	print "hello",key,dists[key]

# range
for number in range(0,11):
	print number


# 2) 
names = ['zhangsan','lisi','wangwu']
numbers = ['111111','222222','333333']
for i in range(len(names)):
	print names[i],numbers[i]

pbk = zip(names,numbers)
for name,number in pbk:
	print name,number

# 3) replace
strings = ['xxx','yyy','xxx','zzz','xxx','foo','bar']
for string in strings:
	if 'xxx' in string:
		index = strings.index(string)
		strings[index] = 'newword'

print strings

index = 0
strings = ['xxx','yyy','xxx','zzz','xxx','foo','bar']
for string in strings:
	if 'xxx' in string:
		strings[index] = 'newword'
	index += 1

print strings


strings = ['xxx','yyy','xxx','zzz','xxx','foo','bar']
for index,string in enumerate(strings):
	if 'xxx' in string:
		strings[index] = 'newword'

print strings

# 4) break  continue
for number in range(100,0,-1):
	root = sqrt(number)
	if root == int(root):
		print 'root=',root
		break




# expression for value in range(x,y)
print [x*x for x in range(0,10)]
print [x*'darkface' for x in range(0,10)]

# 
boys = ['zhangsan', 'lisi', 'wangwu', 'wangba']
girls = ['cuihua', 'xiaohong', 'xiaofang', 'xiaoyun']

print [b+'+'+g for b in boys for g in girls if b[0] > g[0]]

# same as  result = [(i,j) for i in range(0,4) for j in range(0,4)]
#result = []
#for i in range(0,4):
#	for j in range(0,4):
#		result.append((i,j))
#print result
result = [(i,j) for i in range(0,4) for j in range(0,4)]
print result

boys = ['cuijian', 'lisi', 'xiaogang']
girls = ['cuihua', 'xiaohong', 'lifang']
lettergirls = {}

for g in girls:
	lettergirls.setdefault(g[0],[]).append(g)
print lettergirls

print [b+'+'+g for b in boys for g in lettergirls[b[0]]]


