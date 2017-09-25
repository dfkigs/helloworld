#!/usr/bin/python


# join,
# a.join(b)

sep=[1,2,3,4,5]
sep2=['1','2','3','4','5']
seq='+'
#seq.join(sep)
#TypeError: sequence item 0: expected string, int found
print(seq.join(sep2))
#1+2+3+4+5

seq2=['a','b']
seq3=('a','b')
#print(seq2.join(sep2))
#AttributeError: 'list' object has no attribute 'join'

#print(seq3.join(sep2))
#AttributeError: 'tuple' object has no attribute 'join'


# some examples:
paths = ['','home', "dfkigs", "work"]
print('/'.join(paths))
print('C:'+'\\'.join(paths))
