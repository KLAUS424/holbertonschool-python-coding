#!/usr/bin/python3
"""
0-square: Module that defines a Square class.

This module provides the Square class, which represents a geometric square
defined by a private instance attribute 'size'. This privacy is enforced
to control the type and value of the attribute, which is crucial for
calculations like area computation.
"""


class Square:
    """
    Represents a square figure.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size (side length) of the square.
                        It is stored as a private attribute '__size'.
        """
        # The '__size' attribute is private (via name mangling).
        # This mechanism allows the class builder to control access
        # and value validation in future implementations.
        self.__size = size
