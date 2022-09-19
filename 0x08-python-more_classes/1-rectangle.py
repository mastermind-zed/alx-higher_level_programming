#!/usr/bin/python3
""" Real definition of a rectangle """


class Rectangle:
    """ a class Rectangle that defines a rectangle by: (based on 0-rectangle.py """
    def __init__(self, width=0, height=0):
        """ defining a rectangle """
         if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = width
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = height
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """setter of private instance width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of private instance width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """setter of private instance height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of private instance height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
