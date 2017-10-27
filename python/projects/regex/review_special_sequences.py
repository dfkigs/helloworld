#!/usr/bin/python
import re

# 1)   \b  , search for a word's border
# \b itself matches a empty string ; used at the end/start of a word
def test_backslashed_lower_b(tables):
	for string in tables:
		m = re.search('\\bword\\b', string)
		if m: yield string

# 2) \B, not at the end or start of a word
# itself matches a empty string
def test_backslashed_upper_b(tables):
	for string in tables:
		m = re.search('\\Bword\\B', string)
		if m: yield string

tables = [' word', 'word ', ' word ', ',word', 'word,', ',word,', 'Aword', 'wordD', '_word_', 'words', 'aword', 'swords', 'word']
ret = test_backslashed_lower_b(tables)
print "string in ", tables
print "re.search('\\bword\\b', string) = ", list(ret)

ret = test_backslashed_upper_b(tables)
print "re.search('\\Bword\\B', string) = ", list(ret)


# 3) \A  matches only at the start of the string
#  \Z  matches only at the end of the string
# \b matches the border,  
# so
#  'ZZZword'  matches r'\Aword' , not matces r'\bword'
#  ',word'  matches r'\Aword' , matces r'\bword'
# 'wordZZZ'  matches r'word\Z' , not matces r'word\b'
# 'word,'  matches r'word\Z' , matces r'word\b'
def test_backslashed_upper_a(tables):
	for string in tables:
		m = re.search('\\Aword', string)
		if m: yield string

def test_backslashed_upper_z(tables):
	for string in tables:
		m = re.search('word\\Z', string)
		if m: yield string


tables = ['aword', 'word', 'a word\nword', 'wordzzz', 'word,dd']
ret = test_backslashed_upper_a(tables)
print "string in ", tables
print "re.search('\\Aword', string) = ", list(ret)
ret = test_backslashed_upper_z(tables)
print "re.search('word\\Z', string) = ", list(ret)

# 4) 
# \d , same as r'[0-9]'
# \D, same as r'[^0-9]' character
# \s, matches any whitespace character  r'[\t\n\r\f\v]'
# \S, matches any non-whitespace character  r'[^\t\n\r\f\v]'
# \w, [0-9a-zA-Z_]
# \W, [^0-9a-zA-Z_]
m = re.search(r'\d\s\D', '1\n ')
if m:
	print m.group()




