#!/usr/bin/python3
""" Write to a file """


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8) and returns the number of characters written """
    with open(filename, "w", encoding='utf-8') as x_file:
        return x_file.write(text)
