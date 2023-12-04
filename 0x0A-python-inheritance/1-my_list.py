#!/usr/bin/python3
"""Inherits from list and adds a print_sorted method."""


class MyList(list):
    """Inherits from list and adds a print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
