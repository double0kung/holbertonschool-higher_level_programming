#!/usr/bin/python3
"""
This module provides a function for adding two integers.

The main function in this module is add_integer, which takes two numbers
(integers or floats) and returns their sum as an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
        ValueError: If a or b is NaN (Not a Number).
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for NaN
    # NaN is the only value that isn't equal to itself
    if isinstance(a, float) and a != a:
        raise ValueError("cannot convert float NaN to integer")
    if isinstance(b, float) and b != b:
        raise ValueError("cannot convert float NaN to integer")

    return int(a) + int(b)
