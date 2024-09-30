#!/usr/bin/python3
"""Module for reading a file and printing its contents."""


def read_file(filename=""):
    """Read a text file and print its contents to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
