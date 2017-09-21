#!/usr/bin/python

width = input("Input width :")
price_width = 10
item_width = width - price_width 

head_format = '%-*s%*s'
data_format = '%-*s%*.2f'

print (head_format % (item_width,'item',price_width,'price'))
print (width * '=')
print (data_format % (item_width,'apple',price_width,6.48))
print (data_format % (item_width,'egg',price_width,3.98))
print (data_format % (item_width,'pear',price_width,4.28))
print (data_format % (item_width,'orange',price_width,8.181))


