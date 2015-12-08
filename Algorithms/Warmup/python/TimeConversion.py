#!/bin/python

import sys


time = raw_input().strip()
timeOfDay = time[-2:]
if (timeOfDay == "AM"):
    if ( int(time[0:2]) == 12 ):
        print str("00") + time[2:8] 
    elif ( int(time[0:2]) < 10 ):
        print '0' + str( int(time[0:2]) ) + time[2:8] 
    else:
        print str( int(time[0:2]) ) + time[2:8]
else:
    if ( int(time[0:2]) == 12 ):
        print time[0:8]
    else:
        print str( int(time[0:2])+12 ) + time[2:8] 
