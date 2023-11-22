#!/usr/bin/python3
class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): The position of the square (private).
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with optional size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position square. Defaults to (0,0)

        Raises:
            TypeError: If size is not an integer or if position is not a
            tuple of 2 positive integers.
            ValueError: If size is less than 0 or if position
            values are less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method to retrieve the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size attribute.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter method to retrieve the position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position attribute.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If position values are less than 0.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(v, int) for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise ValueError("position values must be >= 0")
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' character based on size and position.

        Prints:
            The square represented by '#' characters.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
