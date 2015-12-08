#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    output=1
    for x in xrange(n):
        if ( x%2 == 1):
            output+=1
        else:
            output*=2
    print output
