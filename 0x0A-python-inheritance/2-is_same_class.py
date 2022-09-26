#!/usr/bin/python3
"""
Exact same object
"""


def is_same_class(obj, a_class):
    """
    is_same_class returns True if object is an instance of specified class.
        Args:
            obj (object): object being checked.
            a_class (class): class.
        Return: True or False.
    """
    return type(obj) == a_class
