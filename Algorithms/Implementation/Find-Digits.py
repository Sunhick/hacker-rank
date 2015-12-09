#!/bin/python3

"""Find-Digits.py: determine how many digits evenly divide N"""

__author__ = "Sunil"
__copyright__ = "Copyright 2015, hacker_rank Project"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "sunhick@gmail.com"


if __name__ == '__main__':
    testcases = int(input().strip())

    for testcase in range(testcases):
        number = int(input().strip())

        print(len([i for i in map(int, list(str(number)))
                   if i != 0 and number % i == 0]))
        """
        tmp = number
        count = 0

        while tmp > 0:
            remainder = tmp % 10
            if remainder != 0 and number % remainder == 0:
                count += 1

            tmp = int(tmp / 10)

        print(count)
        """
