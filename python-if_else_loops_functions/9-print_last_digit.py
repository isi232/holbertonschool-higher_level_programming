#!/usr/bin/python3
def print_last_digit(r):
    last = abs(r) % 10
    print(last, end="")
    return last
