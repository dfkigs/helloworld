#!/usr/bin/python
import re

# count24 is ok
# re is not ok

def count24(number, result):
	if len(number) == 1:
		if number[0] == result:
			yield str(number[0])
	elif len(number) == 2:
		if (number[0] + number[1]) == result:
			yield str(number[0])+'+'+str(number[1])
		elif (number[0] - number[1]) == result:
			yield str(number[0])+'-'+str(number[1])
		elif (number[1] - number[0]) == result:
			yield str(number[1])+'-'+str(number[0])
		elif (number[1] * number[0]) == result:
			yield str(number[0])+'*'+str(number[1])
		elif number[1] > number[0] and (number[1] % number[0]) == 0 and (number[1] / number[0]) == result:
			yield str(number[1])+'/'+str(number[0])
		elif number[0] > number[1] and (number[0] % number[1]) == 0 and (number[0] / number[1]) == result:
			yield str(number[0])+'/'+str(number[1])
	else:
		length = len(number)
		for i in range(length):
			# number[i] + eval(ret) = result  ==> new_result ==  eval(ret) == result - number[i]
			# number[i] - eval(ret) = result  ==> new_result ==  eval(ret) == number[i] - result
			# eval(ret) - number[i] = result  ==> new_result ==  eval(ret) == result + number[i]
			# number[i] * eval(ret) = result  ==> new_result ==  eval(ret) == result / number[i]
			# eval(ret) / number[i] = result  ==> new_result ==  eval(ret) == result * number[i]
			# number[i] / eval(ret) = result  ==> new_result ==  eval(ret) == number[i]/result
			if result >= number[i]:
				for ret in count24(number[0:i]+number[i+1:length], result - number[i]):
					yield str(number[i]) + '+' + '(' + ret + ')'

			if number[i] >= result:
				for ret in count24(number[0:i]+number[i+1:length], number[i] - result):
					yield str(number[i]) + '-' + '(' + ret + ')'

			for ret in count24(number[0:i]+number[i+1:length], result + number[i]):
				yield '(' + ret + ')' + '-' + str(number[i])

			if number[i] and result >= number[i] and (result % number[i]) == 0:
				for ret in count24(number[0:i]+number[i+1:length], result / number[i]):
					yield str(number[i]) + '*' + '(' + ret + ')'

			for ret in count24(number[0:i]+number[i+1:length], result * number[i]):
				yield '(' + ret + ')' + '/' + str(number[i])

			if result and number[i] >= result and (number[i] % result) == 0:
				for ret in count24(number[0:i]+number[i+1:length], number[i] / result):
					yield str(number[i]) + '/' + '(' + ret + ')'


# re test
# how to solve () 
'''
# del parenthese
	(anything) ==> data   ok
	+(anything)$ ==>  +anything$
	+(anything)+
	+(anything)- 
	
===>

	-(data+data)^ ==> +data+data
	-(data-data)^ ==> +data-data
	-(data+data)+ ==> +data+data
	-(data-data)+ ==> +data-data
	-(data+data)- ==> +data+data
	-(data-data)- ==> +data-data


# change order
	+data+data ==> +big+small
	-data+data ==> +data-data
	data+(XX) ==> (XX)+data
	data*(XX) ==> (XX)*data

def del_parenthese(expression):
	ret = re.sub(r'(?<![*/(-])\((.*)\)(?![*/)])', r'\1', expressions)
	return ret

def del_parenthese_generator(expressions):
	for e in expressions:
		yield re.sub(r'(?<![*/(-])\((.*)\)(?![)*/])', r'\1', e)

'''

print list(set(list(del_parenthese_generator(count24([3,5,6,7],24)))))
print list(set(list(del_parenthese_generator(count24([4,5,6,7],24)))))
print list(set(list(del_parenthese_generator(count24([2,5,6,7],24)))))
print list(set(list(del_parenthese_generator(count24([9,5,6,7],24)))))


