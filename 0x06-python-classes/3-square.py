#!/usr/bin/python3
""" class Square that defines a square by: (based on 2-square.py) """


class Square:
    """ defining a sqaure"""

    def __init__(self, size=0):

        """ initializating square
            Args:
                size (int): size of the square.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return self.__size * self.__size
