#!/usr/bin/python

import re
import string

#prog = re.compile(pattern)
#result = prog.match(string)

prog = re.compile("o")

# # No match as "o" is not at the start of "dog".
#print "prog.match(\"dog\") = ", prog.match("dog")
#print "prog.match(\"dog\", 1) = ", prog.match("dog", 1)

#print re.split("\W+", "dog-cat- egg")
#print re.split("(\W+)", "dog-cat- egg")
#(?m)^$
#print re.split("^$", "dog?cat?egg")

m = re.findall("\w+", "this is a dog, that is a dog")
print m

m = re.finditer("\w+", "this is a dog, that is a dog")
for i in m:
	print i.group()

print re.escape('python.exe')

legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
print '[%s]+' % re.escape(legal_chars)

operators = ['+', '-', '*', '/', '**']
# sub
def dashrepl(matchobj):
	if matchobj.group(0) == '-':
		return ' '
	else:
		return '-'

# the leftmost non-overlapping occurrences of pattern in string
print re.sub('-{1,2}', dashrepl, 'pro----gram-files')

def printmatch(matchobj):
	print matchobj.group()
	return 'dark'

print re.sub('(\w+,)?', printmatch, 'pro,gram,files,')

m = re.match('(\w+,)?', 'pro,gram,files,')
if m:
	print m.group()



print re.escape('python.exe')
print map(re.escape, ['*'])
for i in map(re.escape, ['*']):
	print i

legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
print re.escape(legal_chars)
print '[%s]+' % re.escape(legal_chars)

operators = ['+', '-', '*', '/', '**']

print map(re.escape, sorted(operators, reverse=True))

print '|'.join(map(re.escape, sorted(operators, reverse=True)))


