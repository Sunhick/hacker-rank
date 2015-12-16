#!/bin/python3

import math

__author__ = "Sunil"
__copyright__ = "Copyright 2015, hacker_rank Project"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "sunhick@gmail.com"


def count_squares(start, end):
    return int(math.floor(math.sqrt(end)) - math.ceil(math.sqrt(start)) + 1)

if __name__ == '__main__':
    testcases = int(input().strip())

    for i in range(0, testcases):
        start, end = input().strip().split(' ')
        print(count_squares(int(start), int(end)))
