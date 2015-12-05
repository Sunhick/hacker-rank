#!/usr/bin/py


def lonelyinteger(b):
    answer = 0
    for e in b:
        answer ^= e

    return answer

if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))
