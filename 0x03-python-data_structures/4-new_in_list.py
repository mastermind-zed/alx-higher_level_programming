#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace an element at specific index without modifying the whole list"""
    l_len = len(my_list)
    if idx >= l_len or idx < 0:
        return (my_list)

    new_list = my_list[:]
    new_list[idx] = element
    return (new_list)
