#!/bin/python

"""Extra long factorials"""

__author__ = "Sunil"
__copyright__ = "Copyright 2015, hacker_rank Project"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "sunhick@gmail.com"


if __name__ == '__main__':
    n = int(raw_input().strip())
    fact = 1

    while n > 0:
        fact *= n
        n = n-1

    print fact
