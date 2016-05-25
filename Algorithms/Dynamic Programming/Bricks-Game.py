#!/bin/python3

import sys

__author__ = "Sunil"
__copyright__ = "Copyright 2016, hacker_rank Project"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "sunhick@gmail.com"

def get_max_score(bricks):
	dp = [0] * len(bricks)
	dp[0] = bricks[0]
	dp[1] = bricks[1] + dp[0]
	dp[2] = bricks[2] + dp[1]

	csum = dp[:]
	for i in range(3, len(bricks)):
		one_elem = bricks[i] + (csum[i-1] - dp[i-1])
		two_elem = bricks[i] + bricks[i-1] + \
					(csum[i-2] - dp[i-2])
		three_elem = bricks[i] + bricks[i-1] + \
				bricks[i-2] + (csum[i-3] - dp[i-3])
		dp[i] = max(one_elem, two_elem, three_elem)
		csum[i] = csum[i-1] + bricks[i]

	return dp[-1]

if __name__ == "__main__":
	tc = int(input())
	for i in range(tc):
		size = int(input())
		bricks = list(map(int, input().split()))
		print(get_max_score(bricks[::-1]))