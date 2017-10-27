#!/usr/bin/python
import re

# 1)   flags 
# re.compile(pattern, flags=0)
# Compile a regular expression pattern into a regular expression object


# flags  A) re.DEBUG
# re.DEBUG  ,   display debug information about compiled expression
pattern = re.compile(r'\w+', flags=re.DEBUG)
m = pattern.search('this is a foo')
if m:
	print m.group()

# flags  B) re.I ,  re.IGNORECASE  ,  (?i)
# re.I
# re.IGNORECASE
# re.compile(r'XXX', flags=re.I) same as re.compile(r'(?i)XXX')
m1 = re.search('(?i)Total', 'total')
m2 = re.search('Total', 'total', flags=re.IGNORECASE)
if m1 and m2:
	print m1.group(),m2.group()


# flags  C)  re.L , re.LOCALE
# make \w \W \s \S \b \B dependent on the current locale
# re.U, re.UNICODE
# Make the \w, \W, \b, \B, \d, \D, \s and \S sequence s dependent on the Unicode 

# flags d) re.M , re.MULTILINE
# same as (?m)
# usually use with '^'
# m = re.search('(?m)^line', 'line one\nline two')
# even multiline flag is set
# match function will only match the first line at the beginning
m1 = re.search('^line', 'one\nline two', re.MULTILINE)
m2 = re.match('^line', 'one\nline two', re.MULTILINE)
if m1:
	print "re.search('^line', 'one\nline two', re.MULTILINE) =", m1.group()
if m2:
	print m2.group()
else:
	print "re.match('^line', 'one\nline two', re.MULTILINE) =", m2

# match None
# m = re.search('^line', 'one\nline two')

# flags e) re.S , re.DOTALL
# make the . matches all character at all , include new line
 

# flags f)  re.X ,  re.VERBOSE
# allow you write regular expressions that look nicer and more readable by allowing you to add whitespace and comments 
# white space in pattern is ignored. except in [] or after \






