#!/usr/bin/python3
"""Module containing the MyList class"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted in ascending order"""
        print(sorted(self))
