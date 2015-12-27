#!/bin/python

import sys


n,t = raw_input().strip().split(' ')
n,t = [int(n),int(t)]
width = map(int,raw_input().strip().split(' '))
#print width , type(width)
for a0 in xrange(t):
    i,j = raw_input().strip().split(' ')
    i,j = [int(i),int(j)]
    maxValue = 3
    for k in xrange(i,j+1):
        maxValue = min(width[k],maxValue) 
    print maxValue
