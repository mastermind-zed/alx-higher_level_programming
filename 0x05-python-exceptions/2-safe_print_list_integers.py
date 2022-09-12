#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    
    y = count = 0
    for y in range(x):
        try:
            print("{:d}".format(my_list[y]), end="")
            count += 1
        except(TypeError, ValueError):
            continue
    print()
    return count
