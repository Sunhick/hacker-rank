#!/bin/python3

import sys
from collections import Counter

__author__ = "Sunil"
__copyright__ = "Copyright 2016, hacker_rank Project"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "sunhick@gmail.com"

def count_gems(a, b):
	ce = ''
	for c in a:
		if c in b:
			ce = ce + c
	return ce

n = int(input().split()[0])
rocks = [input() for i in range(n)]
counters = [Counter(rock) for rock in rocks]
gems = counters[0]

for ctr in counters:
	gems = gems & ctr

print(sum(gems.values()))