#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    seen = []
    for num in my_list:
        if num not in seen:
            total += num
            seen.append(num)
    return total
