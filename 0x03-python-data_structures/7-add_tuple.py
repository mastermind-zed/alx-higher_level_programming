#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """ function that adds 2 tuples """

    ta_len = len(tuple_a)
    tb_len = len(tuple_b)
    new_tup = ()
    for x in range(2):
        if x >= ta_len:
            val_n = 0
        else:
            val_n = tuple_a[x]
           
           if x >= tb_len:
            val_m = 0
        else:
            val_m = tuple_b[x]

        if (x == 0):
            new_tup = (val_n + val_m)
        else:
            new_tup = (new_tup, val_n + val_m)

    return (new_tup)
