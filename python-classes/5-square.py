#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initialize square"""
        self.size = size

    @property
    def size(self):
        """Retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation"""

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return square area"""
        return self.__size * self.__size

    def my_print(self):
        """Print square using #"""

        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
