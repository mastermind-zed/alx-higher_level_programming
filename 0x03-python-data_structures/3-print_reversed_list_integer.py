#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """ function that prints all integers of a list, in reverse order"""

    if my_list:
        my_list.reverse()
        for number in my_list:
            print("{:d}".format(number))
