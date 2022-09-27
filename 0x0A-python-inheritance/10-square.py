#!/usr/bin/python3


Rectangle = __import__('9-rectangle').Rectangl


class Square(Rectangle):
    """ a class Square that inherits from Rectangle (9-rectangle.py) """
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
