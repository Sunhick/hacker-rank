#!/bin/python

__author__ = "Sunil"
__copyright__ = "Copyright 2015, hacker_rank Project"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "sunhick@gmail.com"


if __name__ == '__main__':
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))

    while len(arr) > 0:
        print len(arr)
        cut = min(arr)
        arr = [e-cut for e in arr if e-cut > 0]
