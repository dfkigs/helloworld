#!/usr/bin/python
from string import maketrans

# basic table
#print(maketrans('',''))

# c => k , s 
table = maketrans('cs','kz')
print(len(table))

print(table[97:123])
print(maketrans('', '')[97:123])

print('this is a book,that is a cat'.translate(table))
# delete second param in string
print('this is a book,that is a cat'.translate(table, ' '))


