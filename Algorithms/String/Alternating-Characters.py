#!/bin/python3

import sys

__author__ = "Sunil"
__copyright__ = "Copyright 2016, hacker_rank Project"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "sunhick@gmail.com"

n = int(input().split(' ')[0])

for i in range(n):
    s = input()
    c = 0
    pr = ''
    for l in range(len(s)):
    	if pr == s[l]:
    		c = c+1
    	pr = s[l]
    print(c)