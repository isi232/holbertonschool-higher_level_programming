#!/usr/bin/python3
"""Module for converting CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON format and write it to data.json.

    Args:
        csv_filename (str): The filename of the input CSV file.

    Returns:
        True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except (csv.Error, json.JSONEncodeError, OSError) as e:
        print(f"Error during conversion: {e}")
        return False
