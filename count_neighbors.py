import numpy as np


def countneighbors(A, row, col):
    count = 0
    A_rows, A_cols = A.shape
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            neighbor_row = (row + i) % A_rows
            neighbor_col = (col + j) % A_cols
            if A[neighbor_row, neighbor_col]:
                count += 1
    return count
