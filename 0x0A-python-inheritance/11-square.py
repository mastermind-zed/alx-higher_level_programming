#!/usr/bin/python3


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py) """
    def __init__(self, size):
        """ define square """

    def area(self):
        """ area of a square """ 
        area = self.__size * self.__size
        return area

    def __str__(self):
        return ("[{}] {}/{}".format("Rectangle", self.__size, self.__size))
