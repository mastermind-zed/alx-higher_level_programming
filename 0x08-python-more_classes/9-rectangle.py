#!/usr/bin/python3
"""
A square is a rectangle
"""


class Rectangle:
    """
    class Rectangle that defines a rectangle by: (based on 8-rectangle.py
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Constructor method """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @classmethod
    def square(cls, size=0):
        """ Create new Rectangle instance with width == height == size """
        return cls(size, size)

    @property
    def width(self):
        """ getter width property """
        return self.__width

    @property
    def height(self):
        """ getter height property """
        return self.__height

    @width.setter
    def width(self, value):
        """ setter width property """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter height property """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Return area of rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Return perimeter of rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """ Return string to print rectangle with # """
        if self.width == 0 or self.height == 0:
            return ''
        to_print = ''
        for col in range(self.height):
            for row in range(self.width):
                to_print += str(self.print_symbol)
            if col != self.height - 1:
                to_print += '\n'
        return to_print

    def __repr__(self):
        """ Return a string representation of the rectangle """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """ Deconstructor method """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
