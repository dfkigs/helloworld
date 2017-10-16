#!/usr/bin/python
import sys

# cat words.txt | ./somescriptes.py
text = sys.stdin.read()
words = text.split()
wordcount = len(words)

print "wordcount:",wordcount
