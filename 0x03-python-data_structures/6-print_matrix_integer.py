#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Function that prints a matrix of integers"""

    for a in range(len(matrix)):
        subm_len = len(matrix[i])
        for b in range(subm_len):
            if b != subm_len - 1:
                endCh = ' '
            else:
                endCh = ''
            print("{:d}".format(matrix[a][b]), end=endCh)
        print("")
