#!/usr/bin/python3
""" 
Same class or inherit from
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class returns true if the object is instance of class.
        Args:
            obj (object): object.
            a_class (class): class.
        Return: True or false.
    """
    return isinstance(obj, a_class)
