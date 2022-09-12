#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """ function that prints the first x elements of a list and only integers. """

    a = count = 0
    for a in range(x):
        try:
            print("{:d}".format(my_list[a]), end="")
            count += 1
        except(TypeError, ValueError):
            continue
    print()
    return count
