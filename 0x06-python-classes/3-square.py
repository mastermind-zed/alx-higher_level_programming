#!/usr/bin/python3
""" class Square that defines a square by: (based on 2-square.py) """


class Square:
    """" Square: define a sqaure """
    def __init__(self, size=0):
        
        """ initializing of square """
         if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ defining the area of square """
        return (self.__size ** 2)
