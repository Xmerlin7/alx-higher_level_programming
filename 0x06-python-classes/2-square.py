#!/usr/bin/python3
""" square module."""


class Square:
    """Define a square."""
    def __init__(self, size=0):
        """constr

        Args:
            size: length of a side of the square.

        Raises:
            TypeError: if size not int
            ValueError: if size < 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
