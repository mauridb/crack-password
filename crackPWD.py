import os, sys, shutil, logging
import random

from datetime import datetime as dt
from termcolor import colored as c


ALPH_CHAR = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
LOW_UP = [0,1]
PWD = ''.join([ALPH_CHAR[random.randrange(len(ALPH_CHAR))].upper() if LOW_UP[random.randrange(len(LOW_UP))] is 0 else ALPH_CHAR[random.randrange(len(ALPH_CHAR))].lower() for index in range(0,5)])
print c('Password generated!!','blue')

# if status 1 break loop and return pwd broken!!!
STATUS_PWD = 0


attempts = 0
dt_start = dt.now()
while STATUS_PWD == 0:
	attempts += 1
	TMP_PWD = ''.join([ALPH_CHAR[random.randrange(len(ALPH_CHAR))].upper() if LOW_UP[random.randrange(len(LOW_UP))] is 0 else ALPH_CHAR[random.randrange(len(ALPH_CHAR))].lower() for index in range(0,5)])
	print c('WARNING: attempt #{}'.format(str(attempts)),'yellow')
	print c('password #{}'.format(TMP_PWD),'cyan')
	if TMP_PWD == PWD:
		STATUS_PWD = 1
		print c('!ALERT: password broken..','red')
		break
dt_end = dt.now()
delta_time = dt_end - dt_start
result = str(delta_time.total_seconds())

# revers time to cut milliseconds because milliseconds always are six chars
result = result[::-1]
print c('TIME SPENT: {}s'.format(result[7::]), 'red')





print c('ATTEMPTS: {}'.format(str(attempts)), 'red')
print PWD
