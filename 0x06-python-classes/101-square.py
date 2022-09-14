#!/usr/bin/python3
""" Square that defines a square by: (based on 6-square.py) """



class Square:
    """ defining square """
    def __init__(self, size=0, position=(0, 0)):
        """ Instantiate a 'Square'
        """
        self.size, self.position = size, position

    def __str__(self):
        """ Create a visual representation of a square
        """
        if self.size:
            return '\n' * self.position[1] + '\n'.join(
                [' ' * self.position[0] + '#' * self.size] * self.size
            )
        return str()

    @property
    def size(self):
        """ Get the size of a square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """ Set the size of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """ Get the position of a square
        """
        return self.__position

    @position.setter
    def position(self, position):
        """ Set the position of a square
        """
        if not (isinstance(position, tuple) and
                len(position) == 2 and
                isinstance(position[0], int) and
                isinstance(position[1], int) and
                position[0] >= 0 and
                position[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ Compute the area of a 'Square'
        """
        return self.size ** 2

    def my_print(self):
        """ Print a visual representation of a square
        """
        print(self)
