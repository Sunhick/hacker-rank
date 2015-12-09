#!/bin/python3

import sys

__author__ = "Sunil"
__copyright__ = "Copyright 2015, hacker_rank Project"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "sunhick@gmail.com"

kALPHABETS = 26


class CaesarCipher:
    """
    Caesar cipher class with key as encryption phrase
    """
    def __init__(self, key):
        self.key = key % kALPHABETS

    def Transform(self, char):
        """
        Transform character to cipher character
        """
        start = ord('a')
        end = ord('z')
        if char.isupper():
            start = ord('A')
            end = ord('Z')

        tchar = ord(char) + self.key
        if tchar > end:
            return chr(start + tchar - end - 1)

        return chr(tchar)
        # return chr(start + (ord(char) + self.key) % kALPHABETS)

    def Encrypt(self, plaintext):
        """
        Encode the plain text using key
        """
        cipher = ''
        for c in plaintext:
            if c.isalpha():
                cipher = cipher + self.Transform(c)
            else:
                cipher = cipher + c

        return cipher


if __name__ == '__main__':
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())

    cc = CaesarCipher(k)
    print(cc.Encrypt(s))
