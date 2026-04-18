#!/usr/bin/python3
for i in range(26):
    c = 122 - i
    if i % 2 == 0:
        print("{}".format(chr(c)), end="")
    else:
        print("{}".format(chr(c - 32)), end="")
