#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    noOf5 = ( n/3 )
    remainderOf5 = n%3
    
    if ( remainderOf5 == 0 ):
        print '5'*noOf5*3
    elif ( n == 3 ):
        print '3'*noOf5*5
    elif ( noOf5 >= 1 ):
        for x in xrange(noOf5):
            if ( (3*(x+1) + remainderOf5 )%5 == 0 ):
                print '5'*(noOf5-x-1)*3 + '3'*(3*(x+1)+remainderOf5)
                break
            if ( x+1 == noOf5 ):
                print '-1'
                
    else:
        print '-1'
