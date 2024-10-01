#!/usr/bin/python3
"""
This module defines a CustomObject class that can be serialized and deserialized
using the pickle module.
"""

import pickle


class CustomObject:
    """
    A custom class with serialization and deserialization capabilities.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
        name (str): The name of the object
        age (int): The age of the object
        is_student (bool): Whether the object is a student or not
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance and save it to a file.

        Args:
        filename (str): The name of the file to save the serialized object

        Returns:
        None
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load and return an instance of CustomObject from a file.

        Args:
        filename (str): The name of the file to load the serialized object from

        Returns:
        CustomObject: The deserialized object, or None if an error occurred
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
