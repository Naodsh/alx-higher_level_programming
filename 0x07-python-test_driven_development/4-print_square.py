#!/usr/bin/python3
"""Module Prints a square with the character '#'."""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
    - size (int): The size length of the square.

    Raises:
    - TypeError: If size is not an integer or if size is a float less than 0.
    - ValueError: If size is less than 0.

    Test:
    >>> print_square(4)
    ####
    ####
    ####
    ####
    >>> print_square(10)
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    >>> print_square(0)
    >>> print_square(1)
    #
    >>> print_square(-1)
    Traceback (most recent call last):
        ...
    ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    for _ in range(size):
        print("#" * size)
