#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """ function that returns a new dictionary with all values multiplied by 2 """

    z_dictionary = {}
    for i in a_dictionary:
        z_dictionary[i] = a_dictionary[i] * 2
    return (z_dictionary)
