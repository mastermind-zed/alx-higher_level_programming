#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """ function that prints the first x elements of a list and only integers. """

    try:
        count = 0
        for a in range(x):
            if isinstance(my_list[a], int):
                count += 1
                print("{:d}".format(my_list[a]), end="")
    except TypeError as err:
        print(err)
    else:
        print("")
        return count
