#!/usr/bin/python3
"""
1-square: Module that defines a Square class with size validation.

This module provides the Square class, which is defined by a private
instance attribute 'size'. The constructor now handles optional instantiation
and enforces strict type and value constraints for the size attribute.
"""


class Square:
    """
    Represents a square figure.

    The square's size is strictly validated upon instantiation.
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

        # Store the validated size as a private attribute.
        self.__size = size
