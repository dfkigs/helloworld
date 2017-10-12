#!/usr/bin/python
import exceptions

#print dir(exceptions)
try:
	raise Exception
except Exception:
	print "Exception raised"

try:
	x = 10/'a'
except ZeroDivisionError:
	print "integer division by zero"
except TypeError:
	print "TypeError"


try:
	x = 10/'a'
except (ZeroDivisionError,TypeError), e:
	print "error:",e


while True:
	try:
		x = input("input x:")
		y = input("input y:")
# if a Exception will be raise:
#  print "x/y=",x/y ,   ','
#  the log will be : 
#  x/y= Error: integer division or modulo by zero
#  so, usually, we must use  '+' instead
#		print "x/y=",x/y
		print "x/y="+str(x/y)
# Error: integer division or modulo by zero
	except Exception,e:
		print "Error:",e
		print "Please try again!"
	else:
		print "else"
		break;
	finally:
		print "finally"
