#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

for x in xrange(1,1000):
    if ( len(arr) == 1 ):
        print len(arr)
        break
    elif ( len(arr) == 0 ):
        break
    else:
        print len(arr)
        minValue = min(arr)
        arr[:] = [ z for z in arr if z != minValue ]
        arr[:] = [ y-minValue for y in arr]
        
        
        
    

