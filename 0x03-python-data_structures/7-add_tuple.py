#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuble_a) < 2:
        if len(tuble_a) == 0:
            tuble_a = (0, 0)
        else:
            tuble_a[1] = 0
    if len(tuble_b) < 2:
        if len(tuble_b) == 0:
            tuble_b = (0, 0)
        else:
            tuble_b[1] = 0
    return (tuple_a[0] + tuble_b[0], tuple_a[1] + tuble_b[1])
