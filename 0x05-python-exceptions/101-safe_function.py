#!/usr/bin/python3

def safe_function(fct, *args):
    """ function that executes a function safely """

    try:
        r = fct(*args)
        return r
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
