#!/usr/bin/python3
""" Print square """


def print_square(size):
    """ function that prints a square with the character #. """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    elif size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    size = int(size)  # if it was a float convert it
    i = 0

    for i in range(0, size):
        j = 0
        for j in range(0, size):
            print('#', end='')
        print()
