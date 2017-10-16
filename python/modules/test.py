#!/usr/bin/python

import hello
import sys, pprint
import myprint
import copy

#pprint.pprint(sys.path)
print myprint.PI


x = [n for n in dir(copy) if not n.startswith('_')]
print x

print copy.__all__
