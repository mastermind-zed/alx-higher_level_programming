#!/usr/bin/python3

def max_integer(my_list=[]):
    """ function that finds all multiples of 2 in a list """

    new_list = []
    for number in my_list:
        if (number % 2) == 0:
            new_list.append(True)

        else:
            new_list.append(False)
    
    return(new_list)
