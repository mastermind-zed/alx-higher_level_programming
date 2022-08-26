#!/usr/bin/python3

def no_c(my_string):
    """
    removes all instances of 'c' & 'C' from string
    """

    new_string = ""
    for a in range(len(my_string)):
        if my_string[a] != "c" and my_string[a] != "C":
            new_string += my_string[a]
    return (new_string)
