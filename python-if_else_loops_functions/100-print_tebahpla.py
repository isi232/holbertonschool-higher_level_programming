#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{}{}".format(chr(122 - (25 - i)), chr(89 - (25 - i))), end="")
