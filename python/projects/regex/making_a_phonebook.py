#!/usr/bin/python
import re

text = """Ross McFluff: 834.345.1254 155 Elm Street

Ronald Heathmore: 892.345.3428 436 Finley Avenue

Frank Burger: 925.541.7625 662 South Dogwood Way


Heather Albrecht: 548.326.4584 919 Park Place"""


entries = re.split('\n+', text)
print entries

for entry in entries:
	name = re.split('(?: )', entry, 3)
	print name

