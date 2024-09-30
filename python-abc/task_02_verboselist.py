#!/usr/bin/env python3
"""Module for VerboseList class"""

class VerboseList(list):
    """A list class that prints notifications for certain operations"""

    def append(self, item):
        """Append an item to the list and print a notification"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list and print a notification"""
        original_length = len(self)
        super().extend(iterable)
        items_added = len(self) - original_length
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        """Remove an item from the list and print a notification"""
        if item in self:
            super().remove(item)
            print(f"Removed [{item}] from the list.")
        else:
            print(f"[{item}] not found in the list.")

    def pop(self, index=-1):
        """Pop an item from the list and print a notification"""
        if len(self) > 0:
            item = super().pop(index)
            print(f"Popped [{item}] from the list.")
            return item
        else:
            print("Cannot pop from an empty list.")
            raise IndexError("pop from empty list")
