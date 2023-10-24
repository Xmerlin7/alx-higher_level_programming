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
        self.__size = size

    @property
    def size(self):
        """property for the length of the square.
        Raises:
            TypeError: if size not int
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """ define a public instance method.


        Returns:
            size of the square
        """
        return self.__size ** 2
