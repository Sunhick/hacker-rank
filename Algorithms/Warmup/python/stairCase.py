#!/bin/python

import sys


n = int(raw_input().strip())
for x in xrange(n):
    print' '*(n-1-x)+'#'*(x+1)
