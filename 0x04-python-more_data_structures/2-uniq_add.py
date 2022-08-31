#!/usr/bin/python3

def uniq_add(my_list=[]):
    """ function that replaces all occurrences of an element by another in a new list """
    return (sum({ele for ele in my_list}))
