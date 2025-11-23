#!/usr/bin/python3
"""
4-square: Module that defines a Square class.

This module provides the Square class with size validation via properties,
a method to calculate area, and a method to print the square graphically.
"""


class Square:
    """
    Represents a square figure with managed access to its size attribute
    and methods for area calculation and graphical printing.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        The initializer uses the setter to validate the initial size value.

        Args:
            size (int, optional): The size (side length) of the square.
                                  Defaults to 0.
        """
        self.size = size  # Calls the setter property

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            int: The size (side length) of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square with validation.

        Args:
            value (int): The new size (side length) for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Computes and returns the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square to stdout using the character '#'.

        The square is printed as a grid of size x size characters.
        If the size is 0, it prints a single empty line.
        """
        if self.__size == 0:
            # Print an empty line if the size is zero
            print()
        else:
            # Loop for each row
            for _ in range(self.__size):
                # Print the row by repeating '#' 'size' times
                print("#" * self.__size)
