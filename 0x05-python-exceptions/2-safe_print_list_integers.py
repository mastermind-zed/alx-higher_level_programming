#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """ function that prints the first x elements of a list and only integers. """

    count, index = 0, 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end="")
        except (TypeError, ValueError):
            pass
        else:
            count += 1
        finally:
            index += 1
    print()
    return count
