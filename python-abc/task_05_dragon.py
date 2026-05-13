#!/usr/bin/python3
"""Dragon mixins module"""


class SwimMixin:
    """Mixin that provides swimming ability"""

    def swim(self):
        """Swim method"""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying ability"""

    def fly(self):
        """Fly method"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim and fly"""

    def roar(self):
        """Roar method"""
        print("The dragon roars!")
