#!/usr/bin/python3
"""FlyingFish module - Multiple Inheritance"""


class Fish:
    """Fish class"""

    def swim(self):
        """Fish swimming method"""
        print("The fish is swimming")

    def habitat(self):
        """Fish habitat method"""
        print("The fish lives in water")


class Bird:
    """Bird class"""

    def fly(self):
        """Bird flying method"""
        print("The bird is flying")

    def habitat(self):
        """Bird habitat method"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class that inherits from Fish and Bird"""

    def fly(self):
        """FlyingFish flying method"""
        print("The flying fish is soaring!")

    def swim(self):
        """FlyingFish swimming method"""
        print("The flying fish is swimming!")

    def habitat(self):
        """FlyingFish habitat method"""
        print("The flying fish lives both in water and the sky!")
