#!/usr/bin/python3
"""
defining class with multiple inheritance type
"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object
    is an instance of, or if the object is an instance
    of a class that inherited from, the specified class"""
    if isinstance(obj, a_class):
        return True
    return False
