#!/usr/bin/python
import re

# 1) (?iLmsux)
#  (?iLmsux)
# a)  (?i), (?L) ...... match empty string
# b)  the letters set the corresponding flags:
#  i ==> re.I,  ignore case
#  L ==> re.L, locale ; Make \w, \W, \b, \B, \s and \S dependent on the current locale
#  m ==> re.M , multiple line
#  s ==> dot match All, include \n
#  u ==> unicode
#  x ==> verbose
#  m = re.search('Total', 'total', re.I)
#  
m = re.search('(?i)Total', 'total')
if m:
	print m.group()

m = re.search('(?m)^line', 'one\nline two')
if m:
	print m.group()

# without (?s), match None
m = re.search('(?s)a.+b', 'a\nb')
if m:
	print m.group()

# x, verbose
#m = re.search(r"""(?x)\d +  # the integral part
#				\.    # the decimal point
#				\d *  # some fractional digits""", '78.90')
# basic
m = re.search('\d+\.\d*', '78.90')
if m:
	print "basic:", m.group()
# Whitespace within the pattern is ignored
m = re.search('(?x)\d + \. \d * ', '78.90')
if m:
	print "with whiteapce:", m.group()

# can add comment
m = re.search('''(?x)\d + #  any data
				 \.  # \. ==> dot
			     \d * '''  # any data or not
				, '78.90')
if m:
	print "with comment:", m.group()

# 2)  (?: ...)
m = re.search(r'(?:a)b', 'abaa')
# sre_constants.error: bogus escape: '\\1'
#m = re.search(r'(a)b\1', 'aba')
if m:
	print m.group()


# 3) (?P<name>...)  & (?P=name)
# the substring matched by the group is accessible via the symbolic group name name
# A symbolic group is also a numbered group
m = re.search(r'(?P<A>a)(?P<B>b)', 'aba')
if m:
	print m.group('A'), m.group(1)
	print m.group('B'), m.group(2)

# (?P=name)
# the example below , matchs a pair of \' or \" 
m = re.search(r'(?P<quote>[\'\"]).*?(?P=quote)', '\'zhangsan\'')
#m = re.search(r'(?P<quote>[\'\"]).*?(?P=quote)', '\"lisi\"')
if m:
	print m.group()


# 4)  (?# ...)
# comment
m = re.search(r'\d+(?#match some digitals)', '2333')
if m:
	print m.group()

# 5)  (?=...)   &   (?!...)
# (?=...)    only matches  (if next matches ...)
# m = re.search('dark(?=face)', 'darkeyes') ,  not matches
m = re.search('dark(?=face)', 'darkfaces')
if m:
	print "re.search('dark(?=face)', 'darkfaces') =", m.group()
	# dark matches

# (?!...)  only matches  (if next not matches ...)
m = re.search('dark(?!face)', 'darkeyes')
if m:
	print "re.search('dark(?!face)', 'darkeyes') =", m.group()
	# dark matches

# (?<=...) & (?<!...)
# (?<=...)  match pre suffix ...
m = re.search(r'(?<=abc)def','abcdefabc')
if m:
	print m.group()# def

# m = re.search('(?<=\d+)\.\d', '99.88')
# look-behind requires fixed-width pattern
m = re.search('(?<=\d{2})\.\d+', '99.88')
if m:
	print m.group()# .88

# (?<!...)  pre suffix not matches ...
m = re.search(r'(?<!abc)def','ddddefabc')
if m:
	print m.group()



