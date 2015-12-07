#!/usr/bin/py
import sys

kALPHABETS_COUNT = 26


def ispangram(line):
    """
    is pangram
    return: True if line contains all alphabets, false otherwise
    """
    # remove all special characters and keep only alphabets
    line = ''.join(e for e in line if e.isalpha())
    alphabets = set()
    for c in line:
        alphabets.add(c)

    # print(alphabets)
    # print('set count = %d, chars in line = %d' % (len(alphabets), len(line)))
    return len(alphabets) == kALPHABETS_COUNT


if __name__ == '__main__':
    line = sys.stdin.readline()
    if ispangram(line.lower()):
        print('pangram')
    else:
        print('not pangram')
