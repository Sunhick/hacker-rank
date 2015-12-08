#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp[a_i])
   a.append(a_temp[n-a_i-1])

sumP = 0
sumS = 0


for i in xrange(len(a)):
    if(i%2) == 0:
        sumP += a[i]
    else:
        sumS += a[i]

print abs(sumP-sumS)
