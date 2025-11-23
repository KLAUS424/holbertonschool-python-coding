#!/usr/bin/python3
"""
2-square: Module that defines a Square class.

This module provides the Square class, which includes size validation
and a public method to compute the area of the square.
"""


class Square:
    """
    Represents a square figure.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size (side length) of the square.
                                  Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Computes and returns the current area of the square.
