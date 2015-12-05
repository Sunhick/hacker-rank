#!/usr/bin/py


if __name__ == '__main__':
    testcases = int(input())

    for i in range(testcases):
        number = int(input())
        flipped = ~number & 0xffffffff
        print("%d" % (flipped))
