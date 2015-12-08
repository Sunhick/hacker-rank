#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

pos = 0
neg = 0
zero = 0
for x in xrange(len(arr)):
    if ( arr[x] > 0 ):
        pos += 1
    elif ( arr[x] == 0 ):
        zero += 1
    else:
        neg += 1

#print pos,neg,zero
print pos/float(len(arr))
print neg/float(len(arr))
print zero/float(len(arr))
        

