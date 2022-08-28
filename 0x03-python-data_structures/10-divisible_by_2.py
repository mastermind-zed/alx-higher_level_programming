#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """ function that finds all multiples of 2 in a list """

    if len(my_list) == 0:
        return (None)
    my_list.sort()
    return (my_list[-1])
