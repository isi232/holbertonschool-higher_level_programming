#!/usr/bin/python3
"""Pickling custom Python objects using the pickle module."""

import pickle


class CustomObject:
    """A custom class with serialization and deserialization support."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance and save it to a file.

        Args:
            filename (str): The filename to save the serialized object to.

        Returns:
            None if an exception occurs.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError) as e:
            print(f"Serialization error: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance of CustomObject from a file.

        Args:
            filename (str): The filename to load the serialized object from.

        Returns:
            CustomObject instance, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (OSError, pickle.UnpicklingError, EOFError) as e:
            print(f"Deserialization error: {e}")
            return None
