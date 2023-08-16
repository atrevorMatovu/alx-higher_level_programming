#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square = []
    for q in matrix:
        square.append([k**2 for k in q])
        return square
