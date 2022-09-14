#!/usr/bin/python3
""" class Square that defines a square by: (based on 5-square.py) """


class Square:
    """ defining sqaure """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """ Define Square area """

    def area(self):
        res = self.__size * self.__size
        return res

    """ Getter size """
    @property
    def size(self):
        return self.__size

    """ Setter size """
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ Prints Square """

    def my_print(self):
        if self.__size > 0:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")

    """ Getter Position """
    @property
    def position(self):
        return self.__position

    """ Setter position """
    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
