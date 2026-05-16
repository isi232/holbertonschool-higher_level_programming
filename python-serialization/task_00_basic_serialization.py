#!/usr/bin/python3
"""Basic serialization module.

Converts Python dictionaries to JSON files and back.
"""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file.

    Args:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file.
                  If the file already exists, it will be replaced.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file.

    Args:
        filename: The filename of the input JSON file

    Returns:
        A Python Dictionary with the deserialized JSON data from the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
