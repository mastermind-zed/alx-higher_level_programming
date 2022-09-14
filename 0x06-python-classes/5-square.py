#!/usr/bin/python3
""" class Square that defines a square by: (based on 4-square.py) """


class Square:
    """ defining a sqaure """
    def __init__(self, size=0):
        """
        initialization function for our square clasee
        """
        if self.__validate_size(size):
            self.__size = size

    @property
    def size(self):
        """ 
        getter function for private attribute size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for the size property
        """
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """
        area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
            prints the square with character #
        """
        if self.__size == 0:
            print()
        else:
            x, y = 0, 0
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()

    def __validate_size(self, size):
        """
        validates the size, checking for errors
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False
    
