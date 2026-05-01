#!/usr/bin/python3
import sys

if __name__ == "__main__":
    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    i = 1
    while i <= count:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
