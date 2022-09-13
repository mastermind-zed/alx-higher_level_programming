#!/usr/bin/python3
""" class Square that defines a square by: (based on 2-square.py) """


class Square:
    """" Square: define a sqaure """

    def __init__(self, size=0):
        
        """ initializing of square """
         if (isinstance(size, int)):
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ defining the area of square """
        return (self.__size ** 2)
