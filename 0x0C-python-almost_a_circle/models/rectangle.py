#!/usr/bin/python3
"""
Class Rectangle inherits from Base
Private instance attributes, each with its own public getter and setter:
__width -> width
__height -> height
__x -> x
__y -> y
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Call the super class with id
        The super call with use the logic of the __init__ of the Base class
        Assign each argument width, height, x and y to the right attribute
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            '''width of rectangle'''
            return self.__width

        @width.setter
        def width(self, width):
            '''setter of rectangle'''
            self.__width = width

        @property
        def height(self):
            '''height of rectangle'''
            return self.__height

        @height.setter
        def height(self, height):
            '''setter of rectangle'''
            self.__height = height

        @property
        def x(self):
            '''x of rectangle'''
            return self.__x

        @x.setter
        def x(self, x):
            '''setter of rectangle'''
            self.__x = x

        @property
        def y(self):
            '''y of rectangle'''
            return self.__y

        @width.setter
        def y(self, y):
            '''setter of rectangle'''
            self.__y = y
