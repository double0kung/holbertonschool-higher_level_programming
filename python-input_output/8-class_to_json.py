#!/usr/bin/python3
"""Module for class_to_json function"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object"""
    return obj.__dict__
