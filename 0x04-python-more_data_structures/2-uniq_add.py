#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    for value in set(my_list):
        res += value
    return (res)
