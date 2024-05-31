#!/usr/bin/env python3
from models.base import Base
def addNumbers(*args):
    for arg in args:
        print(arg, end= " ")
addNumbers(1, "seif", [5, 6, "ahmed"])