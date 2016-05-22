#!/bin/python3

import sys
import math

__author__ = "Sunil"
__copyright__ = "Copyright 2016, hacker_rank Project"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "sunhick@gmail.com"

class Palindrome:
	def __init__(self):
		pass

	def count_changes(self, letter):
		count = 0
		for i in range(int(len(letter)/2)):
			count = count + abs(ord(letter[i]) - ord(letter[-i-1]))
		return count

n = int(input().split()[0])

pl = Palindrome()

for i in range(n):
	l = input()
	c = pl.count_changes(l)
	print(c)
