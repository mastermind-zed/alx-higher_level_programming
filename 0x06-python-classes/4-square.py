#!/usr/bin/python3
""" class Square that defines a square by: (based on 3-square.py) """


class Sqaure:
    """ defining a sqaure """

    def __init__(self, size=0):
        """ initializing square
            Args:
            size: Length of a side of the square.
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ lenght of sides of the square """
        return self.__size

    @size.setter
     def size(self, value):
         """ funtion for private attribute size """
         if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """ area of sqaure """
            return self.__size * self.__size
