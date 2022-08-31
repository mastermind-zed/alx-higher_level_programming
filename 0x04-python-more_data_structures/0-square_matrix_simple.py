#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
   """ function that computes the square value of all integers of a matrix """
    
    new_matrix = [[x ** 2 for x in y] for y in matrix]
    return (new_matrix)
