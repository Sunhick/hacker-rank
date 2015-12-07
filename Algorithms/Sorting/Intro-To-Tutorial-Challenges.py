#!/usr/bin/py


def indexof(array, v):
    index = -1
    for e in array:
        index += 1
        if e == v:
            return index


if __name__ == '__main__':
    v = int(input())
    size = int(input())
    array = [input().split(" ")]
    array = [int(item) for sublist in array for item in sublist]
    print(indexof(array, v))
