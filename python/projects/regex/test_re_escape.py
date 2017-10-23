#!/usr/bin/python

import re
import string

# escape(pattern)
# Escape all the characters in pattern except ASCII letters and numbers

print "re.escape('python.exe') = ", re.escape('python.exe')

# list, tuple \ ==> \\
print "map(re.escape, ['*']) = ", map(re.escape, ['*'])
for i in map(re.escape, ['*']):
	print "i in map(re.escape, ['*']) ,i= ", i


legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
print re.escape(legal_chars)
print '[%s]+' % re.escape(legal_chars)


operators = ['+', '-', '*', '/', '**']
print map(re.escape, sorted(operators, reverse=True))
print '|'.join(map(re.escape, sorted(operators, reverse=True)))
