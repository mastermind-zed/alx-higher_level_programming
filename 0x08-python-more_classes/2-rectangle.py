#!/usr/bin/python3
""" 
Area and Perimeter 
"""


class Rectangle:
    """
    class Rectangle that defines a rectangle by: (based on 1-rectangle.py 
    """

    def __init__(self, width=0, height=0):
        '''Constructor.
        Args:
            width: The width of rectangle.
            height: The height of rectangle.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Property for the width of the rectangle.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Property for the height of the rectangle.
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns area of this rectangle.'''
        return self.width * self.height

    def perimeter(self):
        '''Returns perimeter of this rectangle.'''
        if not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2
