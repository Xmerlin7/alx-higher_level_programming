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
        self.__size = value

    def area(self):
        """ define a public instance method.


        Returns:
            size of the square
        """
        return self.__size ** 2

    def my_print(self):
        """ prints the stdout of the square"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is (self.size - 1) and i != j else "")
        print()
