#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    count=0
    n = str(n)
    for x in xrange(len(n)):
        digit = int( n[x:x+1] )
        #print "Digit: ", digit
        if ( digit != 0 ):
            if ( int(n)%digit == 0 ):
                count += 1
    print count
            
