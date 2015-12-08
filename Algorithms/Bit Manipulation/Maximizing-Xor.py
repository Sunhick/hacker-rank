#!/usr/bin/python3


def maxXor(l, r):
    """
    Max Xor
    """
    i = l
    max_so_far = 0

    while(l <= i and i <= r):
        j = l
        while(l <= j and j <= r):
            tmp = i ^ j
            if max_so_far < tmp:
                max_so_far = tmp

            j += 1

        i += 1

    return max_so_far

if __name__ == '__main__':
    l = int(input())
    r = int(input())
    print(maxXor(l, r))
