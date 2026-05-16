#!/usr/bin/python3
"""Module for serializing and deserializing Python dictionaries using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The Python dictionary to serialize.
        filename (str): The filename to save the XML data to.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="    ")
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """Deserialize an XML file back into a Python dictionary.

    Args:
        filename (str): The filename of the XML file to read.

    Returns:
        dict: The deserialized Python dictionary, or None if an error occurs.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        return {child.tag: child.text for child in root}

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return None
