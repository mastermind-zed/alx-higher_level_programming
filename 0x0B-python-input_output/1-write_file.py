#!/usr/bin/python3
""" Write to a file """


def write_file(filename="", text=""):
    """ writs a string to a text file (UTF8) """
    with open(filename, mode="w", encoding="UTF8") as myFile:
        return(myFile.write(text))
