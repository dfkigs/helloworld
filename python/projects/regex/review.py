#!/usr/bin/python
import re

# 1)  '\\\\'  in pattern string
# A) 
#  to match a literal \, one might have to write '\\\\' as the pattern string
#  pattern string  '\\\\'  ==> regular expression '\\'  ==> match literal '\'
#  string '\\'  ==> literal '\'

# B) 
#  error information , if use '\\' in pattern string: 
#  m = re.search("\\", "\\helloworld")  , if use '\\' in pattern string , 
#  return _compile(pattern, flags).search(string)

#  C)
# so the reason is :
m = re.search("\\\\", "\\helloworld")
if m:
	print m.group()

# D) raw string notation
# you can use r'\\'  ==> regulat expression '\\'  ==> match literal '\'
# r"\helloworld"  ==> literal string :  '\','h','e',......
m = re.search(r"\\", r"\helloworld")
# m = re.search(r"\\", "\\helloworld")
if m:
	print m.group()


#  2)
#   '.' match any character except new line '\n'; but if flags re.DOTALL is set, '.' can match any character
m = re.search(".", "\n", flags=re.DOTALL)
if m:
	print "before new line:",m.group(),"end"

# ^ binder for start
# $ binder for end
m = re.search('line$', 'first line')
if m:
	print "re.search('line$', 'first line') =", m.group()

m = re.search('^line', 'line one')
if m:
	print "re.search('^line', 'line one') = ", m.group()

# * match 0~ n times of preceding RE
# will match a , ab, abbbb ......
# + match 1~n times of preceding RE
# will match ab, ab.....b
# {m,n}  , match m~n times of preceding RE
# {m} , match m times of preceding RE
m = re.search('ab*', 'aaaaa')
if m:
	print "re.search('a*', 'aaaaa') = ", m.group()

# ? match 0 or 1 repetitions of preceding RE
# a or ab

#  3)  greedy & non-greedy
# greedy * + ?
# non-greedy *? +? ??
m = re.search('<.*>', '<a>b<c>')
if m:
	print "re.search('<.*>', '<a>b<c>') = ", m.group()

m = re.search('<.*?>', '<a>b<c>')
# same result : .*? .+? .?? 
#m = re.search('<.*?>', '<a>b<c>')
#m = re.search('<.*?>', '<a>b<c>')
if m:
	print "re.search('<.*>?', '<a>b<c>') = ", m.group()

# greedy  ==> non-greedy   {m,n}  ==> {m,n}?
# {m,n}? 
m = re.search('a{1,4}', 'aaaaaaaa')
if m:
	print "re.search('a{1,4}', 'aaaaaaaa') = ", m.group()
m = re.search('a{1,4}?', 'aaaaaaaa')
if m:
	print "re.search('a{1,4}?', 'aaaaaaaa') = ", m.group()


# 4) 
#  []
# a)  [awk] => match 'a' 'w' 'k'
# b)  [a-z] ==> matchs 'a' to 'z'
# c)  [a\-z], [-a], [a-] ,  the '-' will be regard as a literal '-'
m = re.search('[a-]', '-awk')
if m:
	print "re.search('[a-]', 'awk') = ", m.group()

# *** d) special chars will lost their special meaning inside sets.
# 
# [(.+*?)]  will match '(', ')', '.', '+', '*', '?'
m = re.search('[(.+*?)]', '(.+*?)')
if m:
	print "re.search('[(.+*?)]', '(.+*?)') = ", m.group()

#[()[\]{}]
# only  ']' is special in '[]'
m = re.search('[()[\]{}]', r'{}')
if m:
	print m.group()

# \w , \S
# \w, \S ... ... is ok in []
m = re.search('[\w]+', 'words')
if m:
	print "re.search('[\w]+', 'words') = ", m.group()

# ^ is the first character in [] set; 
# or it's a iteral character
m = re.search('[^567]+', '890')
if m:
	print "re.search('[^567]+', '890') = ", m.group() # 890

# 5) 
# A|B
# | is never greedy !!!  ************   | is never greedy 
# if A matched . never match B
m = re.search('ab|cd', 'abd')
if m:
	print "re.search('ab|cd', 'acd') = ", m.group()


# 6)
# (...)  & \number
#  ************    \\number   or r'\number'
m = re.search(r'(a)b\1', 'aba')
#m = re.search('(a)b\\1', 'aba')
if m:
	print "re.search('(a)bbb\\1', 'aba') = ", m.group()

