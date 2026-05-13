#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    return type(obj) is not a_class and isinstance(obj, a_class)
