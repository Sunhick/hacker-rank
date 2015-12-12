#!/bin/python

import sys
import math

t = int(raw_input().strip())
for a0 in xrange(t):
    a,b = raw_input().strip().split(' ')
    a,b = [int(a),int(b)]
    minValue = int(math.ceil(a**0.5))
    maxValue = int(math.floor(b**0.5))
    print maxValue - minValue + 1
