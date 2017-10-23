#!/usr/bin/python

import re

# RegexObject
# has same param as matchObject without pattern, flags
# flags moved to compile
#  re.compile(pattern, flags=0)

# 2)  search(string[, pos[, endpos]])
# Scan through string looking for a location where this regular expression produces a match, and return a corresponding MatchObject instance
pattern = re.compile("foo")
m = pattern.search("this is a foo, that is a bar")
if m:
	print "pattern.search = ", m.group()

# 3)   match(string[, pos[, endpos]])
pattern = re.compile("foo")
m = pattern.match("this is a foo, that is a bar")
if m:
	print "pattern.match = ", m.group()
else:
	print "pattern.match = ", m

#  4)  split
#split(string, maxsplit=0)
pattern = re.compile(",")
m = pattern.split("one,two,three")
if m:
	print "pattern.split('one,two,three') = ", m

#  5) 
#findall(string[, pos[, endpos]])
pattern = re.compile("\w+")
m = pattern.findall('one,two,three')
if m:
	print "pattern.findall('one,two,three') = ", m

# 6 ) 
# sub(repl, string, count=0)
pattern = re.compile("old")
print pattern.sub("new", "one old, two old, three old", 2)

# 7) 
# subn(repl, string, count=0)
# 
pattern = re.compile("old")
print pattern.subn("new", "one old, two old, three old", 2)
# ('one new, two new, three old', 2)

# 8)
pattern = re.compile("dog", flags=re.IGNORECASE)
dogs = pattern.findall("one Dog, two dog, three DOG")
if dogs:
	print dogs


