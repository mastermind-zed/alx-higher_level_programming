#!/usr/bin/python3
"""my int"""


def add_attribute(clss, atrb, val):
    """ class MyInt that inherits from int """
    if "__dict__" in dir(clss):
        setattr(clss, atrb, val)
    else:
        raise TypeError("can't add new attribute")
