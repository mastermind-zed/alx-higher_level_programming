#!/usr/bin/python3
""" add attribute """


def add_attribute(cls, name, value):
    """ function that adds a new attribute to an object if it’s possible """
    if hasattr(cls, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(cls, name, value)
