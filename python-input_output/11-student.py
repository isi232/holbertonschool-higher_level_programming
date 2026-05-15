#!/usr/bin/python3
"""Module that defines a Student class with JSON serialization support."""


class Student:
    """Represent a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first_name, last_name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance."""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary."""
        for k, v in json.items():
            setattr(self, k, v)
