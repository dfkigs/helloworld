#!/usr/bin/python

# don't check ####
# only 3n+2
# pieces is sorted, from small => big
def check_majong(pieces):
	if len(pieces) == 0:
		yield []
	elif len(pieces) == 2:
		if int(pieces[0]) == int(pieces[1]):
			yield [pieces[0] + pieces[1]]
#	elif len(pieces) == 4:
#		if (int(pieces[0]) == int(pieces[1])) and (int(pieces[0]) == int(pieces[2])) and (int(pieces[0]) == int(pieces[3])):
#			yield [pieces[0] + pieces[1] + pieces[2] + pieces[3]]
	else:
		for i in range(len(pieces)):
			# skip same piece
			if i > 0 and pieces[i] == pieces[i-1]:
				continue
			for j in range(i+1,len(pieces)):
				# skip same piece
				if j > i+1 and pieces[j] == pieces[j-1]:
					continue
				for k in range(j+1,len(pieces)):
					# skip same piece
					if k > j+1 and pieces[k] == pieces[k-1]:
						continue
					new_pieces = pieces[:]
					del(new_pieces[i],new_pieces[j-1],new_pieces[k-2])
					if int(pieces[i]) == int(pieces[j]) and int(pieces[i]) == int(pieces[k]):
						for ret in check_majong(new_pieces):
							yield [pieces[i] + pieces[j] + pieces[k]] + ret
					elif int(pieces[k]) == int(pieces[j]) + 1 and int(pieces[j]) == int(pieces[i]) + 1:
						for ret in check_majong(new_pieces):
							yield [pieces[i] + pieces[j] + pieces[k]] + ret

def sort_result(result):
	for r in result:
		r.sort()
		yield r

def delete_redundant_result(result):
	l_result = list(sort_result(result))
	ret = []
	for i in l_result:
		found = False
		for j in ret:
			if j == i:
				found = True
				break
		if not found:
			ret.append(i)
	print ret

delete_redundant_result(check_majong(list('11122233388')))

