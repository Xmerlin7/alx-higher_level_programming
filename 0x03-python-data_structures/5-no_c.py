#!/usr/bin/python3
def no_c(my_string):
    x = [i for i in my_string if i !='c' or i != 'C']
    return ("".join(x))
