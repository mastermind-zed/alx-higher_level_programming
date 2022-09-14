#!/usr/bin/python3
""" Python class MagicClass that does exactly the same as the following Python bytecode """

import math


class MagicClass:
    """ circle """

    def __init__(self, radius=0):
        """Disassembly of __init__"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Disassembly of area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Disassembly of circumference"""
        return (2 * math.pi * self.__radius)
