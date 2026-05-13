#!/usr/bin/python3
"""VerboseList module"""


class VerboseList(list):
    """VerboseList class that extends list with notifications"""

    def append(self, item):
        """Adds item and prints notification"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extends list and prints notification"""
        items = list(items)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Removes item and prints notification"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pops item and prints notification"""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
