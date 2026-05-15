#!/usr/bin/python3
"""Module that provides a function to convert a Python object to a JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string."""
    return json.dumps(my_obj)
