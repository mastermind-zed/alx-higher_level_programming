#!/usr/bin/python3

def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return (0)
    mul = list(map(lambda x: x[0] * x[1], my_list))
    add = list(map(lambda x: x[1], my_list))
    return sum(mul) / sum(add)
