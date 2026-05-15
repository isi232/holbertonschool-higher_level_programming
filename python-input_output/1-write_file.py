#!/usr/bin/python3
"""This module writes a string to a text file."""


def write_file(filename="", text=""):
    """Writes to a UTF-8 file and returns the number of characters."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
