#!/usr/bin/python3
"""Module to print a formatted name."""


def say_my_name(first_name, last_name=""):
    """
    Prints the name in a formatted string.

    Args:
    - first_name (str): The first name.
    - last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
    - TypeError: If either first_name or last_name is not a string.

    Example:
    >>> say_my_name("John", "Doe")
    My name is John Doe
    >>> say_my_name("Alice")
    My name is Alice
    >>> say_my_name(123)
    Traceback (most recent call last):
        ...
    TypeError: first_name must be a string
    >>> say_my_name("Bob", 456)
    Traceback (most recent call last):
        ...
    TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
