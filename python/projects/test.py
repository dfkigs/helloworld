#!/usr/bin/python
import logging
from ConfigParser import ConfigParser

CONFIGFILE = "python.txt"

config = ConfigParser()
config.read(CONFIGFILE)

print config.get('messages','greeting')

radius = input(config.get('messages','question')+' ')
print config.get('messages', 'result_message'),
print config.getfloat('numbers', 'pi') * radius**2


f = open('log.txt','w')
print >> f, "hello world"


logging.basicConfig(level=logging.INFO, filename='logging.txt')
logging.info('start programmer')
logging.info('try to divide 1 by 0')
print 1/0
logging.info('divide success')
