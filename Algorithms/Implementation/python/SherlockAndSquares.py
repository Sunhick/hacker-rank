#!/bin/python

import sys
import math

t = int(raw_input().strip())
for a0 in xrange(t):
    a,b = raw_input().strip().split(' ')
    a,b = [int(a),int(b)]
    counter = 0
    for x in xrange(a,b):
        if ( math.sqrt(x)**2 == x ):
            counter += 1
    print counter
