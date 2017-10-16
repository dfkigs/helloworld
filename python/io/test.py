#!/usr/bin/python
import fileinput
import sys

def process(value):
	print "process:",value

f = open("input.txt")

while True:
	c = f.read(1)
	if not c:
		break
	else:
		process(c)

while True:
	l = f.readline()
	if not l:
		break
	else:
		process(l)

for c in f.read():
	process(c)

for l in f.readlines():
	process(l)


# file is iterable.
for l in f:
	process(l)

f.close()

print list(open("input.txt"))

for l in open("input.txt"):
	process(l)

for line in fileinput.input('input.txt'):
	process(line)
