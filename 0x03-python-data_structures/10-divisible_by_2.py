#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """ function that finds all multiples of 2 in a list """

    mod_2 = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            mod_2.append(True)
        else:
            mod_2.append(False)
    return (mod_2)
