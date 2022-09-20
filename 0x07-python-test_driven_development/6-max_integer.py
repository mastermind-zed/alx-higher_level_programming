#!/usr/bin/python3
""" Max integer - Unittest """ 


def max_integer(list=[]):
    """  function def max_integer(list=[]): """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
