#!/usr/bin/python

# 1) define : 

print ("----------------------define---------------")
students = ["zhangsan", "lisi"]
teachers = ['wangss', 'ddd']
names = [students, teachers]
myname = "hello"
print (names)

# 2) op :
print ("----------------------OP---------------")

# size is n
# from 0 ~ n-1
print ("-----------pick---------")
print(students[0])
print(myname[1])
# or -1 is the last index ; then -2 ... -n
print(myname[-1])

# [m,n],  m <= x < n
print ("-----------[m,n],  m <= x < n---------")
numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers[3:6])
print(numbers[0:1])

# for last n items
print ("-----------for last n items---------")
print(numbers[-3:0])#[]
print(numbers[-3:-1])#[7,8]
print(numbers[-3:])#[7,8,9]

# from beginning
print ("-----------from beginning---------")
print(numbers[:3])#[0,1,2]

# for all items
print ("-----------for all items---------")
print(numbers[:])

# *****************  step 
print ("-----------step---------")
print(numbers[::1])  # default, step is 1
print(numbers[::4])	 # set to 4
print(numbers[::-2])	 # set to -2
print(numbers[0::-2])	 # set to -2
print(numbers[0:6:-2])	 # set to -2


# add
print ("-----------add---------")
d = 'd'
numbers = [1,2,3,4]
numbers2 = [['a','b','c'],[1,2,3],[1,2,2],[1,2]]
abcs = ['a','b','c',d]

print(numbers+abcs)

# multiply
print ("-----------multiply---------")
print(numbers * 3)
print([None] * 10)

# in
print ("-----------in---------")
print(4 in numbers)
print(5 in numbers)
print([1,3] in numbers)
print([1,2] in numbers)
print([1,2] in numbers2)


# len / min / max
print ("-----------len / min / max---------")
print(len(numbers))
print(len(numbers2))
print(min(numbers))
print(min(numbers2))


# redefine
print ("-----------redefine---------")
numbers[0] = 5
print(numbers)
numbers[2:] = ['a','b','c']
print(numbers)

# insert , numbers[1] will be 'z'
print ("-----------insert---------")
numbers[1:1] = ['z','z','z']
print(numbers)

# del
print ("-----------del---------")
del numbers[0]
print(numbers)

# append
print ("-----------append---------")
numbers.append(4)
print(numbers)

# count
print ("-----------count---------")
print(numbers.count('z'))

# extend, no return !!!
print ("-----------extend---------")
print(numbers.extend(numbers2))
print(numbers)

# index
print ("-----------index---------")
print(numbers.index('c'))
print(numbers.index([1, 2, 3]))

# insert function, no return !!!
print ("-----------insert function, no return---------")
numbers.insert(4,'ghh')
print(numbers)
numbers.insert(3,['ghh','zzd','abc'])
print(numbers)


# pop
print ("-----------pop---------")
print(numbers.pop())
print(numbers)

# remove, no return !!!
print ("-----------remove, no return--------")
numbers.remove('z')
print(numbers)

#reverse, no return !!!
print ("-----------reverse, no return---------")
numbers.reverse()
print(numbers)

print ("----------------------newnumbers---------------")
newnumbers = numbers
newnumbers2 = numbers[:]
print (newnumbers)
print (newnumbers2)

# sort
print ("-----------sort, no return---------")
numbers.sort()
print(numbers)

# after sort , newnumbers changed ,  newnumbers2 unchanged
print ("----------------------newnumbers after sort---------------")
print (newnumbers)
print (newnumbers2)

# special sort 
print ("-----------special sort ---------")
# numbers.sort(key=len)
# TypeError: object of type 'int' has no len()
atable = ['aaa', 'bb', 'cccc']
atable.sort(key=len)
print(atable)

numbers.sort(reverse=True)
print(numbers)


