#!/usr/bin/python3

def safe_print_integer_err(value):
    """ function that prints an integer. """

    import sys
    try:
        print("{:d}".format(value))
    except Exception as ve:
        print("Exception:", ve, file=sys.stderr)
        return False
    return True
