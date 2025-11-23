#!/usr/bin/python3
"""
3-square: Module that defines a Square class.

This module introduces properties (getter and setter) for the private
instance attribute 'size' to ensure type and value validation.
It also includes the public method to compute the area.
"""


class Square:
    """
    Represents a square figure with managed access to its size attribute.
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
