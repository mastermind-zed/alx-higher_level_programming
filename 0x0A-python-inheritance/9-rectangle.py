#!/usr/bin/python3
""" defining rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)"""
    def __init__(self, width, height):
        """ full rectangle """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """ area of rectangle """
        area = self.__width * self.__height
        return area

    def __str__(self):
        """ string of rectangle """
        string = "[Rectangle] "
        string += str(self.__width) + '/' + str(self.__height)
        return string
