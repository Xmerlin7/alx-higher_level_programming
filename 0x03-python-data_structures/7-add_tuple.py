#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_b[1]
    else: 
        a = tuple_a[0] + tuple_b[0]
        b = tuble_a[1]
    if len(tuple_a) > 2 or len(tuple_b) > 2:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_b[1] + tuple_b[1]

    return (a, b)
