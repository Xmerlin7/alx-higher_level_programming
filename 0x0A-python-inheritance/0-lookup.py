#!/usr/bin/python3
``` module for lookup method ```
def lookup(obj):
    ``` looks up pbject Attribute 
    Args:
        obj (object): the object of the list
    Returns:
        list: the list of the attripute
    ```
    return dir(obj)
