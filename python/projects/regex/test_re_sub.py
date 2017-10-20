#!/usr/bin/python
import re
# sub(pattern, repl, string, count=0, flags=0)


# 1) simple
# foo == > bar
# just same as replace
print("this is a foo".replace('foo','bar'))
print re.sub("foo", "bar", "this is a foo")

# 2) foo,bar => zoo
print re.sub("\d+foo|bar", "zoo", "this is a 123foo, that is a bar")

# 3) sub can use function as repl
def replfuc(matchobject):
	if matchobject.group() == 'foo':
		return 'Foo'
	elif matchobject.group() == 'bar':
		return 'Bar'
	else:
		return ''

print re.sub("foo|bar", replfuc, "this is a foo, that is a bar")

# 4) can only replace part of the matches
print re.sub("old", "new", "one old, two old, three old", 2)

# 5) flags just same as search , match, 
print re.sub("old", "new", "one OLD, two Old, three olD, four old", 3, flags=re.IGNORECASE)

# ********************
# 6)
# subn , has same params with sub , but return a tuple ('newstring', count)
print re.subn("old", "new", "one OLD, two Old, three olD, four old", 3, flags=re.IGNORECASE)
# ('one new, two new, three new, four old', 3)


# 7) sub & group
def printmatch(matchobj):
	print matchobj.group() # the last match :  files,
	return 'replaced' 

# each match will be replaced :
# replacedrreplacedreplaced
print re.sub('(\w+,)?', printmatch, 'pro,gram,files,')




