#!/usr/bin/python3
import time
'''Module for is_same_class method.'''


def is_same_class(obj, a_class):
    '''Determines if an object is exactly an instance of a class.'''
    return type(obj) is a_class
