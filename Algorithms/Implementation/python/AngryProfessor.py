#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    #print a
    #print [x >= 0 for x in a]
    if([x <= 0 for x in a].count(True) >= k):
        print "NO"
    else:
        print "YES"
