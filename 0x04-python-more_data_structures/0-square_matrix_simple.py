#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for row in matrix:
        for j in range(3):
            row[j] = row[j] * row[j]
    return matrix
