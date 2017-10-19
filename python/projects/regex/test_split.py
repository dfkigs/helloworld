#!/usr/bin/python

import re

# re.split(pattern, string, maxsplit=0, flags=0)

# 1)  Split string by the occurrences of pattern
print "re.split('\W+', 'dog-cat- egg') = ", re.split('\W+', 'dog-cat- egg')
# ['dog', 'cat', 'egg']

print "re.split('cat', 'dog-cat- egg') = ", re.split('cat', 'dog-cat- egg')
# ['dog-',  '- egg']

print "re.split('dog', 'dog-cat- egg') = ", re.split('dog', 'dog-cat- egg')
#['', '-cat- egg']

# 2) If capturing parentheses () are used in pattern, then the text of all groups in the pattern are also returned as part of the resulting list
print "re.split('(\W+)', 'dog-cat- egg') = ", re.split('(\W+)', 'dog-cat- egg')
# ['dog', '-', 'cat', '- ', 'egg']

# If there are capturing groups in the separator and it matches at the start of the string, the result will start with an empty string. The same holds for the end of the string
print "re.split('(\W+)', '...words, words...') = ", re.split('(\W+)', '...words, words...')
#['', '...', 'words', ', ', 'words', '...', '']

# 3) If maxsplit is nonzero, at most maxsplit splits occur, and the remainder of the string is returned as the final element of the list
print "re.split('\W', 'one dog,two dog,three dog') = ", re.split('\W', 'one dog,two dog,three dog')
#['one', 'dog', 'two', 'dog', 'three', 'dog']
print "re.split('\W', 'one dog,two dog,three dog') = ", re.split('\W', 'one dog,two dog,three dog', 2)
# ['one', 'dog', 'two dog,three dog'] , the remainder of the string is returned as the final element of the list

# 4) flags
print "re.split('[a-f]+', '0aa3B9', flags=re.IGNORECASE) = ", re.split('[a-f]+', '0aa3B9', flags=re.IGNORECASE)
#['0', '3', '9']

# 5) split will never split a string on an empty pattern match
print "re.split('x*', 'foo') = ", re.split('x*', 'foo')
#['foo']
print "re.split('(?m)^$', 'foo\\n\\nbar\\n') = ", re.split('(?m)^$', 'foo\n\nbar\n')
#['foo\n\nbar\n']


