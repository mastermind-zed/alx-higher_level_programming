#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
""" function that computes the square value of all integers of a matrix """

    current_matrix = matrix.copy()
    for i in range(len(matrix)):
        current_matrix[i] = list(map(lambda i: i**2, matrix[i]))
    return (current_matrix)
