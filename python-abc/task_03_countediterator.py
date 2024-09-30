#!/usr/bin/env python3
"""Module for CountedIterator class"""

class CountedIterator:
    """A class that wraps an iterator and keeps track of the number of iterations"""

    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable"""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return self as an iterator"""
        return self

    def __next__(self):
        """Get the next item and increment the counter"""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """Return the current count of iterated items"""
        return self.count
