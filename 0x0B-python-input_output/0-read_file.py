#!/usr/bin/python3
"""Module containing the function read_file"""


def read_file(filename=""):
    """Reads a file and prints to stdout.

    Args:
        filename (str, optional): name of file to read. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as fi:
        read_data = fi.read()
        print(read_data, end='')
