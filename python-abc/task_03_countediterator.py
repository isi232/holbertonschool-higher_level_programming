#!/usr/bin/python3
"""CountedIterator module"""


class CountedIterator:
    """Iterator that counts how many items have been fetched"""

    def __init__(self, iterable):
        """Initialize with an iterable"""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Returns the iterator itself"""
        return self

    def __next__(self):
        """Returns next item and increments counter"""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Returns the number of items fetched"""
        return self.count
