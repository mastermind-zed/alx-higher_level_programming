#!/usr/bin/python3
""" Square #2 """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py) """
    def __init__(self, size):
        """ init method of class """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self)
    """ str method for class """
    string = "[Square] " + str(self.__size) + '/'
        string += str(self.__size)
        return string
