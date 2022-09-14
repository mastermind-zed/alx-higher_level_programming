#!/usr/bin/python3
""" class Square that defines a square by: (based on 4-square.py) """


class Square:
    """Represents an empty square"""
    def __init__(self, size=0):
        """
        Init class with args: size
        runs a check to ensure size data is correct type and value.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method function to return the 'area' of the Square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Method to return the value stored in the private variable 'size'"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method which sets a new value to the 'size' instace/attribute"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Method that draws a square with '#' to the Stdout"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for x in range(self.__size):
                print("#", end="")
            print()
