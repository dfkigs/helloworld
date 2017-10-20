#!/usr/bin/python

import re

#  search  > match
# 0) search    !!! Scan through string !!!
# search(pattern, string, flags=0)
# Scan through string looking for the first location where the regular expression pattern produces a match, and return a corresponding MatchObject instance

# 0) match ,  !!! at the beginning of string !!!
# match(pattern, string, flags=0)
#  If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding MatchObject instance


# ******(1)*********
# match
# return a MatchObject
match = re.match('(\w+)', 'dog&cat&another dog')

# Match objects always have a boolean value of True. Since match() and search() return None when there is no match, 
# you can test whether there was a match with a simple if statement
if match:
	print match.group(0)

m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
if m:
	# ******(2)*********
	#  group([group1, ...])
	# Returns one or more subgroups of the match
	# ******************
	print m.group()  # 'Isaac Newton'
	print m.group(0)  # 'Isaac Newton'
	print m.group(1) # 'Isaac'
	print m.group(2) # 'Newton'
	print m.group(1,2)# ('Isaac', 'Newton')

# ******(3)*********
# (?P<name>...) 
m = re.match(r"(?P<firstname>\w+) (?P<lastname>\w+)", "Isaac Newton, physicist")
if m:
	# group([group1, ...])
	# Returns one or more subgroups of the match
	print m.group()  # 'Isaac Newton'
	print m.group(0)  # 'Isaac Newton'
	print m.group('firstname') # 'Isaac' , same as m.group(1)
	print m.group('lastname') # 'Newton' , same as m.group(2)
	print m.group('firstname','lastname')# ('Isaac', 'Newton')
	print m.group('lastname','firstname')# ('Newton', 'Isaac')

# ****(4)************
# if a group matches multiple times, only the last match is accessible
m = re.match(r"(dog)+","DogdogDOG", flags=re.IGNORECASE)
if m:
	print m.group()
	print m.group(1)#the last match is accessible

# ******** (5)**************
# groups ,  not group
#  groups([default])
#  groups 's param is default, not the same as group
# *********
m = re.match(r"(dog)+","DogdogDOG", flags=re.IGNORECASE)
if m:
	print m.group()
	print m.group(1)
	print m.groups()

m = re.match(r"(\d+)([A-Za-z]+)(\d+)","123Dog456", flags=re.IGNORECASE)
if m:
	print m.group()
	print m.groups()

m = re.match(r"(\d)+([A-Za-z])+(\d)+","123Dog456", flags=re.IGNORECASE)
if m:
	print m.group() # 123Dog456
	print m.group(1) # 3
	print m.group(2) # g
	print m.group(3) # 6
	print m.groups() # ('3', 'g', '6')


m = re.match(r"(\d+)([A-Za-z]+)(\d+)?","123Dog", flags=re.IGNORECASE)
if m:
	print "m.groups() = ", m.groups() # ('3', 'g', None)
	print "m.groups() = ", m.groups('Not Matched') # ('3', 'g', 'Not Matched')


# ******** (6)**************
# groupdict
#  groupdict([default])
#  Return a dictionary containing all the named subgroups of the match, keyed by the subgroup name
# groupdict 's param is same as groups
# *********
m = re.match(r"(?P<digital>\d+)(?P<word>[A-Za-z]+)(?P<anotherdigital>\d+)","123Dog111", flags=re.IGNORECASE)
if m:
	print "m.groupdict() = ", m.groupdict() # {'word': 'Dog', 'digital': '123'}

m = re.match(r"(?P<digital>\d+)(?P<word>[A-Za-z]+)(?P<anotherdigital>\d+)?","123Dog", flags=re.IGNORECASE)
if m:
	print "m.groupdict() = ", m.groupdict("Zero") # {'word': 'Dog', 'digital': '123'}


# ******** (7)**************
# start([group])
# end([group])
# span([group])
email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)
#  [start, end)  
print m.start(),m.end()
print email[m.start():m.end()]
print email[:m.start()] + email[m.end():]
print m.span()

# ******** (8)**************
# findall & finditer
# end
# findall(pattern, string, flags=0)
# Return all non-overlapping matches of pattern in string, as a list of strings
m = re.findall("\w+", "this is a dog, that is a dog")
print m
# ['this', 'is', 'a', 'dog', 'that', 'is', 'a', 'dog']

# finditer(pattern, string, flags=0)
# Return an iterator yielding MatchObject instances over all non-overlapping matches for the RE pattern in string
m = re.finditer("\w+", "this is a dog, that is a dog")
for obj in m:
	# obj is a MatchObject instance
	print obj.group()


