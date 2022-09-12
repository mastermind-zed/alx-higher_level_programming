#!/usr/bin/python3

def safe_print_division(a, b):
    """ function that divides 2 integers and prints the result. """

    res = 0
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {}".format(res))
        return res
