#!/usr/bin/python3
"""
This module provides functionality to serialize and deserialize
Python dictionaries to and from XML format.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save it to a file.

    Args:
    dictionary (dict): The dictionary to serialize
    filename (str): The name of the file to save the XML

    Returns:
    None
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file to a Python dictionary.

    Args:
    filename (str): The name of the file to read the XML from

    Returns:
    dict: The deserialized dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
