#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    b,w = raw_input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]

    if ( x == y ):
        print b*x + w*y
    elif ( x > y+z ):
        print b*(y+z) + w*y
    elif ( y > x+z ):
        print b*x + w*(x+z)
    else:
        print b*x + w*y
