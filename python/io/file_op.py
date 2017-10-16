#!/usr/bin/python

# open
# 'r' , 'w' , 'a' , 'b' , '+'
# 
# 
#	open in mode "w",  the file content will be lost.
# 
# open(filename, mode, buffer)
# if buffer is not 0, the file will change after close(),flush called

# read only
def test_readonly():
	#	r is default, the same as f = open('input.txt')
	f = open('input.txt', 'r')
	print f.read(-1)
	print f.tell()
	f.close()

# write only, the file's old content will lost.
def test_writeonly():
	f = open('input.txt', 'w')
	f.write("write only")
	f.close()

# append
#
def test_append():
	f = open('input.txt', 'a')
	f.write("append")
	f.close()

# binary
# can be add to "r" 'w' 'a'
def test_binary():
	f = open('input.txt', 'ab')
	f.write("binary append")
	f.close()

# read or write
# error :  'rw' 
def test_read_plus():
	f = open('input.txt', 'r+')
	print f.read(-1)
	f.write("read_plus added\n")
	f.close()

# read or write
# error :  'rw' 
# write and read, the file's old content will lost.
def test_write_plus():
	f = open('input.txt', 'w+')
	print f.read(-1)
	f.write("write_plus_added\n")
	f.close()

def test_readline():
	f = open('input.txt', 'r')
	print f.readline()
	f.close()
	
def test_readlines():
	f = open('input.txt', 'r')
	print f.readlines()
	f.close()

def test_writelines():
	lines = ['first line\n', 'second\n', 'third\n']
	f = open('input.txt', 'w')
	f.writelines(lines)
	f.close()
	
test_writelines()



