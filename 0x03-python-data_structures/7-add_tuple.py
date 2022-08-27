#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """ function that add tuples """
    
    ta_len = len(tuple_a)
    tb_len = len(tuple_b)
    new_tup = ()
    for x in range(2):
        if x >= ta_len:
            val_a = 0
        else:
            val_a = tuple_a[x]
        
        if x >= tb_len:
            val_b = 0
        else:
            val_b = tuple_b[x]

        if (x == 0):
            new_tup = (val_a + val_b)
        else:
            new_tup = (new_tup, val_a + val_b)
    return (new_tup)
