import numpy as np


def countneighbors(A, row, col):  # Finds the number of True neighbors around an element in matrix A
    countneighbors.__doc__ = ("Finds the number of true neighbors to evolve a matrix in Conway's Game of Life \n"
                              "Inputs- A: MxN boolean matrix \n"
                              "\t row: row number of element within A \n"
                              "\t col: column number of element within A \n"
                              "Output- count: number of true neighbors in 8 surrounding elements")
    count = 0
    A_rows, A_cols = A.shape

    # Finds the number of true elements in the 8 surrounding elements
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:  # Ignores the element in consideration
                continue
            # Wraps the edges of the matrix together
            neighbor_row = (row + i) % A_rows
            neighbor_col = (col + j) % A_cols

            if A[neighbor_row, neighbor_col]:
                count += 1
    return count
