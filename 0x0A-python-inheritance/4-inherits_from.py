#!/usr/bin/python3
""" Only sub class of """


def inherits_from(obj, a_class):
    """
    checks if an object inherited from a class

    inherits_from returns true if object is instance of a class
        that inherited directly or indirectly from the specified class.
        Args:
            obj (object): object.
            a_class (class): class.
        Returns: True or False.
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be of type 'type'")
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
