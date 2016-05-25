#!/bin/python3

import sys

__author__ = "Sunil"
__copyright__ = "Copyright 2016, hacker_rank Project"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "sunhick@gmail.com"


def isfunny(S):
	R = S[::-1]
	for i in range(1, len(S)):
		if abs(ord(S[i])-ord(S[i-1])) != abs(ord(R[i])-ord(R[i-1])):
			return "Not Funny"
	return "Funny"

if __name__ == "__main__":
	N = int(input().split(' ')[0])

	for i in range(N):
		S = input()
		res = isfunny(S)
		print(res)

