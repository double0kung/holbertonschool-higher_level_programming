#!/usr/bin/python3
"""
This module provides basic serialization functionality to serialize
a Python dictionary to a JSON file and deserialize the JSON file
to recreate the Python Dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize and save data to the specified file.

    Args:
    data (dict): A Python Dictionary with data
    filename (str): The filename of the output JSON file

    Returns:
    None
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize data from the specified file.

    Args:
    filename (str): The filename of the input JSON file

    Returns:
    dict: A Python Dictionary with the deserialized JSON data from the file
    """
    with open(filename, 'r') as f:
        return json.load(f)
