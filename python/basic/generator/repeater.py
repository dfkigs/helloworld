#!/usr/bin/python

def repeater(value):
	while True:
		new = (yield value)
		if new is not None: value = new

r = repeater(24)
print r.next()
print r.next()


def flatten_recursion(nested):
	result = []
	try:
		try:
			nested + ''
		except TypeError:
			pass
		else:
			raise TypeError
		for sublist in nested:
			for element in flatten_recursion(sublist):
#				yield element
				result.append(element)
	except TypeError:
#		yield nested
		result.append(nested)

	return result


nested = [[1,2],[3,4],[5,6,[7,8]],'test']

result = flatten_recursion(nested)

print result

